def transpose(inp_mat):
    out_mat = []
    temp_el = 0
    temp_arr = []

    for itr in range(len(inp_mat[0])):
        for i in inp_mat:
            temp_el = i[itr]
            temp_arr.append(temp_el)
        out_mat.append(temp_arr.copy())
        temp_arr.clear()
    
    return out_mat