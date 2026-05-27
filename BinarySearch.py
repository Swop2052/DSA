# i/p  nums = [1,2,3,4,5], target = 4
# o/p = 3

def binary_search(nums,target):

    left = 0
    right = len(nums)-1

    while left <= right:

        mid = (left+right)//2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid+1

        else:
            right = mid-1

    return -1

print(binary_search([1,2,3,4,5],4))