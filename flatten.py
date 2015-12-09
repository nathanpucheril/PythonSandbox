#Flattens list by one level, no mutation
def flatten(lst):
    new_lst = []
    for item in lst:
        if type(item) == type(lst):
            for elem in item:
                new_lst.append(elem)
        else:
            new_lst.append(item)
    return new_lst

#Flattens list by all levels, no mutation
def deep_flatten_comprehension(lst):
    lstref = []
    if type(lst) == type(lstref):
        return [item for element in lst for item in flatten2(element)]
    return [lst]

#Flattens list by levels specified or all if no specification, no mutation
def deep_flatten(lst, depth = -1):
    new_lst = []
    for item in lst:
        if type(item) == type(lst) and (depth > 0 or depth < 0):
            item = deep_flatten(item, depth - 1)
            for elem in item:
                new_lst.append(elem)
        else:
            new_lst.append(item)
    return new_lst
L = [[[1, 2, 3], [4, 5]], 6]
print(flatten2(L))
