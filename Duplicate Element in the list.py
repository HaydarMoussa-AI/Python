A = [10, 20, 30, 40, 50]
N = len(A)
# Extend list to double it's size
A.extend([0]*N)
print("After extending List A :) :",A)
# start stop step
for i in range(N-1, -1, -1):
    A[2 * i] = A[i]
    A[2 * i + 1] = A[i]
print("After Duplicating Elements in the list :) :",A)

    
    
