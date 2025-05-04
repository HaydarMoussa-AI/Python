def min(A, start, end):
    if start == end:
        return A[start]
    middle = (start + end) // 2
    U = min(A, start, middle)
    V = min(A, middle + 1 , end)
    if(U > V):
        return V 
    else:
        return U

A = [1,2,3,4,5]
print("The min is :) :",min(A, 0, len(A) - 1))