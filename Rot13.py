import string

def rot13(message):
    alph_upper = string.ascii_uppercase

    final = ''

    for s in message:
        if s.upper() in alph_upper:
            if s.lower() < 'n':
                if s.isupper():
                    final += alph_upper[alph_upper.find(s) + 13]
                else: final += alph_upper.lower()[alph_upper.lower().find(s) + 13]
            else:
                if s.isupper():
                    final += alph_upper[alph_upper.find(s) - 13]
                else: final += alph_upper.lower()[alph_upper.lower().find(s) - 13]
        else: final += s
    
    return final