from sys import maxsize

def max_sequence(arr):

    def isnegative(arr_to_check):
        # This script checks whether the given array consists fully of
        # negative numbers

        # Returns False if there's at least 1 posivite number and
        # True if there're only negative ones
        flag = True
        for el in arr_to_check:
            if el*(-1) != abs(el):
                flag = False
        return flag
    
    # Main body
    if arr == [] or isnegative(arr) == True:
        return 0
    else:
        size = len(arr)
        max_so_far = -maxsize - 1
        max_ending_here = 0

        for i in range(0, size):
            max_ending_here = max_ending_here + arr[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far