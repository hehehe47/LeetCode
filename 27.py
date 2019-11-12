def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] == val:
            j = i + 1
            while j < len(nums) and nums[j] == val:
                j += 1
            if j != len(nums):
                nums[i] = nums[j]
            count += 1
    print(nums)
    return len(nums) - count


print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
