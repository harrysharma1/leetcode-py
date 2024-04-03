def containsDuplicate(nums: list[int]) -> bool:
    a = list(set(nums))
    return len(a) != len(nums)


print([1, 2, 3, 1], containsDuplicate([1, 2, 3, 1]))
print([1, 2, 3, 4], containsDuplicate([1, 2, 3, 4]))
print([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
      containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
