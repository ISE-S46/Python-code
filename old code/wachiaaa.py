print("*** Shopping List ***")
list_shopping = ["egg", "ham", "water", "soda"]
shopping = input("Enter some pairs of (operation, item):").split(",")
for pair in shopping :
    x = pair[0]
    item = pair[2:].strip()
    if x=='a':
        if item in list_shopping:
            continue
        else:
            list_shopping.append(item.lower())
    elif x=='r':
        try:
            list_shopping.remove(item.lower())
        except:
            continue
    else:
        print("Operation not supported!")
        exit()
print("Final shopping list is", list_shopping)