import string
ALPHABET = list(string.ascii_lowercase)
def is_pangram(strng):
    strng = strng.lower()
    unique = []
    for s in strng:
        if s in ALPHABET and s not in unique:
            unique.append(s)
    unique.sort()
    
    if unique == ALPHABET:
        return True
    return False