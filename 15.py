def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # 最简单的 hash记任意两数的和，第二次遍历查找hash
    # 问题在于没法去重
    # d = {}
    # l = []
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] not in d:
    #             d[nums[i] + nums[j]] = [[nums[i], nums[j]]]
    #         else:
    #             d[nums[i] + nums[j]].append([nums[i], nums[j]])
    # for i in nums:
    #     if -i in d.keys():
    #         for c in d[-i]:
    #             e = c.copy()
    #             e.append(i)
    #             l.append(e)
    # return l


print(threeSum([-1, 0, 1, 2, -1, -4]))
d = {1: 2}
enumerate
