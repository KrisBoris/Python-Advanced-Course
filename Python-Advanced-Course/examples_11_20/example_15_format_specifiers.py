# Example 15 - format specifiers
# Format a value based on what flags are inserted

price = 3129.2965

# Set number of decimals
print(f"{price:.2f}")
# Set space reserved to display number
print(f"{price:10}")
# Add zero at the beginning to precede number with zeros
print(f"{price:010}")
# Left justify (align)
print(f"{price:<10}")
# Right justify (align)
print(f"{price:>10}")
# Center number
print(f"{price:^10}")
# Show plus sign for positive numbers
print(f"{price:+10}")
# Leave empty space in place of plus sign for positive numbers
print(f"{price: 10}")
# A thousand separator
print(f"{price:,}")
