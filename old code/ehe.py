name = []
score = []
for i in range(int(input())):
    n = input()
    name.append(n)
    s = float(input())
    score.append(s)
res = {name[i]: score[i] for i in range(len(name))}
val = list(res.values())
val.sort()
lowest_number = min(val)
second_lowest = min(n for n in val if n != lowest_number)
name2 = []
for key in res:
    if(res[key] == second_lowest):
        name2.append(key)
sn = sorted(name2)
for j in range(len(sn)):
    print(sn[j])

