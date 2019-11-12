def numsSameConsecDiff(N, K):
    """
    :type N: int
    :type K: int
    :rtype: List[int]
    """
    l1 = [[] for _ in range(N)]
    l1[0] = [i for i in range(1, 10)]

    if N == 1:
        l1[0].append(0)
        return l1[0]

    for i in range(1, N):
        for j in l1[i - 1]:
            a = j % 10
            if a + K < 10:
                l1[i].append(j * 10 + a + K)
            if a - K >= 0 and a - K != a + K:
                l1[i].append(j * 10 + a - K)

    return l1[N - 1]


print(numsSameConsecDiff(2, 0))
