def solution(start, finish):  
    diff = finish - start
    rem_3 = diff%3 # remainder of division by 3
    full_3 = (diff - rem_3)/3 # number of full [i+3] jumps
    if rem_3 != 0: res = full_3 + rem_3 # if the remainder non zero
    else: res = full_3 

    return res