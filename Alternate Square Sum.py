def alternate_sq_sum(arr):
    list_odd = arr[::2]
    list_even = arr[1::2]
    sum_odd = 0
    sum_even = 0

    for i in list_odd:
        sum_odd += i
    for i in list_even:
        sq = i**2
        sum_even += sq
    return (sum_odd + sum_even)