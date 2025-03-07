# Example 14 - String indexing

credit_number = "1234-5678-9012-3456"

# Returns character at the first position
print(credit_number[0])
# Returns characters from the beginning to given index
print(credit_number[:4])
# Returns characters from one given index to another excluding last index character
print(credit_number[5:9])
# Returns characters from given index to the end
print(credit_number[5:])
# Returns the first character starting from the end
print(credit_number[-1])
# Returns characters occurring every given step [start : end : step]
# Negative step would start from the end of string
# In this case; from start to finish every second step
print(credit_number[::2])
