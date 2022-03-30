from minimum_number_of_vertices_to_reach_all_nodes.main import (
    find_smallest_set_of_vertices,
)


class TestMinimumNumberOfVerticesToReachAllNodes:
    def test_example_1(self):
        assert (
            find_smallest_set_of_vertices(
                n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
            )
            == set()
        )

    def test_example_2(self):
        assert (
            find_smallest_set_of_vertices(
                n=5, edges=[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
            )
            == set()
        )
