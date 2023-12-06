def countDigitOne(n):
  
    count = 0

   
    for i in range(1, n + 1):
        num_str = str(i)

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
