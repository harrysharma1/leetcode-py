
from typing import List


def binarySearch(nums: List[int], target: int) -> bool:
    l = 0
    r = len(nums)-1

    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return False


print(binarySearch([1, 4, 12, 13, 19, 59, 100, 222, 322], 100))
