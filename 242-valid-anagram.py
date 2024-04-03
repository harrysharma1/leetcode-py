def isAnagram(s: str, t: str) -> bool:
    s_set = set(s)
    if len(s) != len(t):
        return False
    for i in s_set:
        if s.count(i) != t.count(i):
            return False
    return True


print("anagram", "nagaram", ":", isAnagram("anagram", "nagaram"))
print("rat", "car", ":", isAnagram("rat", "car"))
