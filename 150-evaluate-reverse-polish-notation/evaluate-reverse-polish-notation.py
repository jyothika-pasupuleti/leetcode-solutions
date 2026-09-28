class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()

                if token == "+":
                    stack.append(b + a)

                elif token == "-":
                    stack.append(b - a)

                elif token == "*":
                    stack.append(b * a)

                elif token == "/":
                    stack.append(int(b / a))

        return stack[-1]