x = int(input("Enter an integer(n) : "))
if(x<10):
    for i in range(1,13,1):
        txt = "{} x {}{}={}{}"
        a = " "
        b = a*2
        c = a*3
        y = x*i
        if(10>y):
            print(txt.format(x,i,b,b,y))
        elif(i<10):
            print(txt.format(x,i,b,a,y))
        else:
            print(txt.format(x,i,a,a,y)) 
else:
    for i in range(1,13,1):
        txt = "{} x {}{}={}{}"
        a = " "
        b = a*2
        c = a*3
        y = x*i
        if (y <= 9 and i <= 9):
            print(txt.format(x,i,b,c,y))
        elif(y <= 9 and i >= 10):
            print(txt.format(x,i,a,b,y))
        elif(y >= 10 and y <= 99 and i <= 9):
            print(txt.format(x,i,b,b,y))
        elif(y >= 10 and y <= 99 and i >= 10):
            print(txt.format(x,i,a,b,y))
        elif(y >= 100 and i <= 9):
            print(txt.format(x,i,b,a,y))
        elif(y >= 100 and i >= 10):
            print(txt.format(x,i,a,a,y))
