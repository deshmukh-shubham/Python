# Use a hashtable to filter out diplicate items
# Time complexity is: O(n)

# define a set of items that wqe want to reduce duplicate
items = ["apple","pear","orange","banana","apple","orange","apple",
         "pear","banana","orange","apple","kiwi","pear","apple","orange"]


# TODO: Create a hashtable to perform a filter
filter = dict()

# TODO: loop over each item and add to the hashtable
for key in items:
    filter[key] = 0

# TODO: create a set from resulting keys in the hashtable
result = set(filter.keys())
print(result)
