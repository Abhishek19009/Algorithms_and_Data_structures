input_string = "AABAAAABB"
pattern = "AAB"

# We will considering only letters and special symbols.
# In ASCII table there are 127 of them.
# Just use the ord to get ASCII values

pattern_hash = 0
window_hash = 0
temp_index = []

for i in range(len(pattern) - 1, -1, -1):
    pattern_hash += ord(pattern[i]) * (127 ** (len(pattern) - 1 - i))
    # First window hash
    window_hash += ord(input_string[i]) * (127 ** (len(pattern) - 1 - i))

for i in range(1, len(input_string) - len(pattern) + 1):
    if window_hash == pattern_hash:
        # print("Pattern found at position " + str(i-1))
        temp_index.append(i-1)
    window_hash = (window_hash - (ord(input_string[i - 1]) * (127 ** (len(pattern) - 1)))) * 127 + ord(
        input_string[i + (len(pattern) - 1)])
    if i == len(input_string) - len(pattern):
        if window_hash == pattern_hash:
            # print("Pattern found at position " + str(i-1))
            temp_index.append(i-1)


print(temp_index)
# temp_index contains indexes for input_string that matches the hash value of pattern
# One more step i.e checking for each hash value whether pattern is true can be done
# Since hashing might return same value for different strings.