# TO-DO: complete the helpe function below to merge 2 sorted arrays
alpha = [1,2,3,4,5]
beta = [5,6,7,8,9]
def merge( arrA, arrB ):
    merged_arr = []
    # TO-DO
    x = 0
    y = 0
    while x < len( arrA )  and y < len( arrB ):
        if arrA[x] < arrB[y]:
            merged_arr.append(arrA[x])
            x += 1
        else:
            merged_arr.append(arrB[y])
            y += 1
    
    return merged_arr

print(merge(alpha, beta))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
