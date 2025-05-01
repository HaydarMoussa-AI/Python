A = [5, 4, 3, 2, 1]
N = len(A)
# Outer loop
for i in range(N):
    # inner loop
    for J in range(0, N - i - 1):
        if A[J] > A[J+1]:
            # swapping 
            temp = A[J]
            A[J] = A[J+1]
            A[J+1] = temp
print("After Sorting the List :) :",A)
        