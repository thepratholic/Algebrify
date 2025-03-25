from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

class Solution:
    def InfixtoPostfix(self, s):
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        output = []
        operators = []

        def is_operator(c):
            return c in precedence

        def top_precedence():
            return precedence.get(operators[-1], 0) if operators else 0

        for char in s:
            if char.isalnum():
                output.append(char)
            elif char == "(":
                operators.append(char)
            elif char == ")":
                while operators and operators[-1] != "(":
                    output.append(operators.pop())
                if operators: operators.pop()  # Remove '('
            elif is_operator(char):
                while (operators and operators[-1] != "(" and
                       precedence[char] <= top_precedence()):
                    output.append(operators.pop())
                operators.append(char)

        while operators:
            output.append(operators.pop())

        return "".join(output)

    def infixToPrefix(self, s):
        def reverse_expression(exp):
            return "".join(")" if c == "(" else "(" if c == ")" else c for c in reversed(exp))

        rev_exp = reverse_expression(s)
        postfix_exp = self.InfixtoPostfix(rev_exp)
        return reverse_expression(postfix_exp)

    def postfixToInfix(self, postfix):
        stack = []
        for char in postfix:
            if char.isalnum():
                stack.append(char)
            elif len(stack) >= 2:  # Ensure stack has enough operands
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(f"({t2}{char}{t1})")
        return stack[-1] if stack else "Invalid Expression"

    def prefixToInfix(self, prefix):
        stack = []
        for char in reversed(prefix):
            if char.isalnum():
                stack.append(char)
            elif len(stack) >= 2:
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(f"({t1}{char}{t2})")
        return stack[-1] if stack else "Invalid Expression"

    def postfixToPrefix(self, postfix):
        stack = []
        for char in postfix:
            if char.isalnum():
                stack.append(char)
            elif len(stack) >= 2:
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(char + t2 + t1)
        return stack[-1] if stack else "Invalid Expression"

    def prefixToPostfix(self, prefix):
        stack = []
        for char in reversed(prefix):
            if char.isalnum():
                stack.append(char)
            elif len(stack) >= 2:
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t1 + t2 + char)
        return stack[-1] if stack else "Invalid Expression"

solution = Solution()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    expression = data.get('expression', '').strip()
    conversion_type = data.get('conversion_type', '')

    if not expression:
        return jsonify({'result': 'Error: Empty expression'}), 400

    try:
        conversion_map = {
            'infix_to_postfix': solution.InfixtoPostfix,
            'infix_to_prefix': solution.infixToPrefix,
            'postfix_to_infix': solution.postfixToInfix,
            'prefix_to_infix': solution.prefixToInfix,
            'postfix_to_prefix': solution.postfixToPrefix,
            'prefix_to_postfix': solution.prefixToPostfix,
        }
        result = conversion_map.get(conversion_type, lambda x: "Invalid conversion type")(expression)
    except Exception as e:
        return jsonify({'result': f'Error: {str(e)}'}), 500

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
