class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        frequencies = [0] * 26
        for char in sentence:
            index = ord(char)-97
            frequencies[index] += 1
        
        return all(freq > 0 for freq in frequencies)
             
        