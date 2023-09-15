class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=['a','e','i','o','u','A','E','I','O','U']
        a=[]
        b=[]
        for i in s:
            if i in vowel:
                a.append(i)
        
        a=a[::-1]
        l=0
        for j in range(len(s)):
            if s[j] in vowel:
                b.append(a[l])
                l=l+1
            else:
                b.append(s[j])
        z=''.join(b)
        return(z)
    
a=Solution()
print(a.reverseVowels(input()))