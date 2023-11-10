def evenodd(num):
    if num%2 == 0: return 'even'
    if num%2 == 1: return 'odd'

def sum_groups(arr):
    len_in = 0
    len_out = len(arr) - 2
    i = 0
    flag = True
    i_decr = 0
    s = 0
    temp_arr = []

    while len_in != len_out:
        len_in = len(arr)
        while i <= len(arr)-2:
            temp_arr.append(arr[i])
            while flag == True:
                if evenodd(arr[i+1]) == evenodd(arr[i]):
                    temp_arr.append(arr[i+1])
                    i_decr += 1
                    i += 1
                    if i == len(arr)-1:
                        s = sum(temp_arr)
                        i -= i_decr
                        arr.insert(i, s)
                        arr[(i+1):(i+2)+i_decr] = []

                        break
                else:
                    flag = False
                    s = sum(temp_arr)
                    i -= i_decr
                    arr.insert(i, s)
                    arr[(i+1):(i+2)+i_decr] = []
            temp_arr.clear()
            s = 0
            i_decr = 0
            i += 1
            flag = True
        i = 0
        len_out = len(arr)

    return len(arr)