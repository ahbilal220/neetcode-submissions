class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr=""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr
        
    def decode(self, s: str) -> List[str]:
        dls=[]
        i=0
        while i<len(s):
            j=i
            while s[j] != "#": j+=1
            l = int(s[i:j])
            dls.append(s[j+1:j+l+1])

            i=j+l+1
        return dls


