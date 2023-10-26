def find_uniq(arr):
    uniq = set(arr)
    uniq_list = []
    
    for i in uniq:
        uniq_list.append(i)
        
    if arr.count(uniq_list[0]) == 1:
        return uniq_list[0]
    return uniq_list[1]