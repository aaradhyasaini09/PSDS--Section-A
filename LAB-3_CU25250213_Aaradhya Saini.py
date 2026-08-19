# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ================= STACK =================

top = None

# PUSH
def push(data):
    global top

    new_node = Node(data)
    new_node.next = top
    top = new_node

    print("Pushed:", data)


# POP
def pop():
    global top

    if top is None:
        print("Stack is empty")
    else:
        print("Popped:", top.data)
        top = top.next


print("STACK")

push(10)
push(20)
push(30)

pop()
pop()


# ================= QUEUE =================

front = None
rear = None

# ENQUEUE
def enqueue(data):
    global front, rear

    new_node = Node(data)

    if front is None:
        front = rear = new_node
    else:
        rear.next = new_node
        rear = new_node

    print("Enqueued:", data)


# DEQUEUE
def dequeue():
    global front, rear

    if front is None:
        print("Queue is empty")
    else:
        print("Dequeued:", front.data)
        front = front.next

        if front is None:
            rear = None


print("\nQUEUE")

enqueue(10)
enqueue(20)
enqueue(30)

dequeue()
dequeue()

