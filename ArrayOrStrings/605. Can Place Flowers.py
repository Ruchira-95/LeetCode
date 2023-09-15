class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        f=[0]+flowerbed+[0]
        for i in range(1, len(f)-1):
            if f[i-1]==0 and f[i]==0 and f[i+1]==0:
                f[i]=1
                n-=1
        return n<=0

a=Solution()
l= list(map(int,input().strip().split()))
n=int(input())
print(a.canPlaceFlowers(l, n))