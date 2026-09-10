from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, num in enumerate(nums):
            x = target - num
            if x in hash:
                return [hash[x], index]
            hash[num] = index

if __name__=="__main__":
    nums = [4,5,6]
    target = 10
    result = Solution().twoSum(nums, target)
    print(result)