# Example 25 - Dictionaries

capitals = {"USA": "Washington D.C.", "Poland": "Warsaw",
             "China": "Beijing", "Germany": "Berlin"}

# Get value associated with given key -> returns value or None if it doesn't exists
capitals.get("USA")
# Update existing value or insert a new one
capitals.update({"France": "Paris"})
# Pop existing item
capitals.pop("China")
# Pop the last item
capitals.popitem()
# Delete all items
# capitals.clear()

# Get all keys
keys = capitals.keys()
# Ge tall values
values = capitals.values()
# Get all key-value pairs
items = capitals.items()
for key, value in items:
    print(f"{key}: {value}")
