#1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ma = max(candies)
        ans = []
        for i in range(len(candies)):
                if(candies[i]+extraCandies >= ma):
                        ans.append(1)
                else:
                        ans.append(0)
        return ans