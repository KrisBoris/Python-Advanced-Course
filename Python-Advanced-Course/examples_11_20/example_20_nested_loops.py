# Example 19 - Nested loops

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol to fill rectangle with: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
