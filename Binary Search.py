A = [1,2,3,4,5]
# define a Function 
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    #looping 
    while left <= right:
        middle = (left + right) // 2
        # if the middle it's the target
        if arr[middle] == target :
            # return the index
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle -1 
    # Target was not found
    return -1      
print(binary_search(A, 5))
    
