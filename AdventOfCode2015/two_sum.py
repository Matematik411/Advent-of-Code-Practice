
def twoSum(nums, target):
    sumsFromLeft = [nums[0]]
    for x in nums[1:]:
        sumsFromLeft.append(sumsFromLeft[-1] + x)
    sumsFromRight = [nums[-1]]
    for i in range(2, len(nums)+1):
        sumsFromRight.append(sumsFromRight[-1] + nums[-i])
    sumsFromRight = sumsFromRight[::-1]

    print(sumsFromLeft)
    print(sumsFromRight)

print(twoSum([2,7,11,15], 9))