# Use a hashtable to count individual items
# Time complexity is: O(n)

# define a set of items that wqe want to reduce duplicate
items = ["apple","pear","orange","banana","apple","orange","apple",
         "pear","banana","orange","apple","kiwi","pear","apple","orange"]


# TODO: Create a hashtable object to hold the items and counts
counter = dict()

# TODO: Iterae over each item and increment the count for each one
for item in items:
    if(item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1
        
# print the results
print(counter)
