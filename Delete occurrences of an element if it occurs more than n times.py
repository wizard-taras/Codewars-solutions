def delete_nth(lst, limit):
    for i in lst:
        while lst.count(i) > limit:
            lst.reverse()
            lst.remove(i)
            lst.reverse()
    return lst