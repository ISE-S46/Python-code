number = int(input('Input number: '))
if(number < 1):
    print("Please enter a number greater than 0.")
for i in range(1,(number+1)):
    if(i%2)==0:
        print(i)