n=int(input("Enter an integer(n) : "))
for i in range(1,13):
    if (i*n <= 9 and i <= 9):
        print("{} x {}  =   {}".format(n,i,i*n))
    elif(i*n <= 9 and i >= 10):
        print("{} x {} =  {}".format(n,i,i*n))
    elif(i*n >= 10 and i*n <= 99 and i <= 9):
        print("{} x {}  =  {}".format(n,i,i*n))
    elif(i*n >= 10 and i*n <= 99 and i >= 10):
        print("{} x {} =  {}".format(n,i,i*n))
    elif(i*n >= 100 and i <= 9):
        print("{} x {}  = {}".format(n,i,i*n))
    elif(i*n >= 100 and i >= 10):
        print("{} x {} = {}".format(n,i,i*n))