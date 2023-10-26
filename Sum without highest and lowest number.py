def sum_array(arr):
    if arr is not None and len(arr) > 1: return sum(arr) - sum([max(arr), min(arr)])
    else: return 0