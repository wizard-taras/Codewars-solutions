def number(lines):
    output = []
    index = 1
    for s in lines:
        output.append(f'{index}: {s}')
        index += 1
    return output