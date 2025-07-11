for i in range(5, 0, -1):       # i goes from 5 to 1 (decreasing)
    for j in range(1, i + 1):   # print i stars in the i-th row
        print("*", end="")
    print()                     # move to next line
