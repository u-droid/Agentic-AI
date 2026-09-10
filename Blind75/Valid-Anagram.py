# Intial Solution
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            print(f"({s}) and ({t}) are not anagrams!")
            return False
        s_hash = {}
        t_hash = {}
        for s_i, t_i in zip(s,t):
            s_hash[s_i] = 1 + s_hash.get(s_i, 0) 
            t_hash[t_i] = 1 + t_hash.get(t_i, 0)
        if s_hash!=t_hash:
            print(f"({s}) and ({t}) are not anagrams!")
            return False
        print(f"({s}) and ({t}) are anagrams!")
        return True

# Pythonic way
from collections import Counter
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)== Counter(t)

def main():
    Solution1().isAnagram(
            s='racecar',
            t='racings'
        )
    Solution1().isAnagram(
        s='racecar',
        t='carrace'
    )
    print(Solution2().isAnagram(
        s='abc',
        t='bce'
    ))
    print(Solution2().isAnagram(
        s='anagram',
        t='naagram'
    ))


if __name__=="__main__":
    main()
    