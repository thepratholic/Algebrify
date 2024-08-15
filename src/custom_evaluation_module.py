class Solution:
    # 1)Infix to Postfix
    def InfixtoPostfix(self, s):
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        output = []
        operators = []

        def is_operator(c):
            return c in precedence
        
        def top_precedence():
            if operators:
                return precedence.get(operators[-1], 0)
            return 0  # Return 0 if there are no operators on the stack

        for char in s:
            if char.isalnum():
                output.append(char)
            elif char == "(":
                operators.append(char)
            elif char == ")":
                while operators and operators[-1] != "(":
                    output.append(operators.pop())
                operators.pop()  # Remove the '(' from the stack
            elif is_operator(char):
                while (operators and operators[-1] != "(" and
                       precedence[char] <= top_precedence()):
                    output.append(operators.pop())
                operators.append(char)

        while operators:
            output.append(operators.pop())

        return "".join(output)
    
    # 2)Infix to Prefix
    def infixToPrefix(self, string):
        def reverse_expression(exp):
            rev_exp = []
            for char in reversed(exp):
                if char == "(": rev_exp.append(")")
                elif char == ")": rev_exp.append("(")
                else: rev_exp.append(char)
            return "".join(rev_exp)
        
        def InfixToPostfix(s):
            stack = []
            postfix = []
            precedence = {"+":1, "-":1, "*":2, "/":2, "^":3}
            def top_precedence():
                if stack:
                    return precedence.get(stack[-1])
                return 0
            for char in s:
                if char.isalnum():
                    postfix.append(char)
                elif char == "(":
                    stack.append(char)
                elif char == ")":
                    while stack and stack[-1] != "(":
                        postfix.append(stack.pop())
                    stack.pop()
                else:
                    while stack and precedence[char] < top_precedence():
                        postfix.append(stack.pop())
                    stack.append(char)
            while stack:
                postfix.append(stack.pop())
            return "".join(postfix)
        
        rev_expression = reverse_expression(string)
        postfix_expression = InfixToPostfix(rev_expression)
        ans = reverse_expression(postfix_expression)
        return ans
    
    # 3) Postfix to Infix
    def postfixToInfix(self, postfix):
        stack = []
        for char in postfix:
            if char.isalnum(): stack.append(char)
            else:
                t1 = stack[-1]
                stack.pop()
                t2 = stack[-1]
                stack.pop()
                con = "(" + t2 + char + t1 + ")"
                stack.append(con)
        return stack[-1]
    
    # 4) Prefix to Infix
    def prefixToInfix(self, s):
        stack = []
        for char in reversed(s):
            if char.isalnum(): stack.append(char)
            else:
                t1 = stack[-1]
                stack.pop()
                t2 = stack[-1]
                stack.pop()
                con = "(" + t1 + char + t2 + ")"
                stack.append(con)
        return stack[-1]
    
    # 5) Postfix to Prefix
    def postfixToPrefix(self, s):
        stack = []
        for char in s:
            if char.isalnum(): stack.append(char)
            else:
                t1 = stack[-1]
                stack.pop()
                t2 = stack[-1]
                stack.pop()
                con = char + t2 + t1
                stack.append(con)
        return stack[-1]
    
    # 6) Prefix to Postfix
    def prefixToPostfix(self, s):
        stack = []
        for char in reversed(s):
            if char.isalnum(): stack.append(char)
            else:
                t1 = stack[-1]
                stack.pop()
                t2 = stack[-1]
                stack.pop()
                con = t1 + t2 + char
                stack.append(con)
        return stack[-1]

s = Solution()
# print(s.infixToPrefix("a+b"))
