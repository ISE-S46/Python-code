class A:
    def __init__(self,a1,a2,id):
        self.a1 = a1
        self.a2 = a2
        self.id = id
    def idk(self,n1):
        for n in range(self.a1,self.a2,1):
            n1 += 1
        return n1
    def g(f):
        if f < 5:
            g = abs((2*f)-17)
            ng =1
        elif 15 <= f < 30:
            g = abs(((1/13)*f) -43)
            ng =2
        else :
            g = (f**1/2) - ((10/33)*f)
            ng =3
        gx = (g,ng)
        return gx
    def h(g):
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
class B :
    def __init__(self):
        self
    def check(fx,gx,hx,id):
        if hx < (float(fx)/float(gx)):
            cond = (fx/gx) + hx
        elif hx >= (fx/gx):
            cond = ((fx-1)*hx)/gx
        if str(id) in str(cond):
            z.append(cond)
    def check2(fx,gx,hx,id,x,nt,n3):
        ncond = 0
        if hx < (float(fx)/float(gx)):
            cond = (fx/gx) + hx
            ncond = 1
        elif hx >= (fx/gx):
            cond = ((fx-1)*hx)/gx
            ncond = 2
        if str(id) in str(cond):
            if nt<4:
                nt += 1
                form ='[{}] x = {} --> f(x) = {} --> g(f(x)) = {} --> h(g(f(x))) = {}'
                form2 = '--> conver(f, g, h) = {} --> Result = True'
                print(form.format(n3,x,fx,gx,hx))
                print(form2.format(cond))
        return nt
    def check3(f,g,h,id,x,nt1):
        ncond = 0
        if h[0] < (f[0]/g[0]):
            cond = (f[0]/g[0]) + h[0]
            ncond =1
        elif h[0] >= (f[0]/g[0]):
            cond = ((f[0]-1)*h[0])/g[0]
            ncond =2
        if str(id) in str(cond):
            if nt1<4:
                nt1 += 1
                cor ='({},{})'
                print('Condition',f[1],'within f(x), the coordintate is',cor.format(x,f[0]))
                print('Condition',g[1],'within g(x), the coordintate is',cor.format(f[0],g[0]))
                print('Condition',h[1],'within h(x), the coordintate is',cor.format(g[0],h[0]))
                print('Condition',ncond,'within Convert function, the result is',cond)
                print('===========================================================================')   
        return nt1
z = []
never = {}
a1 = 0
a2 = 20
id = 2+2+2+1+6+1+0+0+7+0
print('The starting value :',a1)
print('The ending value :',a2)
n3 = 0
nt = 0
nt1 = 0
re = A(a1,a2,id)
noi = re.idk(0)
print('===========================================================================')
print('student id : 2221610070 --> The reference value :',id)
print('===========================================================================')
never['gonna give you up'] = noi
print('The amount of input :',never['gonna give you up'])
print('===========================================================================')
for x in range (a1,a2,1):
    n3 += 1
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
    gx = A.g(fx[0])
    hx = A.h(gx[0])
    never['gonna let you down'] = B.check(fx[0],gx[0],hx[0],id)
    never['gonna run around and desert you'] = B.check2(fx[0],gx[0],hx[0],id,x,nt,n3)
print('The amount of True output :', len(z))
if len(z) == 0:
    print('There is no True output;')
elif len(z) ==1:
    print('The only True output is shown above; ')
elif 1<len(z)<=4:
    print('The True output is shown above; ')
else:
    print('The first 4 of them are shown above;')
print('===========================================================================')
for x in range (a1,a2,1):
    n3 += 1
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
    gx = A.g(fx[0])
    hx = A.h(gx[0])
    never['gonna make you cry'] = B.check3(fx,gx,hx,id,x,nt1)
if len(z) == 0 :
    print('Get into the condition number 1, the final output of the model is',id)
elif len(z) == 1 :
    s = str(z)
    z2 = list()
    for i in s:
        if i.isdigit():
            z2.append(int(i))
    print('Get into the condition number 2, the final output of the model is',sum(z2))
elif len(z)>1 :
    print('Get into the condition number 3, the final output of the model is',sum(z)/len(z))
print('===========================================================================')