nums = [-4,-1,0,3,10]

squares_nums = []

for i in range(len(nums)):
    squares_nums.append(nums[i]*nums[i])

print(sorted(squares_nums))