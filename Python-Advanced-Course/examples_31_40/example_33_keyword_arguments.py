# Example 32 - Keyword arguments

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


# Place position arguments before keyword arguments (4 for country should be at the beginning)
# phone_num = get_phone(area=123, first=456, last=7890, 4)
phone_num = get_phone(country=4, area=123, first=456, last=7890)

print(phone_num)