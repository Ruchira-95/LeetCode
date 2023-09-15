class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        l=max(l1,l2)
        a=[]
        for i in range(l):
            if(l1==0):
                a.append(word2[i])
                continue
            if(l2==0):
                a.append(word1[i])
                continue
            a.append(word1[i])
            a.append(word2[i])
            l1-=1
            l2-=1
        return ''.join(a)


obj=Solution()
print(obj.mergeAlternately(input(), input()))