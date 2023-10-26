def repeat_str(repeat, string):
    ls = []
    [ls.append(string) for i in range(repeat)]
    return ''.join(ls)