#stack
stack = []
for i in range(1,6):
    stack.append(i)         #push
    print("pushed: ",i, ", stack:", stack)
for i in range(len(stack)):
    stack.pop()             #pop
    print("popped: ",i,", stack:", stack)

#queue
queue = []
for i in range(1,4):
    queue.append(i)         #Enqueued
    print("Enqueued: ",i, ", queue:", queue)
for i in range(len(queue)):
    queue.pop(0)
    print("Dequeued: ",i,", queue:", queue)   #Dequeued
