from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class Solution:
    # Methods copied from your provided code
    def InfixtoPostfix(self, s):
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        output = []
        operators = []

        def is_operator(c):
            return c in precedence
        
        def top_precedence():
            if operators:
                return precedence.get(operators[-1], 0)
            return 0

        for char in s:
            if char.isalnum():
                output.append(char)
            elif char == "(":
                operators.append(char)
            elif char == ")":
                while operators and operators[-1] != "(":
                    output.append(operators.pop())
                operators.pop()
            elif is_operator(char):
                while (operators and operators[-1] != "(" and
                       precedence[char] <= top_precedence()):
                    output.append(operators.pop())
                operators.append(char)

        while operators:
            output.append(operators.pop())

        return "".join(output)

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

    def postfixToInfix(self, postfix):
        stack = []
        for char in postfix:
            if char.isalnum(): stack.append(char)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                con = "(" + t2 + char + t1 + ")"
                stack.append(con)
        return stack[-1]
    
    def prefixToInfix(self, s):
        stack = []
        for char in reversed(s):
            if char.isalnum(): stack.append(char)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                con = "(" + t1 + char + t2 + ")"
                stack.append(con)
        return stack[-1]
    
    def postfixToPrefix(self, s):
        stack = []
        for char in s:
            if char.isalnum(): stack.append(char)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                con = char + t2 + t1
                stack.append(con)
        return stack[-1]
    
    def prefixToPostfix(self, s):
        stack = []
        for char in reversed(s):
            if char.isalnum(): stack.append(char)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                con = t1 + t2 + char
                stack.append(con)
        return stack[-1]

solution = Solution()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    expression = data.get('expression', '')
    conversion_type = data.get('conversion_type', '')
    
    if conversion_type == 'infix_to_postfix':
        result = solution.InfixtoPostfix(expression)
    elif conversion_type == 'infix_to_prefix':
        result = solution.infixToPrefix(expression)
    elif conversion_type == 'postfix_to_infix':
        result = solution.postfixToInfix(expression)
    elif conversion_type == 'prefix_to_infix':
        result = solution.prefixToInfix(expression)
    elif conversion_type == 'postfix_to_prefix':
        result = solution.postfixToPrefix(expression)
    elif conversion_type == 'prefix_to_postfix':
        result = solution.prefixToPostfix(expression)
    else:
        result = "Invalid conversion type"
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)