class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphabets = ""
        for char in s:
            if char.isalnum():
                alphabets += char
        return alphabets.lower() == alphabets.lower()[::-1]