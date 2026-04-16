class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol=[]
        sorted_nums=sorted(nums)
        n=len(sorted_nums)
        for i in range(n):
            if i>0 and sorted_nums[i] == sorted_nums[i-1]: continue
            right = n-1
            left=i+1 
            while left < right:
                total=sorted_nums[i]+sorted_nums[left]+sorted_nums[right]
                if total ==0:
                    sol.append([sorted_nums[i],sorted_nums[left],sorted_nums[right]])
                    left+=1
                    while left < right and sorted_nums[left] == sorted_nums[left-1]: left+=1
                    
                elif total > 0: right-=1
                elif total < 0: left+=1  
              
        return sol