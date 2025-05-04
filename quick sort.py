def partition(A, P, r):
    x = A[r]  # r is the pivot
    i = P - 1
    for j in range(P, r):  # it reaches r - 1
        if A[j] <= x:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = temp
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

# Example usage
A = [10, 7, 8, 9, 1, 5]
quicksort(A, 0, len(A) - 1)
print("Sorted array :) :", A)
