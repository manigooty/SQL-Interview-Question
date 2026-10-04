class Solution:
    def checkValidString(self, s: str) -> bool:
        low=0
        high=0
        for w in s:
            if w=='(':
                low+=1
                high+=1
            elif w==')':
                low-=1
                high-=1
            else:
                low-=1
                high+=1
            if high<0:
                return False
            if low<0:
                low=0
        return low==0
        