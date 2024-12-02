list = input('Enter student names and grades: ')
dictionary = dict(subString.split(": ") for subString in list.split(", "))

grades = [*dictionary.values()]
names = [*dictionary.keys()]

for i in range(0,len(grades)):
    dictionary[names[i]] = int(grades[i])

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

