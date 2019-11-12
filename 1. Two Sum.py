def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for idx, i in enumerate(nums):
        if target - i not in d.keys():
            d[target - i] = idx
        else:
            return [idx, d[i]]
    # for idx,i in enumerate(nums):
    #     if i in d.keys() and idx!=d[i]:
    #         return [idx,d[i]]


print(twoSum([2, 7, 11, 15], 9))
