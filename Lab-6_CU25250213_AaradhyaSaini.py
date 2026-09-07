#Q1
def three_sum(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == 0:
                    print("Three numbers:", arr[i], arr[j], arr[k])
                    print("Sum:", arr[i] + arr[j] + arr[k])


arr = list(map(int, input("Enter numbers: ").split()))

three_sum(arr)

#Q2
n = int(input("Enter number of terms: "))

a = 0
b = 1
print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#Q3
def tower_of_hanoi(n, source, auxiliary, destination):

    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter number of disks: "))

tower_of_hanoi(n, 'A', 'B', 'C')


  
