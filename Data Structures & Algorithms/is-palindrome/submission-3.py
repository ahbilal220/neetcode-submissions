class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = s.replace(" ","")
        res=re.sub(r'[^a-zA-Z0-9]',"",res)
        res=res.lower()
        print(res)
        left=0
        right=len(res)-1
        while left < right:
            if res[right] == res[left]:
                left+=1
                right-=1
            else:
                return False
        return True
        
        