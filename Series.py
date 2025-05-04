def m(i):
    # base case
    if i == 0:
        return 0
    # recurrence relation
    return i / ( 2 * i + 1) + m(i - 1)

for i in range(30):
   print(m(i))