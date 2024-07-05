print("*** Alphabet Sequence (A-Z) ***")
list = input("Enter character step length : ").split()
a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
b = int(list[1])
X = []
if(b==0):
    Y = 1
else:
    Y = b
if(b>1):
    c = int(list[2])*Y
else:
    c = int(list[2])
if(list[0]=="A"):
    if(b!=0):
        for i in range(0,c,Y):
            if(i>124 and i<= 149):
                print(a[i-130],end="=")
            if(i>99 and i<= 124):
                print(a[i-104],end="=")
            if(i>74 and i<=99):
                print(a[i-78],end="=")
            if(i>49 and i<=74):
                print(a[i-52],end="=")
            if(i>=26 and i<=49):
                print(a[i-26],end="=")
            if(i<=26-1):
                print(a[i],end="=")
    else:
        for j in range(0,c,Y):
            print(a[0],end="=")
    print()
else:
    print("Invalid input !!!")
print("===== End of Program =====")