# Find two indices whose elements add up to the target
# nums = [2,7,11,15]
# target = 9
# Output: [0,1] 


    
def two_sum(nums, target):
    hashmap = {}
    '''initializes an empty associative array. This data structure stores data in key-value pairs, allowing you to quickly insert, retrieve, and delete values based on their unique keys.'''

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[nums[i]] = i

nums = [2,7,11,15]
target = 9

print(two_sum(nums, target))

