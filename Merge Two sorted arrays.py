A = [1,2,3,4,5]
B = [6,7,8,9,10]
C = [] 
i = J = 0
while i < len(A) and J < len(B):
    if A[i] < B[J]:
        C.append(A[i])
        i += 1 
    else:
        C.append(B[J])
        J += 1
# Append the remaining element to A
while(i<len(A)):
        C.append(A[i])
        i += 1 
# Append the remaining element to B
while(J<len(B)):
        C.append(B[J])
        J += 1 
        
print("After merging the two lists :) :", C)