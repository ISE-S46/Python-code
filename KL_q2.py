import numpy as np
from scipy.special import  rel_entr
from math import log2,sqrt
import matplotlib.pyplot as plt    

prod = ['car','credit card','debt collection', 'house', 'medical', 'wedding', 'vacation', 'moving', 'tax payment']

p = [10,5,8,12,12,9,23,9,12]
q = [9,10,9,13,11,21,8,10]

print("Sum of q",sum(q))

#let e as small constant for smoothing
e = 1
q.append(e)

for i in range(len(q)):
    q[i] = q[i] - (e/len(q))
for i in range(len(q)):
    p[i] = p[i] - (e/len(q))

print(q)
print("Fill ACTUAL (q) using smoothing method by appending a small value",e, ", then subtract every single value in the array by ",e)
print("Also, smooth ")
print("Sum of q after smoothing",sum(q))
print()
print("Kullback-Leibler Divergence")

def kl_divergence(p,q):
    x = sum(p[i] * log2(p[i]/q[i]) for i in range(len(p)))
    return x
kl_pq = kl_divergence(p,q)
kl_qp = kl_divergence(q,p)
print("KL(P||Q) divergence: %.3f bits" % kl_pq)
print("KL(P||Q) distance: %.3f nats" % sum(rel_entr(p,q)))
print("KL(Q||P) divergence: %.3f bits" % kl_qp)
print("KL(Q||P) distance: %.3f nats" % sum(rel_entr(q,p)))
print("KL(Q||P) and KL(P||Q) do not have the same value, KL Divergence is not symmetric")

#check symmetry between qp and pq divergences in each type
#given that JS divergence is symmetric, while KL divergence is not.

def symmetry_check(a,b):
    if a == b:
        return True
    elif a != b:
        return False

print("Symmetry: ", symmetry_check(kl_pq,kl_qp))
print()
p = np.array(p)
q = np.array(q)

#JS divergence
def js_divergence(p,q):
    m = 0.5 * (p + q)
    n = 0.5 * kl_divergence(p, m) + 0.5 * kl_divergence(q,m)
    return n
js_pq = js_divergence(p, q)
js_qp = js_divergence(q, p)
print("Jensen-Shannon Divergence")
print("JS(P||Q) divergence: %.3f bits" % js_pq)
print("JS(P||Q) distance: %.3f" % sqrt(js_pq))
print("JS(P||Q) divergence: %.3f bits" % js_qp)
print("JS(Q||P) distance: %.3f" % sqrt(js_qp))
print("Symmetry: ", symmetry_check(js_pq,js_qp))
print()
print("JS(Q||P) and JS(P||Q) have the same value, JS Divergence is symmetric")

plt.subplot(2,1,1)
plt.bar(prod,p,color = 'green')
plt.xticks(range(len(prod)), prod, rotation='vertical')

plt.subplot(2,1,2)
plt.bar(prod,q)
plt.xticks(range(len(prod)), prod, rotation='vertical')

plt.subplots_adjust(hspace=1.5)  # adjust the spacing

plt.show()