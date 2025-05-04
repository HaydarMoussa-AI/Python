def max(A, start, end):
    if start == end:
        return A[start]
    middle = (start + end) // 2
    U = max(A, start, middle)
    V = max(A, middle + 1 , end)
    if(U > V):
        return U 
    else:
        return V

A = [1,2,3,4,5]
print("The max is :) :",max(A, 0, len(A) - 1))