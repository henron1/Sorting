# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        smallest = min(arr[i:])
        smallest_index = arr.index(smallest)
        if arr[smallest_index] < arr[cur_index]:
            arr[cur_index] = arr[smallest_index]


        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # loop through array, find smallest value
        # for j in range(i + 1, len(arr) - 1):
        #     if arr[j] < arr[cur_index]:
        #         j = cur_index

                

            # smallest = min(arr[j:])
            # index = arr.index(smallest)
            # if smallest < arr[i]:
            #     arr[i] = smallest
            #     arr[index] = arr[i]
                
        # move smallest value to beginning of array
        # swap OG first element to smallest value's OG place
        # loop through array, starting 1 index in
        
        # min_array = min(arr[i:len(arr) - 1])
        # min_index = arr.index(min_array)
        
        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr