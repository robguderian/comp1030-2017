
nums = [30, 10, 20]

# first swap
print "phase 0: " + str(nums)
temp = nums[0]
nums[0] = nums[1]
print "phase 1: " + str(nums)
nums[1] = temp
print "phase 2: " + str(nums)


# second swap, 1 and 2
temp = nums[2]
nums[2] = nums[1]
print "phase 1: " + str(nums)
nums[1] = temp
print "phase 2: " + str(nums)
