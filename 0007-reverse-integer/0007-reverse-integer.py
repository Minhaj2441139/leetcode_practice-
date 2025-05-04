class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if x>0:
            while(x>0):
                a=x%10
                rev=rev*10+a
                x=x//10
        
        if x<0:
            x=(-1)*x
            while(x>0):
                a=x%10
                rev=rev*10+a
                x=x//10
            rev=(-1)*rev
        
        if rev > 2 ** 31 - 1:
            return 0

        return rev 