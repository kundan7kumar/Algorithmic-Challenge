# For Loop Method
def ContainsDuplicate(nums):
    nums.sort()
    for i in range(0, len(nums)):
        if len(nums) < 1:
            return False
        if nums[i] == nums[i + 1]:
            return True
    return False


# Check len
def ContainsDuplicate1(nums):
    A = list(set(nums))

    if len(nums) != len(A):
        return True


# Using Hashing
def ContainsDuplicate2(nums):

    A = {}
    for num in nums:
        if num not in A:
            A[num] = 1
        else:
            A[num] += 1
        print(A)
    for key, value in A.items():
        if value > 1:
            return True
    return False

def ContainsDuplicate3(nums):
    if len(nums) ==0:
        return False

    nums.sort()

    curr = nums[0]
    for i in range(1,len(nums)):
        if nums[i]^curr==0:
            return True
        curr=nums[i]
    return False


nums = [2, 1, 3, 22, 22]

print(ContainsDuplicate(nums))
print(ContainsDuplicate1(nums))
print(ContainsDuplicate2(nums))
print(ContainsDuplicate3(nums))