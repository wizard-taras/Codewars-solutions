def open_or_senior(data):
    res = []
    [res.append('Senior') if i[0] >= 55 and i[1] > 7 else res.append('Open') for i in data]
    return res