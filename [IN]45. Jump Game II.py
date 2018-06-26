'''
Q:https://leetcode.com/problems/jump-game-ii/description/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4] #3,4,7,3,2,1,6,4,4,4,8,9,1 # 1,2,3,4,5,7,8
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

timestamp:2018-6-26 19:45:52
'''

a = list(map(int, input().split(',')))
print(a)


def asd(a):
    if 0 in a:
        return 0
    index, count = 0, 0
    while index < len(a):
        count += 1
        flag_max = 0
        i_range = a[index]
        if index + i_range >= len(a) - 1:
            return count
        max_step = a[index + 1] + 1
        if index + 1 + max_step >= len(a) - 1:
            count += 1
            return count
        for ran in range(1, i_range + 1):
            act_index = ran + index
            if act_index > len(a):
                break_flag = 1
                break
            else:
                if act_index - index + a[act_index] > max_step:
                    max_step = act_index + a[act_index]
                    index = act_index
                    flag_max = 1
        if flag_max != 1:
            index = index + 1
    return count


####################
def jump(a):
    if not a or len(a) == 0:
        return 0
    lastReach, reach, step, i = 0, 0, 0, 0
    while i <= reach and i < len(a):
        if i > lastReach:
            step += 1
            lastReach = reach
        reach = max(reach, a[i] + i)
        i += 1
    if reach < len(a) - 1:
        return 0
    return step


print(jump(a))
