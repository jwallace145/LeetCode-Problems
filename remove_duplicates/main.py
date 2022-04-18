from typing import List


def remove_duplicates(nums: List[int]) -> int:
    i = 0  # first element is guaranteed to be unique, starting point
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1
