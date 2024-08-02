#443. String Compression
class Solution:
    def compress(self, chars: List[str]) -> int:
        prevChar = '!'
        currCount = 0
        idx = 0
        for i in range(len(chars)):
            if chars[i] != prevChar:
                if currCount > 1:
                    chars[idx] = prevChar
                    idx += 1
                    for j in range(len(str(currCount))):
                        chars[idx] = str(currCount)[j]
                        idx += 1
                elif currCount == 1:
                    chars[idx] = prevChar
                    idx += 1
                prevChar = chars[i]
                currCount = 1
            else:
                currCount += 1
        
        if currCount > 1:
            chars[idx] = prevChar 
            idx += 1
            for j in range(len(str(currCount))):
                chars[idx] = str(currCount)[j]
                idx += 1
            return idx
        elif currCount == 1:
            chars[idx] = prevChar
            idx += 1

    
        
        return idx
