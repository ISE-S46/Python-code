print(" *** Maximum occurence ***")
input_str = input("Enter numbers : ")
nums = [int(num) for num in input_str.split()]

# Extract the numbers before the "-1" delimiter
arrSort = []
for num in nums:
    if num == -1:
        break
    arrSort.append(num)

# Sort the extracted numbers
arrSort.sort()
print(arrSort)

# Count the occurrences of each number and find the maximum count
max_count = 0
num_counts = {}
for num in arrSort:
    if num in num_counts:
        num_counts[num] += 1
    else:
        num_counts[num] = 1
    if num_counts[num] > max_count:
        max_count = num_counts[num]

# Find the numbers with the maximum count
max_nums = []
for num in num_counts:
    if num_counts[num] == max_count:
        max_nums.append(num)

print('Count:', max_count)
print('Max occurence:', max_nums)
print("===== End of program =====")