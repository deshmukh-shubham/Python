# Linear search
# Unorderd list

items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]

def find_item(item, itemlist):
    for i in range(0, len(items)):
        if item == itemlist[i]:
            return i

    return None   

print(find_item(87, items))
print(find_item(250, items))
