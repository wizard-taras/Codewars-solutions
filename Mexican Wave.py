import string
alph = string.ascii_lowercase

def wave(input):
    input_lst = list(input)
    final_lst = []
    temp = input_lst.copy()
    for i in range(0, len(input_lst)):
        if input_lst[i] in alph:
            temp[i] = input_lst[i].upper()
            final_lst.append(''.join(temp))
        temp = input_lst.copy()
    return final_lst