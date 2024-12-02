list = input('Enter student names and grades: ')
dictionary = dict(subString.split(": ") for subString in list.split(", "))

grades = [*dictionary.values()]
print(grades)
print(len(grades))

for name in dictionary:
    for i in range(0,len(grades)):
        print(i)
        dictionary[name] = int(grades[i])
print(dictionary)

for k, v in dictionary.items():
    print(k, v)

'''
gradestr = [*dictionary.values()]
grade = []

for i in range(0,len(gradestr),1):
    grade.append(int(gradestr[i]))

AverageGrade = sum(grade)/len(grade)
HighestGrade = max(grade)
LowestGrade = min(grade)

print(f'Average grade: {AverageGrade}')
print(AverageGrade)
print(HighestGrade)
print(LowestGrade)
'''

