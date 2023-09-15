class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1=len(str1)
        l2=len(str2)
        l=min(l1,l2)
        
        def isDivisor(x):
            if l1%x or l2%x:
                return False
            f1, f2 = l1//x, l2//x
            return str1[:x]*f1==str1 and str1[:x]*f2==str2

        for i in range(l, 0, -1):
            if isDivisor(i):
                return str1[:i]
        return ""
    
a=Solution()
print(a.gcdOfStrings(input(), input()))