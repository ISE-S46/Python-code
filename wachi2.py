print("*** greeting ***")
list = input("Enter some names : ").split()
print(list)
a = len(list)
for i in range(0,a,1):
    print("hello",list[i])
