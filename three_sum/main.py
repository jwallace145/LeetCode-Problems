from typing import List


def three_sum(nums: List[int]) -> List[set]:
    # sorts in place
    nums.sort()
    results = []
    length_of_list = len(nums)
    for i in range(length_of_list):
        # ensure that we keep bumping i until we get the last element with that value
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        front_ptr = i + 1
        back_ptr = length_of_list - 1
        while front_ptr < back_ptr:
            if nums[front_ptr] + nums[back_ptr] == target:
                results.append(nums[i], nums[front_ptr], nums[back_ptr])
                front_ptr += 1
                while front_ptr < back_ptr and nums[front_ptr] == nums[front_ptr - 1]:
                    front_ptr += 1
            elif nums[front_ptr] + nums[back_ptr] < target:
                front_ptr += 1
            else:
                back_ptr -= 1
    return results
