def merge_sort(array):
    n = len(array)
    
    if n == 1:
        return array
    
    n_2 = int(n/2)
    larray = array[:n_2]
    rarray = array[n_2:]
    
    larray_sorted = merge_sort(larray)
    rarray_sorted = merge_sort(rarray)
    
    nl = len(larray_sorted)
    nr = len(rarray_sorted)
    
    array_sorted = []
    i = 0
    j = 0
    while i<nl and j<nr:
        if larray_sorted[i] <= rarray_sorted[j]:
            array_sorted.append(larray_sorted[i])
            i += 1
        else:
            array_sorted.append(rarray_sorted[j])
            j += 1
    
    while i < nl:
        array_sorted.append(larray_sorted[i])
        i += 1
    
    while j < nr:
        array_sorted.append(rarray_sorted[j])
        j += 1
    
    return array_sorted


if __name__ == '__main__':
    ar = [2, 3, 1, 5, 4]
    print(merge_sort(ar))