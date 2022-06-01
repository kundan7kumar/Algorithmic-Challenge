def test(nums):
    # Convert list into dictionary then check if there are more than "two" in values of dictionary.
    # T: O(N)
    # S: O(N)

    d = {}

    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    for k, v in d.items():
        if v >= 2:
            return True

    return False

print(test([2, 1, 3, 22, 22]))