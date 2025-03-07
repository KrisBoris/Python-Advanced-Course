# Example 13 - string methods

name = input("Enter your name: ")

# Returns length including white spaces
print(len(name))
# Returns index of the first occurrence of the given character or -1 if absent
print(name.find("Kok"))
# Returns index of the last occurrence of the given character or -1 if absent
print(name.rfind("K"))
# Capitalizes the first letter of the string (doesn't modify the original)
print(name.capitalize())
# Changes all letters to lowercase
print(name.lower())
# Changes all letters to uppercase
print(name.upper())
# Returns true if string contains only digits (white spaces not allowed)
print(name.isdigit())
# Returns true if string contains only alphabetical characters (white spaces not allowed)
print(name.isalpha())
# Returns the number of given character occurrences
print(name.count(" "))
# Replaces first character with second character
print(name.replace(" ", "-"))
# Prints list of all class methods
#print(help(str))
