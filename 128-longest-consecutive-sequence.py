# https://leetcode.com/problems/longest-consecutive-sequence/description/

# Average Time: 360.60 ms
# Average Memory: 34.66 ms
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    sorted_set = set(sorted(nums))
    count = 0
    for i in nums:
        if (i-1) not in sorted_set:
            n_count = 0
            while (i+n_count) in sorted_set:
                n_count += 1
            count = max(n_count, count)
    return count


print(f"Input: [100,4,200,1,3,2]\nOutput:{longestConsecutive([100, 4, 200, 1, 3, 2])}")  # noqa:E501
print(f"Input: [0,3,7,2,5,8,4,6,0,1]\nOutput:{longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])}")  # noqa:E501
