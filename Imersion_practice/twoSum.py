#Brute force 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

#Optimal solution
#Hash map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i,n in enumerate(nums):
            rem=target-nums[i]
            if rem in mp:
                return [i,mp[rem]]
            mp[n]=i
        