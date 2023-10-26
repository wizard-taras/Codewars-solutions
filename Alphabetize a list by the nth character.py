def sort_it(words: str, n: int) -> str:
    lst = [s.strip() for s in words.split(',')]
    for i in range(len(lst)-1):
        for j in range(len(lst) - 1 - i):
            if lst[j][n-1] > lst[j+1][n-1]:
                lst[j], lst[j+1] =  lst[j+1], lst[j]
    
    return ', '.join(lst).removesuffix(', ')