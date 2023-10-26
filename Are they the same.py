def comp(array1, array2):
    if array1 == None or array2 == None: return False
    arr1 = [i**2 for i in array1]
    arr1.sort()
    array2.sort()
    if arr1 != array2: return False
    return True