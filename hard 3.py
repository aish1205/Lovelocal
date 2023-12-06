def countDigitOne(n):
    # Initialize the count of digit 1
    count = 0

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Convert the current number to a string
        num_str = str(i)

        # Count the number of occurrences of '1' in the string
        count += num_str.count('1')

    return count

# Example 1
n = 13
result = countDigitOne(n)
print(result)

# Example 2
n = 0
result = countDigitOne(n)
print(result)