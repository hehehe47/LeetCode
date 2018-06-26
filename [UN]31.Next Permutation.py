'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

i.e.
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
'''


def next(nums):
    '''
    :param nums: list[int]
    :return: void
    '''
    m = sorted(nums, reverse=True)
    if m == nums:
        print('max')
        return
    f = False
    sub, m = -1, 0
    for i in range(len(nums) - 1, 0, -1):
        # if nums[i] > nums[i - 1]:
        #     if i > 1:
        #         tmp = nums[i - 1]
        #         nums[i - 1] = nums[i]
        #         nums[i] = tmp
        #     else:
        #         num = nums.pop(len(nums) - 1)
        #         nums.insert(0, num)
        #     f = True
        #     break
        # if not f:
        #     for i in range(0,int((len(nums)-1)/2)):
        #         tmp = nums[i]
        #         nums[i] = nums[len(nums)-1-i]
        #         nums[len(nums)-1-i]=tmp
        index = len(nums) - 1
        if nums[i] > nums[i - 1]:
            s1, s2 = i - 1, i
            if s2 == len(nums) - 1:
                t = nums[s2]
                nums[s2] = nums[s1]
                nums[s1] = t
                return nums
            for j in range(len(nums) - 1, s1, -1):
                if nums[j] > nums[s1]:
                    m = nums[j] - nums[s1]
                    if sub == -1:
                        sub = m
                        index = j
                    else:
                        if sub > m:
                            sub = m
                            index = j
            t = nums[index]
            nums[index] = nums[s1]
            nums[s1] = t
            nums = nums[:s2] + sorted(nums[s2:])
            return nums
    if not f:
        nums = sorted(nums)
        return nums


a = [2, 3, 1]
next(a)
print(a)
