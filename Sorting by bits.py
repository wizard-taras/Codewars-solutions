def sort_by_bit(arr):
    
    master_list = []
    for num in arr:
        
        # This internal script takes a number and converts it to its binary equivalent in list form
        bin_str = ''
        q = num//2
        rem = num%2
        bin_str += str(rem)
        while q != 0:
            rem = q%2
            bin_str += str(rem)
            q = q//2
            
        master_list.append([num, bin_str.count('1')]) # populate a list with pair of integer and the number of its 'on' bits ('1's)
    
    # Using bubble sort algorithm to sort the master list based on its 2nd element of each pair - i.e. the number of integer 'on' bits
    for i in range(len(master_list)-1):
        for ii in range(len(master_list)-1):
            if master_list[ii][1] > master_list[ii+1][1]:
                tmp = master_list[ii+1]
                master_list[ii+1] = master_list[ii]
                master_list[ii] = tmp
                
                # This section of conditional modifies original array 'arr' --> an in-place sorting is performed
                tmp = arr[ii+1]
                arr[ii+1] = arr[ii]
                arr[ii] = tmp
            elif master_list[ii][1] == master_list[ii+1][1]:
                if master_list[ii][0] > master_list[ii+1][0]:
                    tmp = master_list[ii+1]
                    master_list[ii+1] = master_list[ii]
                    master_list[ii] = tmp
                    
                    # This section of conditional modifies original array 'arr' --> an in-place sorting is performed
                    tmp = arr[ii+1]
                    arr[ii+1] = arr[ii]
                    arr[ii] = tmp