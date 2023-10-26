def xo(s):
    o_count = 0
    x_count = 0
    l = []
    for i in s: l.append(i)
    for ch in l:
        if ch.lower() == 'o': o_count += 1
        elif ch.lower() == 'x': x_count += 1
    if x_count != o_count: return False
    else: return True