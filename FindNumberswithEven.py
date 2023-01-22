nums = [555,901,482,1771]

cnt=0
for i in range(len(nums)):
    if len(str(nums[i])) % 2 == 0:
        cnt+=1
    # if nums[i] % 2 == 0:
    #     cnt+=1

print(cnt)
