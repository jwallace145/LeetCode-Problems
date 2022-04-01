from three_sum.main import three_sum


class TestThreeSum:
    def test_three_sum_simple(self):
        assert three_sum(nums=[-1, 0, 1, 2, -1, 4]) == [[-1, -1, 2], []]
