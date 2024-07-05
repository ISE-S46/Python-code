val = [6,42,34,21,56]
lowest_number = min(val)
second_lowest = float('inf')
for n in val:
    print(n)
for n in val:
    if n != lowest_number and n < second_lowest:
        second_lowest = n
print(second_lowest)
