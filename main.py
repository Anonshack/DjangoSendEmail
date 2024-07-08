def test(temp):
    n = len(temp)
    for i in range(n):
        for j in range(0, n - i - 1):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]

