class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # alphabets = ""
        # for char in s:
        #     if char.isalnum():
        #         alphabets += char
        # return alphabets.lower() == alphabets.lower()[::-1]


        left = 0
        right = len(s)-1

        while left < right:
            while left < right and not self.isalphanumeric(s[left]):
                left += 1
            while left < right and not self.isalphanumeric(s[right]):
                right -= 1

            left_char = self.tolower(s[left])
            right_char = self.tolower(s[right])

            if left_char != right_char:
                return False
            
            left += 1
            right -= 1
        return True


    def isalphanumeric(self,char):
        return ('A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9')
            
    def tolower(self,char):
        if 'A' <= char <= 'Z':
            return chr(ord(char)+32)
        return char