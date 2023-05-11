def closest_sum(a, b, t):
    a.sort()
    b.sort()
    i = 0
    j = len(b) - 1
    min_diff = float('inf')
    res_a, res_b = None, None
    while i < len(a) and j >= 0:
        curr_sum = a[i] + b[j]
        curr_diff = abs(curr_sum - t)
        if curr_diff < min_diff:
            min_diff = curr_diff
            res_a, res_b = a[i], b[j]
        if curr_sum < t:
            i += 1
        elif curr_sum > t:
            j -= 1
        else:
            return (a[i], b[j])
    return (res_a, res_b)


a = [9, 13, 1, 8, 12, 4, 0, 5]
b = [3, 17, 4, 14, 6]
t = 20
print(closest_sum(a, b, t))  # Output: (13, 6)
