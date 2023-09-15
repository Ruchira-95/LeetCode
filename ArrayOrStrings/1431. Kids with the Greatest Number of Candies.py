class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        m=max(candies)
        l=[]
        for i in range(len(candies)):
            if m<=candies[i]+extraCandies:
                l.append(True)
            else:
                l.append(False)
        return l

a=Solution()
l=list(map(int,input().strip().split()))
n=int(input())
print(a.kidsWithCandies(l, n))