def generate_hashtag(s):
    lst = []
    if len(s) != 0:
        lst = s.split(' ')
        result = [i.lower().title() for i in lst if i != ' ']
        result = '#' + ''.join(result)
        if len(result) <= 140:
            return result
    return False