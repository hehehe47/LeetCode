def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    if not str:
        return 0
    s = str.lstrip(' ')
    if not s:
        return 0
    l = []
    t = True if s[0] == '-' else False
    if s[0] == '+':
        s = s[1:]
    b = 0
    for i in range(t, len(s)):
        if 48 <= ord(s[i]) <= 57:
            a = ord(s[i]) - 48
            b = b * 10 + a
        else:
            break
    if b and t:
        b *= -1

    if b < -2 ** 31:
        return -2 ** 31

    elif b >= 2 ** 31:
        return (2 ** 31 - 1)
    elif b:
        return b
    else:
        return 0


print(myAtoi('++'))
