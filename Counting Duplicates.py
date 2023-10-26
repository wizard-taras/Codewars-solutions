def duplicate_count(text):
    occurs = 0
    text = text.lower()
    for s in text:
        if text.count(s) > 1:
            occurs += 1
            text = text.replace(s, '')
    return occurs