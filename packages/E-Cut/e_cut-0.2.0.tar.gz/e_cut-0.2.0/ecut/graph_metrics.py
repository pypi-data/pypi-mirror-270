from sklearn.decomposition import PCA
import numpy as np
from .base_types import BaseNode, BaseMetric, BaseFragment
from .gcut_utils.distribution import Distribution


class EnsembleFragment(BaseFragment):

    def __init__(self):
        super().__init__()
        self.path_len = 0.  # the path length of this fragment


class EnsembleNode(BaseNode):
    """
    The dist will be used for global cost calculation.
    """

    def __init__(self, id):
        super().__init__(id)
        self.gof_cost = 0.  # the gof of this fragment w.r.t. a soma
        self.path_dist = 0.  # the path distance to soma


class EnsembleMetric(BaseMetric):
    def __init__(self, gof_weight=1., angle_weight=4., radius_weight=2., anchor_dist=20., avg_branch_len=50.,
                 distribution=Distribution(), epsilon=1e-7, soma_radius=20.):
        """
        :param gof_weight: the weight of the global gof metric
        :param angle_weight: the weight of the local angle metric
        :param radius_weight: the weight of the local radius metric
        :param anchor_dist: the distance to calculate fragment angle
        :param avg_branch_len: the (expected) average branch length, used to scale the probability of gof
        :param distribution: GOF distribution class, should load the data before use
        :param epsilon: for preventing zero division
        """
        self._distribution = distribution
        self._gof_weight = gof_weight
        self._angle_weight = angle_weight
        self._radius_weight = radius_weight
        self._anchor_dist = anchor_dist
        self.avg_branch_len = avg_branch_len
        self._epsilon = epsilon
        self._soma_radius = soma_radius
        distribution.load_distribution()

    def init_fragment(self, cut, frag: EnsembleFragment):
        # calculate path length
        pts_list = np.array([cut.swc[i][2:5] for i in frag.nodes])
        frag.path_len = np.linalg.norm((pts_list[1:] - pts_list[:-1]) * cut.res, axis=1).sum()

    def _get_len(self, pts_list, res):
        pts_list = np.array(pts_list)
        diff = (pts_list[1:] - pts_list[:-1]) * res
        return np.linalg.norm(diff, axis=1).sum()

    def __call__(self, cut, soma, frag_par, frag_ch, reverse):
        # the angle calculation is based on the pca pc1 of the two point lists
        # there's a case where pc1 DNE, it returns a vector of (1,0,0)
        pts_par, radius_par = self._path_upstream(cut, soma, frag_par)
        pts_ch, radius_ch = self._path_within(cut, frag_ch, not reverse)
        par_len = self._get_len(pts_par, cut.res)
        ch_len = self._get_len(pts_ch, cut.res)
        conf = np.sqrt(par_len * ch_len) / self._anchor_dist
        angle = self.get_angle(pts_par, pts_ch, cut.res) / np.pi
        radius = max(np.mean(radius_ch) - np.mean(radius_par), 0) / np.mean(radius_ch)
        pts_list = [cut.swc[i][2:5] for i in cut.fragment[frag_ch].nodes]
        if not reverse:
            pts_list = pts_list[::-1]
        frag_node: EnsembleNode = cut.fragment_trees[soma][frag_par]
        frag: EnsembleFragment = cut.fragment[frag_ch]

        frag_gof = self.get_gof(pts_list, cut.swc[soma][2:5], cut.res)
        pseudo_order = frag_node.path_dist / self.avg_branch_len  # farther branches will be more even in probability
        frag_gof_prob = self._distribution.probability(frag_gof) * min(1, np.log(1 + 1 / (pseudo_order + self._epsilon)))
        # no suppressing short branches
        ret = {'path_dist': frag_node.path_dist + frag.path_len}
        ret['gof_cost'] = frag_node.gof_cost + (1 - frag_gof_prob) * frag.path_len
        ret['cost'] = (angle * self._angle_weight *  + radius * self._radius_weight) * conf + \
                      ret['gof_cost'] / max(self._soma_radius, ret['path_dist']) * self._gof_weight # equals avg gof along the path
        return ret

    def _path_upstream(self, cut, soma: int, frag_id: int):
        """
        Construct a list of nodes based on an existing fragment tree, starting from current fragment
        towards the soma of the fragment tree.
        """
        path_dist = 0
        fragment_tree = cut.fragment_trees[soma]
        frag_node = fragment_tree[frag_id]
        pts_list = []
        radius_list = []
        while path_dist < self._anchor_dist:  # stop when exceeding the anchor dist
            # nodes in a fragment start from child to parent in the original tree
            # the path needs to start from a far end whenever
            a, b, c = self._path_within(cut, frag_node.id, frag_node.reverse, path_dist, True)
            pts_list.extend(a)
            radius_list.extend(b)
            path_dist += c
            # finish one fragment and get its parent
            p = frag_node.parent
            if p == -1:
                break
            frag_node = fragment_tree[p]
        return pts_list, radius_list

    def _path_within(self, cut, frag_id: int, reverse: bool, path_dist=0., return_distance=False):
        """
        Construct a list of nodes departing from the soma within current fragment.
        The direction is explicitly given.
        """
        pts_list = []
        radius_list = []
        nodes = cut.fragment[frag_id].nodes
        if reverse:
            nodes = reversed(nodes)
        for i in nodes:
            pts_list.append(np.array(cut.swc[i][2:5]))
            radius_list.append(cut.swc[i][5])
            if len(pts_list) > 1:
                path_dist += np.linalg.norm((pts_list[-2] - pts_list[-1]) * cut.res)
            if path_dist > self._anchor_dist:
                break  # stop when exceeding the anchor dist
        if return_distance:
            return pts_list, radius_list, path_dist
        else:
            return pts_list, radius_list

    @staticmethod
    def line_fit_pca(pts_list: list[np.ndarray]) -> np.ndarray:
        """
        fit 3D points to a straight line.
        :param pts_list: a list of 3D connected points
        :return: a 3D vector fitted to the list
        """
        pca = PCA(n_components=1)
        pca.fit(pts_list)
        line_direction = pca.components_[0]
        temp = pts_list[-1] - pts_list[0]
        if temp.dot(line_direction) < 0:
            line_direction = -line_direction
        return line_direction

    def get_angle(self, pts_list1: list[np.ndarray], pts_list2: list[np.ndarray], res):
        """
        The angle between 2 vectors (fitted from 2 point lists), but supplementary.
        the vectors share the start point, but to make it fit for scoring, its supplementary is returned.
        so a smaller angle means a more straight connection.

        :param pts_list1: a list of 3D points for one branch
        :param pts_list2: a list of 3D points for another branch
        :return: an angle in arc
        """
        vec1 = -self.line_fit_pca(pts_list1) * res
        vec2 = self.line_fit_pca(pts_list2) * res
        vec3 = (pts_list2[0] - pts_list1[0]) * res
        if np.linalg.norm(vec3) > self._epsilon:
            cos1 = vec1.dot(vec3) / (np.linalg.norm(vec1) * np.linalg.norm(vec3))
            cos2 = vec2.dot(vec3) / (np.linalg.norm(vec2) * np.linalg.norm(vec3))
            return np.arccos(np.clip(cos1, -1, 1)) + np.arccos(np.clip(cos2, -1, 1))
        else:
            cos = vec1.dot(vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
            return np.arccos(np.clip(cos, -1, 1))

    def get_gof(self, pts_list: list[tuple[float, float, float]], soma: np.ndarray, res) -> float:
        pts_list = np.array(pts_list)
        tan = (pts_list[1:] - pts_list[:-1]) * res
        tan_norm = np.linalg.norm(tan, axis=1, keepdims=True)
        tan /= tan_norm + self._epsilon
        ps = (pts_list[:-1] - soma) * res
        ps_norm = np.linalg.norm(ps, axis=1, keepdims=True)
        ps /= ps_norm + self._epsilon
        proj = np.clip(np.sum(tan * ps, axis=1), -1, 1)
        gof = np.mean(np.arccos(proj))
        return gof
