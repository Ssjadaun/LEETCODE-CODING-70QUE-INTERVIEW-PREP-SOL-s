#151. Reverse Words in a String
class Solution(object):
    def reverseWords(self, s):
        length = len(s)
        word_positions = []  # To store start and end indices of words
        
        i = 0
        # Iterate through the string to identify word boundaries
        while i < length:
            # Skip leading spaces
            while i < length and s[i] == ' ':
                i += 1
            if i == length:
                break
            
            start = i  # Start of the word
            
            # Move to the end of the word
            while i < length and s[i] != ' ':
                i += 1
            end = i - 1  # End of the word
            
            # Store the start and end indices of the word
            word_positions.append((start, end))
        
        result = []
        # Reverse the order of the words and build the result string
        for start, end in reversed(word_positions):
            word = s[start:end + 1]
            result.append(word)
        
        return ' '.join(result)