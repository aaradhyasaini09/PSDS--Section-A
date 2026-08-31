#Q1.
# Infix to Postfix Conversion using Stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0


def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = Stack()
    postfix = ""

    for ch in expression:

        # If character is an operand
        if ch.isalnum():
            postfix += ch

        # If opening bracket
        elif ch == '(':
            stack.push(ch)

        # If closing bracket
        elif ch == ')':
            while stack.peek() != '(':
                postfix += stack.pop()
            stack.pop()  # Remove '('

        # If character is an operator
        else:
            while (not stack.is_empty() and
                   stack.peek() != '(' and
                   precedence(stack.peek()) >= precedence(ch)):
                postfix += stack.pop()

            stack.push(ch)

    # Pop remaining operators
    while not stack.is_empty():
        postfix += stack.pop()

    return postfix


expression = input("Enter infix expression: ")

result = infix_to_postfix(expression)

print("Infix Expression:", expression)
print("Postfix Expression:", result)


# Q2
# Postfix Expression Evaluation using Integer Stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0


def evaluate_postfix(expression):
    stack = Stack()

    for ch in expression:

        # If character is a number
        if ch.isdigit():
            stack.push(int(ch))

        # If character is an operator
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.push(a + b)

            elif ch == '-':
                stack.push(a - b)

            elif ch == '*':
                stack.push(a * b)

            elif ch == '/':
                stack.push(a // b)

            elif ch == '^':
                stack.push(a ** b)

    return stack.pop()


expression = input("Enter postfix expression: ")

result = evaluate_postfix(expression)

print("Postfix Expression:", expression)
print("Result:", result)
