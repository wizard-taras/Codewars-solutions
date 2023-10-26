def to_alternating_case(string):
    res = ''
    for s in string:
        if s.isupper(): res += s.lower()
        elif s.islower(): res += s.upper()
        else: res += s
    return res