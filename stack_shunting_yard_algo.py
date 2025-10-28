def operations(op):
    operation = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return operation.get(op, 0)

def infix_to_postfix(expression):
    output = []
    stack = []
    postfix = expression.split()

    for char in postfix:
        if char.isalpha() or char.isnumeric():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and operations(stack[-1]) >= operations(char):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)