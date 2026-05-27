# Find two indices whose elements add up to the target
# nums = [2,7,11,15]
# target = 9
# Output: [0,1] 


    
# def two_sum(nums, target):
#     hashmap = {}
    

#     for i in range(len(nums)):
#         complement = target - nums[i]

#         if complement in hashmap:
#             return [hashmap[complement], i]

#         hashmap[nums[i]] = i

# nums = [2,7,11,15]
# target = 9

# print(two_sum(nums, target))



# nums = [2,11,7,15]
# target = 9
# Output: [0,2]

def sum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] + num[j] == target:
                return[i,j]

num = [2,11,7,15]
target = 9
print(sum(num,target)) 