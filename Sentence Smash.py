def smash(words):
    str = ''
    for s in words:
        str += s.strip() + ' '
    return str.rstrip()   