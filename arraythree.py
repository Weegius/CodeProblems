def k_largest(a, k):
    a.sort(reverse=True)
    return a[:k]

a = [5, 1, 3, 6, 8, 2, 4, 7]
k = 3
print(k_largest(a, k))  # Output: [8, 7, 6]
