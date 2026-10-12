T = int(input("Enter number of test cases: "))
for i in range(T):
    S = input("Enter string: ")
    freq = {}
    for ch in S:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1
    ans = 0
    for ch in freq:
        ans += freq[ch] // 2
    print("Max no of palindromes:", ans)