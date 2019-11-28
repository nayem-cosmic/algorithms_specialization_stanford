#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:11:48 2019

@author: cosmic
"""

def inversions(array):
    n = len(array)
    
    if n == 1:
        return array, 0
    
    n_2 = int(n/2)
    larray = array[:n_2]
    rarray = array[n_2:]
    
    larray_sorted, invl = inversions(larray)
    rarray_sorted, invr = inversions(rarray)
    
    nl = len(larray_sorted)
    nr = len(rarray_sorted)
    
    array_sorted = []
    invn = invl + invr  # inversion number
    i = 0
    j = 0
    while i<nl and j<nr:
        if larray_sorted[i] <= rarray_sorted[j]:
            array_sorted.append(larray_sorted[i])
            i += 1
        else:
            array_sorted.append(rarray_sorted[j])
            j += 1
            invn += nl - i
    
    while i < nl:
        array_sorted.append(larray_sorted[i])
        i += 1
    
    while j < nr:
        array_sorted.append(rarray_sorted[j])
        j += 1
    
    return array_sorted, invn


array = [1, 3, 5, 2, 4, 7, 6]
print(inversions(array))