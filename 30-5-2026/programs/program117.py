def next_in_line(lst, num):
    if lst:
        lst.pop(0)
        lst.append(num)
        return lst
    else:
        return "No list has been selected"
