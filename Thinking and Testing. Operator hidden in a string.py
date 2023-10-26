import string
alphabet = string.ascii_lowercase
signs = ('+-*/'*7).removesuffix('*/')

def testit(s):
    if len(s) == 1: return (alphabet.find(s) + 1)
    elif len(s)%2 != 0:
        index = 1
        temp = str((alphabet.find(s[0]) + 1))
        while index != len(s)-1:
            operator = str(signs[alphabet.find(s[index])])
            temp += operator + str((alphabet.find(s[index+1]) + 1))
            if index == len(s)-2:
                return eval(temp)
            index += 2