# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index       
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i+1,len(arr)):    
            if arr[x]<arr[smallest_index]:
                smallest_index = x
        # TO-DO: swap
        if smallest_index != i:
            arr[i],arr[smallest_index]=arr[smallest_index],arr[i]
    return arr
# print(selection_sort([3,4,1,5,6,6,4,3,2,8,0,9,8]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    sort=False
    while not sort:
        sort=True
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i] 
                sort=False
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

