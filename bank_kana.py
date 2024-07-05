import random
def max(n_s):
    vmin = n_s[0]
    dmax = 0
    for i in range(len(n_s)):
        if(n_s[i]<vmin):
            vmin = n_s[i]
        elif(n_s[i]-vmin>dmax):
            dmax = n_s[i]-vmin
    return dmax
n_s = []
max_diff = []
for j in range(0,10000):
    for i in range(0,20):
        n = random.randint(1,365)
        n_s.append(n)
    max_diff.append(max(n_s))
    n_s = []
print("Probability: ",sum(max_diff)/len(max_diff))