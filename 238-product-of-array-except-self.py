# https://leetcode.com/problems/product-of-array-except-self/description/

# Average Runtime: 263 ms
# Average Memory:  25.76 MB

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    ret = [1] * len(nums)
    pre = 1
    for i in range(len(nums)):
        ret[i] = pre
        pre *= nums[i]

    post = 1
    for i in range(len(nums)-1, -1, -1):
        ret[i] *= post
        post *= nums[i]

    return ret


print(f"Input: [-1,1,0,-3,3]\nOutput:{productExceptSelf([-1, 1, 0, -3, 3])}")
print(f"Input: [1,2,3,4]\nOutput:{productExceptSelf([1, 2, 3, 4])}")
