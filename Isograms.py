def is_isogram(string):
    lst = list(string.lower())
    for i in range(len(lst)-1, -1, -1):
        if lst.pop(i) in lst:
            return False
    return True