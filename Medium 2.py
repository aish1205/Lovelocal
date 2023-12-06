def majorityElement(nums):
    n = len(nums)
    threshold = n // 3
    candidates = []
    counts = {}

    for num in nums:
        if num not in counts:
            counts[num] = 0

        counts[num] += 1

        if counts[num] > threshold and num not in candidates:
            candidates.append(num)

    return candidates

# Example 1
nums = [3, 2, 3]
result = majorityElement(nums)
print(result)

# Example 2
nums = [1]
result = majorityElement(nums)
print(result)

# Example 3
nums = [1,2]
result = majorityElement(nums)
print(result)