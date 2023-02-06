print('  Alphabet Sequence (A-Z) ')
x,y,z = input('Enter character step length : ').split()
x = ord(x)
y=int(y)
z=int(z) - 1
if 91 > x > 64 and y >= 0:
    x = x - int(y) 
    while z >= 0 :
        if z == 0 :
            x = int(x) + int(y)
            if x >= 91 :
                x = x - 26
            x = chr(x)
            print(x)
        elif z >= 0 :
            x = int(x) + int(y)
            if x >= 91 :
                x = x - 26
            x = chr(x)
            print(f"{x}",end="=")
            x = ord(x)
        z = z - 1
else :
    print("Invalid input !!!")
print("===== End of program =====")