"""
Return the "centered" average of an array of ints, which we'll say is 
the mean average of the values, except ignoring the largest and smallest
values in the array. If there are multiple copies of the smallest 
value, ignore just one copy, and likewise for the largest value. Use int 
division to produce the final average. You may assume that the array is 
length 3 or more. 
"""

from test import Tester

def centered_average2(nums):
    mini = maxi = nums[0]
    sum = 0
    for num in nums:
        mini = min(mini, num)
        maxi = max(maxi, num)
        sum+=num
    sum-=(maxi+mini)
    average = sum/(len(nums)-2)
    return average

# shorter way of achieveing the same thing
def centered_average(nums):
    # sort the list
    newNums = sorted(nums)
    # cull the first and last, highest and lowest
    keeping = newNums[1:(len(newNums)-1)]
    sum = 0    
    for num in keeping:
        sum += num
    return sum/len(keeping)
    
    

Tester(centered_average([1, 2, 3, 4, 100]), 3)
Tester(centered_average([1, 1, 5, 5, 10, 8, 7]), 5)
Tester(centered_average([-10, -4, -2, -4, -2, 0]), -3)
Tester(centered_average([5, 3, 4, 6, 2]), 4)
Tester(centered_average([5, 3, 4, 0, 100]), 4)
Tester(centered_average([100, 0, 5, 3, 4]), 4)
Tester(centered_average([4, 0, 100]), 4)
Tester(centered_average([0, 2, 3, 4, 100]), 3)
Tester(centered_average([1, 1, 100]), 1)
Tester(centered_average([7, 7, 7]), 7)
Tester(centered_average([1, 7, 8]), 7)
Tester(centered_average([1, 1, 99, 99]), 50)
Tester(centered_average([1000, 0, 1, 99]), 50)
Tester(centered_average([4, 4, 4, 4, 5]), 4)
Tester(centered_average([4, 4, 4, 1, 5]), 4)
Tester(centered_average([6, 4, 8, 12, 3]), 6)
