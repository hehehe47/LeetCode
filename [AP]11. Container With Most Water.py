def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    i, j = 0, len(height) - 1
    m = 0
    while i != j:
        m = max(m, (j - i) * min(height[i], height[j]))
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1

    return m


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
