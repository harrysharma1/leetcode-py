import time
from typing import List


def bubbleSort(nums: List[int], size: int) -> List[int]:
    for i in range(0, size-1):
        for j in range(0, size-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums


start = time.time() * 1000
print(f"Before Sort: [2,3,1,8,2,0,19,6,38] After Sort: {bubbleSort([2, 3, 1, 8, 2, 0, 19, 6, 38], len([2, 3, 1, 8, 2, 0, 19, 6, 38]))}")  # noqa: E501
end = time.time() * 1000
print(f"Time taken to sort: {end-start}")
