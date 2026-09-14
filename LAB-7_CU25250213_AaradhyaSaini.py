#Q1
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = \
                    self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def delete_min(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return minimum

    def heapify_down(self, index):
        n = len(self.heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = \
                    self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break


# Input
arr = list(map(int, input("Enter elements: ").split()))

# Create Min Heap
heap = MinHeap()

for value in arr:
    heap.insert(value)

print("Min Heap:", heap.heap)

# Priority Queue
print("Priority Queue:", end=" ")

while len(heap.heap) > 0:
    print(heap.delete_min(), end=" ")

# Heap Sort
heap = MinHeap()

for value in arr:
    heap.insert(value)

sorted_array = []

while len(heap.heap) > 0:
    sorted_array.append(heap.delete_min())

print("\nHeap Sort:", sorted_array)


#Q2
def rearrange_array(arr):
    arr.sort()

    n = len(arr)
    result = []

    if n % 2 == 0:
        # Even number of elements
        left = n // 2 - 1
        right = n - 1

        result.append(arr[left])
        left -= 1

        while left >= 0:
            result.append(arr[left])
            result.append(arr[right])
            left -= 1
            right -= 1

        result.append(arr[0])

    else:
        # Odd number of elements
        result.append(arr[n // 2 + 1])

        left = n // 2 - 1
        right = n - 1

        while left >= 0:
            result.append(arr[left])
            result.append(arr[right])
            left -= 1
            right -= 1

        result.append(arr[n // 2])

    return result


arr = list(map(int, input("Enter elements: ").split()))

result = rearrange_array(arr)

total = 0

for i in range(len(result) - 1):
    total += abs(result[i] - result[i + 1])

print("Rearranged Array:", result)
print("Maximum Sum:", total)


#Q3
arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target: "))

start = 0
current_sum = 0
min_length = len(arr) + 1

for end in range(len(arr)):

    current_sum = current_sum + arr[end]

    while current_sum > target:

        length = end - start + 1

        if length < min_length:
            min_length = length

        current_sum = current_sum - arr[start]
        start = start + 1

if min_length == len(arr) + 1:
    print("Smallest Subarray Length: -1")
else:
    print("Smallest Subarray Length:", min_length)