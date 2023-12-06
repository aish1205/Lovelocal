def generate(numRows):
    if numRows == 1:
        return [[1]]

    pascal = generate(numRows - 1)
    last_row = pascal[-1]
    new_row = [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)]
    new_row.insert(0, 1)
    new_row.append(1)
    pascal.append(new_row)
    return pascal

# Example 1
numRows = 5
pascal = generate(numRows)
print(pascal)

# Example 2
numRows = 1
pascal = generate(numRows)
print(pascal)
