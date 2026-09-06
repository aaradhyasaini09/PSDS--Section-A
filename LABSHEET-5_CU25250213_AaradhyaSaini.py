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


#Q3
# Binary Search Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    # Insert a node
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Find minimum value
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    # Delete a node
    def delete(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)

        elif data > root.data:
            root.right = self.delete(root.right, data)

        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: Only right child
            elif root.left is None:
                return root.right

            # Case 3: Only left child
            elif root.right is None:
                return root.left

            # Case 4: Two children
            else:
                temp = self.find_min(root.right)
                root.data = temp.data
                root.right = self.delete(root.right, temp.data)

        return root


# Create BST
tree = BST()
root = None

# Insert values
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = tree.insert(root, value)

# Traversals
print("Inorder Traversal:")
tree.inorder(root)

print("\nPreorder Traversal:")
tree.preorder(root)

print("\nPostorder Traversal:")
tree.postorder(root)

# Delete a node
print("\n\nAfter deleting 30:")
root = tree.delete(root, 30)

print("Inorder Traversal:")
tree.inorder(root)
