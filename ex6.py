nums = list(input())
target = int(input())
for i in range(len(nums)):
    for k in range(i+1,len(nums)):
        if nums[i]+nums[k] == target:
            print([i,k])
