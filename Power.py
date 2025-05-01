base = int(input("Please Enter the base number: "))
exponent = int(input("Please Enter the exponent: "))
result = 1
for _ in range(exponent):
    result *= base
print("The Value is equal to :) :", result)


