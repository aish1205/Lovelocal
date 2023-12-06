def length_of_last_word(s):
    return len(s.strip().split()[-1])
  
# Example 1
s = "Hello World"
last_word_length = length_of_last_word(s)
print(last_word_length)  # Output: 5

# Example 2
s = "   fly me   to   the moon  "
last_word_length = length_of_last_word(s)
print(last_word_length)  # Output: 4

# Example 3
s = "luffy is still joyboy"
last_word_length = length_of_last_word(s)
print(last_word_length)  # Output: 6
