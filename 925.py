def isLongPressedName(name, typed):
    """
    :type name: str
    :type typed: str
    :rtype: bool
    """
    tmp = ''

    name, typed = list(name), list(typed)
    # while name and typed:
    #     if name[0] == typed[0]:
    #         tmp = name.pop(0)
    #         typed.pop(0)
    #     elif tmp == typed[0]:
    #         tmp = typed.pop(0)
    #     else:
    #         return False
    # while typed:
    #
    #
    # if not name and not typed:
    #     return True
    i, j = 0, 0
    while j < len(typed):
        if i < len(name) and typed[j] == name[i]:
            i += 1
            j += 1
        elif typed[j] == typed[j - 1]:
            j += 1
        else:
            return False
    if j == len(typed) and i == len(name):
        return True
    else:
        return False


print(isLongPressedName("pyplrz", "ppyypllr"))
