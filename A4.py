def check3(f,g,h,id,x,nt,n1):
    ncond = 0
    if h[0] < (float(f[0])/float(g[0])):
        cond = (f[0]/g[0]) + h[0]
        ncond =1
    elif h[0] >= (f[0]/g[0]):
        cond = ((f[0]-1)*h[0])/g[0]
        ncond =2
    if str(id) in str(cond):
        if nt<4:
            nt = nt+1
            form ='[{}] x = {} --> f(x) = {} --> g(f(x)) = {} --> h(g(f(x))) = {}'
            form2 = '--> conver(f, g, h) = {} --> Result = True'
            print(form.format(n1,x,f[0],g[0],h[0]))
            print(form2.format(cond))
    return nt
def check2(f,g,h,id,n2):
    if h < (f/g):
        cond = (f/g) + h
    elif h >= (f/g):
        cond = ((f-1)*h)/g
    if str(id) in str(cond):
        o.append(cond)
        n2 = n2+1
    else :
        pass
    return n2
def check(f,g,h,id,x,nt):
    ncond = 0
    if h[0] < (f[0]/g[0]):
        cond = (f[0]/g[0]) + h[0]
        ncond =1
    elif h[0] >= (f[0]/g[0]):
        cond = ((f[0]-1)*h[0])/g[0]
        ncond =2
    if str(id) in str(cond):
        if nt<4:
            nt = nt+1
            cor ='({},{})'
            print('Condition',f[1],'within f(x), the coordintate is',cor.format(x,f[0]))
            print('Condition',g[1],'within g(x), the coordintate is',cor.format(f[0],g[0]))
            print('Condition',h[1],'within h(x), the coordintate is',cor.format(g[0],h[0]))
            print('Condition',ncond,'within Convert function, the result is',cond)
            print('===========================================================================')   
    return nt
def h(g):
    nh = 0
    if g < 10:
        h = 1.7246*g
        nh =1
    elif 20 <= g < 35:
        h = 1.3355/((g/2.1425)+(1.1311*g))
        nh = 2
    else :
        h = (7.142/(0.5412*g))**(1/3)
        nh = 3
    hx = (h,nh)
    return hx
def g(f):
    ng=0
    if f < 5:
        g = abs((2*f)-17)
        ng =1
    elif 15 <= f < 30:
        g = abs(((1/13)*f) -43)
        ng =2
    else :
        g = (f**1/2) - ((10/33)*f)
        ng =3
    gx =(g,ng)
    return gx                  
o = []
a1 = 0
a2 = 100
id = 2+2+2+1+6+1+0+0+7+0
print('The starting value :',a1)
print('The ending value :',a2)
n1 = 0
n2 = 0
for n in range(a1,a2,1):
    n1 += 1
print('The amount of input :',n1)
print('===========================================================================')
print('student id : 2221610070 --> The reference value :',id)
print('===========================================================================')
for x in range (a1,a2,1):
    nf = 0
    if x < 10:
        f = x**2-5*x
        nf =1
    elif 10<=x<50:
        f = (3*x+11)**1/2
        nf =2
    else:
        f = (x**2-25)**1/3
        nf =3
    fx = (f,nf)
    gx = g(fx[0])
    hx = h(gx[0])
    n2 = check2(fx[0],gx[0],hx[0],id,n2)
print('The amount of True output :',n2)
if len(o) == 0:
    print('There is no True output;')
elif len(o) ==1:
    print('The only True output is shown below; ')
elif 1<len(o)<=4:
    print('The True output is shown below; ')
else:
    print('The first 4 of them are shown below;')
nt =0
n1 =0
for x in range (a1,a2,1):
    n1 = n1+1
    if x < 10:
        f = x**2-5*x
        nf =1
    elif 10<=x<50:
        f = (3*x+11)**1/2
        nf =2
    else:
        f = (x**2-25)**1/3
        nf =3
    fx =(f,nf)
    gx = g(fx[0])
    hx = h(gx[0])
    nt =check3(fx,gx,hx,id,x,nt,n1)
print('===========================================================================')
if len(o)>0:
    print('The log of the corresponding indexs are shown below;')
nt =0
for x in range (a1,a2,1):
    if x < 10:
        f = x**2-5*x
        nf =1
    elif 10<=x<50:
        f = (3*x+11)**1/2
        nf =2
    else:
        f = (x**2-25)**1/3
        nf =3
    fx =(f,nf)
    gx = g(fx[0])
    hx = h(gx[0])
    nt = check(fx,gx,hx,id,x,nt)
if len(o) == 0 :
    print('Get into the condition number 1, the final output of the model is',id)
elif len(o) == 1 :
    s = str(o)
    o2 = list()
    for i in s:
        if i.isdigit():
            o2.append(int(i))
    print('Get into the condition number 2, the final output of the model is',sum(o2))
elif len(o)>1 :
    print('Get into the condition number 3, the final output of the model is',sum(o)/len(o))
print('===========================================================================')