#345. Reverse Vowels of a String
class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E','I','O','U']
        l = 0
        r = len(s) - 1
        s = list(s)
        while l<r:
            if s[l] in v and s[r] in v:
                s[l],s[r] = s[r], s[l]
                l += 1
                r -= 1
            if s[l] not in v:
                l += 1
            if s[r] not in v:
                r -= 1
    
        return ''.join(s)