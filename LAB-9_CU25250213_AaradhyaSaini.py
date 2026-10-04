
def solve(N, A):
    positive = 0
    negative = 0

    for x in A:
        if x > 0:
            positive += x
        elif x < 0:
            negative += x

    total = positive + negative

    if total > 0:
        return -1

    if 2 * positive > -negative:
        return -1

    return -total


T = int(input("Enter number of test cases: "))

for i in range(T):
    print("\nTest case", i + 1)

    N = int(input("Enter number of elements: "))
    A = list(map(int, input("Enter elements separated by space: ").split()))

    answer = solve(N, A)

    print("Minimum operations:", answer)