def count_deaf_rats(pattern):
    splitted = pattern.replace(' ', '').split('P')
    deaf_rats = 0
    for i in splitted[0][::2]:
        if i == 'O': deaf_rats += 1
    for i in splitted[1][::2]:
        if i == '~': deaf_rats += 1

    return deaf_rats