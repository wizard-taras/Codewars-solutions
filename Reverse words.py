def reverse_words(text):
    spl = text.split()
    rev = []
    for i in spl:
        i = list(i)
        i.reverse()
        rev.append(''.join(i))
    rev = ''.join(rev)
    ltext = list(text)
    i = 0
    spcs = []
    for j in ltext:
        if j == ' ':
            spcs.append(i)
        i = i + 1
    ls = list(rev)
    for i in spcs: ls.insert(i, ' ')
    return ''.join(ls)