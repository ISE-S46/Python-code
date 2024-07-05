print("*** Odd/Even at left/Right ***")
E = input("Enter numbers: ")
Bing = [int(num) for num in E.split()]
odd = []
even = []
for i in range(len(Bing)):
    if(Bing[i] % 2 == 0):
        even.append(Bing[i])
    else:
        odd.append(Bing[i])
chiling = odd + even
chiling2 = odd[::-1] + even
print("odd = ", odd)
print("even = ", even)
print("odd+even = ", chiling)
print("new = ", chiling2)
