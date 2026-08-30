class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # for b in s:
        #     if b in "([{":
        #         stack.append(b)
        #     else:
        #         if stack:
        #             if (b == ')' and stack.pop() == '(')  or (b == ']' and stack.pop() == '[')  or (b == '}' and stack.pop() == '{'):
        #                 stack.pop()
        #             else:
        #                 return False
        #         else:
        #             return False
        # if not stack:
        #     return True

        stack = []
        pairs = {")":"(",'}':'{',"]":"["}
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False
        if not stack:
            return True
        return False
        
        