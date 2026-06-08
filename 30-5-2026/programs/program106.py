def move_to_end(lst, element):
    count = lst.count(element)
    lst = [x for x in lst if x != element]
    lst.extend([element] * count)
    return lst
