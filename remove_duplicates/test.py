from remove_duplicates.main import remove_duplicates


class TestRemoveDuplicates:
    def test_simple_duplicates(self):
        nums = [1, 1, 2]
        assert remove_duplicates(nums) == 2
        for i, val in enumerate([1, 2]):
            assert nums[i] == val

    def test_many_duplicates(self):
        nums = [1, 1, 1, 1, 2, 2, 2, 2, 2]
        assert remove_duplicates(nums) == 2
        for i, val in enumerate([1, 2]):
            assert nums[i] == val
