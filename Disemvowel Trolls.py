def disemvowel(string_):
    for i in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']:
        string_ = string_.replace(i, '')
    return string_