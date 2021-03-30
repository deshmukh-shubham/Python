# Use a recursive algorithm to find a maximum value

# declare the list of values to operate on
items = [6, 28, 8, 19, 56, 23, 87, 41, 49, 53]

def find_max(items):
    # TODO: breaking condition: last item in the list? if yes return it
    if len(items) == 1:
        return items[0]

    # TODO: otherwise fet the first item and call the function
    # again to operate on the rest of the list
    op1 = items[0]
    op2 = find_max(items[1:])
    
    # TODO: perform the comparision when we are down to just two
    if op1 > op2:
        return op1
    else:
        return op2

# test the function
print(find_max(items))
