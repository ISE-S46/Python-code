ref = 2+2+2+1+6+1+0+0+7+0
def check(fx,gx,hx):
    if hx < (fx/gx):
        cond = (fx/gx) + hx
    elif hx >= (fx/gx):
        cond = ((fx-1)*hx)/gx
    if str(ref) in str(cond):
        z.append(cond)
    else :
        pass
    print(str(ref) in str(cond))
    breakpoint
def h(gx):
    if gx < 10:
        hx = 1.7246 * gx
    elif 20 <= gx < 35:
        hx = 1.3355/((gx/2.1425)+(1.1311*gx))
    else :
        hx = (7.142/(0.5412*gx))**(1/3)
    return hx
def g(fx):
    if fx < 5:
        gx = abs((2*fx)-17)
    elif 15 <= fx < 30:
        gx = abs(((1/13)*fx) -43)
    else :
        gx = (fx**1/2) - ((10/33)*fx)
    return gx
z = []
for x in range (-50,50,1):
    if x < 10:
        fx = x**2-5*x
    elif 10<=x<50:
        fx = (3*x+11)**1/2
    else:
        fx += (x**2 - 25)**1/3
    gx = g(fx)
    hx = h(gx)
    check(fx,gx,hx)
print(z)
if len(z) == 0 :
    print(ref)
elif len(z) == 1 :
    s = str(z)
    z2 = list()
    for i in s:
        if i.isdigit():
            z2.append(int(i))
    print(sum(z2))
elif len(z)>1 :
    print(sum(z)/len(z))