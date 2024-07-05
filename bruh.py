'''X = int(input())
Y = int(input())
Z = int(input())
n = int(input())
'''
'''xyz = [[i, j, k] for i in range(X+1)
                for j in range(Y+1)
                for k in range(Z+1) if i+j+k != n]'''
'''
xyz = []
for i in range(X+1):
    for j in range(Y+1):
        for k in range(Z+1):
            if i+j+k != n:
                xyz.append([i,j,k])
print(xyz)
'''
n = int(input())
a = map(int, input().split())
a = list(a)
sublist = [x for x in a if x < max(a)]
print(max(sublist))


