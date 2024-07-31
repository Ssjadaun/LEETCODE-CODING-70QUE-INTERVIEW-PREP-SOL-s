#338. Counting Bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Create a list of size n + 1 with all elements initialized to 0
        result = [0] * (n + 1)

        # If n is 0, return the list
        if n == 0:
            return result

        # Base cases:
        # Set the first two elements of the list
        result[0] = 0
        if n >= 1:
            result[1] = 1

        # Iterate from 2 to n
        for x in range(2, n + 1):
            # If 'x' is even, set the x-th element of the list to 
            # the (x // 2)-th element
            if x % 2 == 0:
                result[x] = result[x // 2]
            # If x is odd, set the x-th element of the list to 
            # the (x // 2)-th element + 1
            else:
                result[x] = result[x // 2] + 1

        # Return the final list
        return result

        
        