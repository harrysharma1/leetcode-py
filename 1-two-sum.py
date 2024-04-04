# https://leetcode.com/problems/two-sum/description/

# Average Runtime: 57.8 ms
# Average Memory: 17.98 MB

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i, j in enumerate(nums):
        if j in d:
            return [i, d[j]]
        d[target-j] = i
    return []


print(f"List: [2,7,11,15] \n Target: 9 \n Array Position: {twoSum([2, 7, 11, 15], 9)}")  # noqa:E501
print(f"List: [3,2,4] \n Target: 6 \n Array Position: {twoSum([3, 2, 4], 6)}")
print(f"List: [3,3] \n Target: 6 \n Array Position: {twoSum([3, 3], 6)}")
