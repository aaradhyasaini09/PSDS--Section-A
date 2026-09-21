#Q1
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter K: "))

current_sum = 0
for i in range(k):
    current_sum += arr[i]

max_sum = current_sum

for i in range(k, len(arr)):
    current_sum += arr[i]
    current_sum -= arr[i - k]

    if current_sum > max_sum:
        max_sum = current_sum

print("Maximum Sum:", max_sum)


#Q2
s = input("Enter string: ")
characters = set()
start = 0
max_length = 0

for end in range(len(s)):

    while s[end] in characters:
        characters.remove(s[start])
        start += 1

    characters.add(s[end])

    length = end - start + 1

    if length > max_length:
        max_length = length

print("Longest substring length:", max_length)

#Q3
n, m, k = map(int, input("Enter N, M, K: ").split())

edges = []

for i in range(m):
    u, v, weight = map(int, input().split())
    edges.append((u, v, weight))

INF = 10**9

dp = [INF] * (n + 1)

dp[1] = 0

for count in range(k):

    new_dp = dp.copy()

    for u, v, weight in edges:

        if dp[u] != INF:
            new_dp[v] = min(new_dp[v], dp[u] + weight)

        if dp[v] != INF:
            new_dp[u] = min(new_dp[u], dp[v] + weight)

    dp = new_dp

if dp[n] == INF:
    print(-1)
else:
    print("Minimum Path Weight:", dp[n])