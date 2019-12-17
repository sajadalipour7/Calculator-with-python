from tkinter import *
import math
a = Tk()
q=0
p=0
t=0
s=0
a.title("Calculator(CR7)")
a.geometry('347x386')
a.configure(background = 'yellowgreen')
c = Entry(a,justify=RIGHT,width = 55)
c.place(x = 6 , y = 5)
def dl(x):
    global p
    p = c.get()
    global t
    t = len(p)
    c.delete(t-1)
def clear(x):
    c.delete(0,END)
def f(x):
    c.insert(100,'1')
def f1(x):
    c.insert(100,'2')
def f2(x):
    c.insert(100,'3')
def f3(x):
    c.insert(100,'4')
def f4(x):
    c.insert(100,'5')
def f5(x):
    c.insert(100,'6')
def f6(x):
    c.insert(100,'7')
def f7(x):
    c.insert(100,'8')
def f8(x):
    c.insert(100,'9')
def f9(x):
    c.insert(100,'0')
def let(x):
    global p
    p = float(c.get())
    global i
    i = 0
    while p > 0:
        p = p // 10
        i+=1
    c.delete(0,END)
    c.insert(0,i)
    return p
def ch(x):
    global p
    p = int(c.get())
    p = chr(p)
    c.delete(0,END)
    c.insert(0,p)
    return p
def asinr(x):
    global p
    p = float(c.get())
    p = math.radians(p)
    p = math.asin(p)
    c.delete(0,END)
    c.insert(0,p)
    return p
def cotr(x):
    global p
    p = float(c.get())
    p = math.radians(p)
    p = math.atan(p)
    c.delete(0,END)
    c.insert(0,p)
    return p
def det(x):
    global p
    p = float(c.get())
    p = math.degrees(p)
    c.delete(0,END)
    c.insert(0,p)
    return p
def radi(x):
    global p
    p = float(c.get())
    p = math.radians(p)
    c.delete(0,END)
    c.insert(0,p)
    return p
def logi(x):
    global p
    p = float(c.get())
    p = math.log10(p)
    c.delete(0,END)
    c.insert(0,p)
    return p
def lgi(x):
    global p
    global s
    p = float(c.get())
    s = p
    global y
    y = 22
    c.delete(0,END)
    return p
def ghir(x):
    global p
    p = float(c.get())
    p = math.fabs(p)
    c.delete(0,END)
    c.insert(0,p)
    return p
def asu(x):
    global p
    p = float(c.get())
    p = math.radians(p)
    p = math.asinh(p)
    c.delete(0,END)
    c.insert(0,p)
    return p
def ac(x):
    global p
    p = float(c.get())
    p = math.radians(p)
    p = math.acos(p)
    c.delete(0,END)
    c.insert(0,p)
    return p
def aci(x):
    global p
    p = float(c.get())
    p = math.radians(p)
    p = math.acosh(p)
    c.delete(0,END)
    c.insert(0,p)
    return p
def ori(x):
    global p
    p = c.get()
    p = ord(p)
    c.delete(0,END)
    c.insert(0,p)
    return p
def ini(x):
    global p
    global s
    p = float(c.get())
    s = int(p)
    c.delete(0,END)
    c.insert(0,s)
    return s
def mok(x):
    global s
    s = math.e
    c.delete(0,END)
    c.insert(0,s)
    return s
def tan(x):
    global p
    p = float(c.get())
    s = p
    global y2
    global y1
    y2 = math.radians(s)
    y1 = math.tan(y2)
    c.delete(0,END)
    c.insert(0,y1)
    return y1
def tavan(x):
    global p
    global s
    p = float(c.get())
    s = p
    global y
    y = 10
    c.delete(0,END)
    return s
def bagh(x):
    global p
    global s
    p = float(c.get())
    s = p
    global y
    y = 11
    c.delete(0,END)
    return s
def kharej(x):
    global p
    global s
    p = float(c.get())
    s = p
    global y
    y = 12
    c.delete(0,END)
    return s
def add(x):
    global p
    global s
    p =float(c.get())
    s = p
    global y
    y = 1
    c.delete(0,END)
    return s
def tafrigh(x):
    global p
    p = (float(c.get()))
    global s
    s = p
    global y
    y = 2
    c.delete(0,END)
    return s
def equal(x):
    global t
    t =float(c.get())
    global s
    global q
    global i
    global bmm
    bmm = 1
    i = 0
    if y == 1 :
        q = s + t
    elif y == 2 :
        q = s - t
    elif y == 3:
        q = s * t
    elif y == 4 :
        q = s / t
    elif y==8:
        if s>t:
            k=t
        else :
            k=s
        while i<=k:
            i+=1
            if s%i==0 and t%i==0:
                bmm = i
        q = bmm
    elif y==9:
        if s>t:
            k=t
        else :
            k=s
        while i<=k:
            i+=1
            if s%i==0 and t%i==0:
                bmm = i
        r = s * t
        r2 = r/bmm
        q = r2
    elif y == 10:
        q = s ** t
    elif y == 11:
        q = s % t
    elif y == 12:
        q = s // t
    elif y == 13:
        q = s ** (1/t)
    elif y == 22:
        q = math.log(s,t)
    c.delete(0,END)
    c.insert(100,q)
    return s
def dot(x):
    global t2
    global u
    t2 = float(c.get())
    u = t2 / 10
    c.delete(0,END)
    c.insert(100,u)
def mosmen(x):
    u1 = -1 * float(c.get())
    c.delete(0,END)
    c.insert(100,u1)
def zarb(x):
    global p
    global s
    p =float(c.get())
    s = p
    global y
    y = 3
    c.delete(0,END)
    return s
def taghsim(x):
    global p
    global s
    p =float(c.get())
    s = p
    global y
    y = 4
    c.delete(0,END)
    return s
def sino(x):
    global p
    global s
    global y
    global y2
    p = float(c.get())
    s = p
    y2 = math.radians(s)
    y = math.sin(y2)
    c.delete(0,END)
    c.insert(100,y)
    return s
def cosinos(x):
    global p
    global s
    global y
    p = float(c.get())
    s = p
    y2 = math.radians(s)
    y = math.cos(y2)
    c.delete(0,END)
    c.insert(100,y)
    return s
def aval(x):
    global p
    global s
    global i
    global e
    e = 0
    i = 1
    p = float(c.get())
    s=p
    while i<=p:
        if p%i==0:
            e = e + 1
        i+=1
    if e>2:
        c.delete(0,END)
        c.insert(0,"No")
    else :
        c.delete(0,END)
        c.insert(0,"Yes")
    return s
def fact(x):
    global p
    global s
    global tyu
    p = float(c.get())
    s = int(p)
    tyu = 1
    for i in range(1,s+1):
        tyu = tyu * i
    c.delete(0,END)
    c.insert(0,tyu)
def majmo(x):
    global p
    global s
    global iu
    iu = 0
    p = float(c.get())
    s = p
    while s>0:
        iu = iu + s%10
        s = s // 10
    c.delete(0,END)
    c.insert(0,int(iu))
def rad(x):
    global p
    global s
    global y
    global y2
    p = float(c.get())
    s = p
    y = 13
    c.delete(0,END)
    return s
def tma(x):
    global p
    global s
    global ik
    global tuy
    ik = 1
    tuy = 0
    p = float(c.get())
    s = p
    while ik<=s:
        if s%ik==0 :
            tuy+=1
        ik+=1
    c.delete(0,END)
    c.insert(0,tuy)
def bmm(x):
    global p
    global s
    p =float(c.get())
    s = p
    global y
    y = 8
    c.delete(0,END)
def kmm(x):
    global p
    global s
    p =float(c.get())
    s = p
    global y
    y = 9
    c.delete(0,END)
def abo(x):
    t = Tk()
    t.title("About Program")
    l1 = Label(t,text="Calculator(CR7) version 1.0")
    l2 = Label(t,text="I'm mohammad sajad alipour and this program created by me")
    l3 = Label(t,text="This program is a verygood calculator for engineers and other people")
    l4 = Label(t,text="next version of Calculator(CR7) is coming soon...")
    l5 = Label(t,text="My site : www.CR7group.blog.ir")
    l6 = Label(t,text="My E-mail : sajadalipour1380@gmail.com")
    l7 = Label(t,text="Enjoy it!")
    l8 = Label(t,text="If you like this program follow my instagram : sajadalipourcr7")
    l1.pack()
    l2.pack()
    l3.pack()
    l4.pack()
    l5.pack()
    l6.pack()
    l7.pack()
    l8.pack()
def p(x):
    global s
    s = math.pi
    c.delete(0,END)
    c.insert(0,s)
    return s
def bord(x):
    br = Tk()
    br.geometry("405x605")
    br.title('Boardar')
    global j
    j = Canvas(br,width = 400,height = 400,bg = 'white' )
    j.place(x = 0 , y = 200)
    vao = j.create_line(5,200,395,200)
    vaa = j.create_line(200,5,200,395)
    tr1 = j.create_oval(10,195 ,5,205,fill='black')
    tr2 = j.create_oval(390,195 ,395,205,fill='black')
    tr3 = j.create_oval(195,10 ,205,5,fill='black')
    tr4 = j.create_oval(195,390 ,205,395,fill='black')
    lx1 = Label(br,text="X1 :")
    lx1.place(x=10,y=5)
    ex1 = Entry(br,width=10)
    ex1.place(x=40,y=5)
    ly1 = Label(br,text="Y1 :")
    ly1.place(x=10,y=35)
    ey1 = Entry(br,width=10)
    ey1.place(x=40,y=35)
    lx2 = Label(br,text="X2 :")
    lx2.place(x=10,y=65)
    ex2 = Entry(br,width=10)
    ex2.place(x=40,y=65)
    ly2 = Label(br,text="Y2 :")
    ly2.place(x=10,y=95)
    ey2 = Entry(br,width=10)
    ey2.place(x=40,y=95)
    veri = Button(br,text="Verify",width ='4',height ='2',bg = 'goldenrod2')
    veri.place(x = 150 , y = 25)
    lx3 = Label(br,text="X3 :")
    lx3.place(x=240,y=5)
    ex3 = Entry(br,width=10)
    ex3.place(x=270,y=5)
    ly3 = Label(br,text="Y3 :")
    ly3.place(x=240,y=35)
    ey3 = Entry(br,width=10)
    ey3.place(x=270,y=35)
    lx4 = Label(br,text="X4 :")
    lx4.place(x=240,y=65)
    ex4 = Entry(br,width=10)
    ex4.place(x=270,y=65)
    ly4 = Label(br,text="Y4 :")
    ly4.place(x=240,y=95)
    ey4 = Entry(br,width=10)
    ey4.place(x=270,y=95)
    def b(x):
        x1 = float(ex1.get())
        y1 = float(ey1.get())
        x2 = float(ex2.get())
        y2 = float(ey2.get())
        x3 = float(ex3.get())
        y3 = float(ey3.get())
        x4 = float(ex4.get())
        y4 = float(ey4.get())
        line1 = j.create_line(x1,y1,x2,y2,fill='blue')
        ltr1 = j.create_oval(x2,y2,x2+5,y2+5,fill='black')
        line2 = j.create_line(x3,y3,x4,y4,fill='red')
        ltr2 = j.create_oval(x4,y4,x4+5,y4+5,fill='black')
        line3 = j.create_line(200,200,x2+x4,y2+y4,fill='green')
        ltr3 = j.create_oval(x2+x4,y2+y4,x2+x4+5,y2+y4+5,fill='black')
    veri.bind('<Button-1>',b)    
b = Button(a,text = '7' , bg = 'goldenrod2' , width = '5' , height = '2' )
b.place(x = 6 , y = 30)
y = Button(a,text = 'Clear', bg = 'goldenrod2' , width = '5' , height = '2')
y.place(x = 6 , y = 180)
y.bind('<Button-1>' , clear)
b.bind('<Button-1>' , f6)
b2 = Button(a,text = '8' , bg = 'goldenrod2', width = '5' , height = '2' )
b2.place(x = 60 , y = 30)
b2.bind('<Button-1>' , f7)
b3 = Button(a,text = '9' , bg = 'goldenrod2', width = '5' , height = '2' )
b3.place(x = 60+54 , y =30)
b3.bind('<Button-1>' , f8)
b4 = Button(a,text = '4' , bg = 'goldenrod2', width = '5' , height = '2' )
b4.place(x = 6 , y = 80)
b4.bind('<Button-1>' , f3)
b5 = Button(a,text = '5' , bg = 'goldenrod2', width = '5' , height = '2' )
b5.place(x = 60 , y = 80)
b5.bind('<Button-1>' , f4)
b6 = Button(a,text = '6' , bg = 'goldenrod2' , width = '5' , height = '2')
b6.place(x = 60+54 , y = 80)
b6.bind('<Button-1>' , f5)
b7 = Button(a,text = '1' , bg = 'goldenrod2', width = '5' , height = '2' )
b7.place(x = 6 , y = 130)
b7.bind('<Button-1>' , f)
b8 = Button(a,text = '2' , bg = 'goldenrod2' , width = '5' , height = '2')
b8.place(x = 60 , y = 130)
b8.bind('<Button-1>' , f1)
b9 = Button(a,text = '3' , bg = 'goldenrod2', width = '5' , height = '2' )
b9.place(x = 60+54 , y = 130)
b9.bind('<Button-1>' , f2)
b0 = Button(a,text = '0' , bg = 'goldenrod2', width = '5' , height = '2' )
b0.place(x = 60 , y = 180)
b0.bind('<Button-1>' , f9)
plus = Button(a,text = '+' , bg = 'goldenrod2', width = '4' , height = '2')
men = Button(a,text = '-' , bg = 'goldenrod2' , width = '4',height='2')
men.bind('<Button-1>' ,tafrigh)
men.place(x = 114+54 , y = 80)
plus.bind('<Button-1>' , add)
plus.place(x = 114+54 , y = 30)
eq = Button(a,text = '=' , bg = 'goldenrod2' , width = '4',height='2')
za = Button(a,text = '*' , bg = 'goldenrod2' , width = '4',height='2')
za.bind('<Button-1>' ,zarb)
za.place(x = 114+54 , y = 130)
ta = Button(a,text = '/' , bg = 'goldenrod2',width = '4',height='2')
ta.bind('<Button-1>' , taghsim)
ta.place(x = 114+54 , y = 180)
mos = Button(a,text = '+/-' , bg = 'goldenrod2' , width = '5',height='2')
mos.bind('<Button-1>' ,mosmen)
mos.place(x=114 , y = 230)
si = Button(a,text = 'sin' , bg = 'goldenrod2' , width = '5',height='2')
si.bind('<Button-1>' ,sino)
si.place(x=114 - 54 , y = 230)
co = Button(a,text = 'cos' , bg = 'goldenrod2' , width = '5',height='2')
co.bind('<Button-1>' ,cosinos)
co.place(x=6 , y = 230)
do = Button(a,text = '.' , bg = 'goldenrod2' , width = '5',height='2')
do.bind('<Button-1>' ,dot)
do.place(x = 114 , y = 180)
eq.bind('<Button-1>' ,equal)
eq.place(x = 114+54 , y = 230)
dr=Button(a,text = "Delete",bg='goldenrod2',width="4",height="2")
dr.bind("<Button-1>" , dl)
dr.place(x=114+54+45,y=230)
av=Button(a,text = "AVAL",bg='goldenrod2',width="5",height="1")
av.bind("<Button-1>" , aval)
av.place(x=114,y=280)
fa=Button(a,text = "!",bg='goldenrod2',width="5",height="1")
fa.bind("<Button-1>" , fact)
fa.place(x=114-54,y=280)
maj=Button(a,text = "MA",bg='goldenrod2',width="5",height="1")
maj.bind("<Button-1>" , majmo)
maj.place(x=6,y=280)
ra=Button(a,text = "radical",bg='goldenrod2',width="4",height="2")
ra.bind("<Button-1>" , rad)
ra.place(x=114+54+45,y=180)
tm=Button(a,text = "TM",bg='goldenrod2',width="4",height="1")
tm.bind("<Button-1>" , tma)
tm.place(x=114+54+45,y=315)
bm=Button(a,text = "BMM",bg='goldenrod2',width="5",height="1")
bm.bind("<Button-1>" , bmm)
bm.place(x=114-54,y=315)
km=Button(a,text = "KMM",bg='goldenrod2',width="5",height="1")
km.bind("<Button-1>" , kmm)
km.place(x=114,y=315)
tav=Button(a,text = "**",bg='goldenrod2',width="4",height="2")
tav.bind("<Button-1>" , tavan)
tav.place(x=114+54+45,y=30)
baghi=Button(a,text = "%",bg='goldenrod2',width="4",height="2")
baghi.bind("<Button-1>" , bagh)
baghi.place(x=114+54+45,y=80)
kh=Button(a,text = "//",bg='goldenrod2',width="4",height="2")
kh.bind("<Button-1>" , kharej)
kh.place(x=114+54+45,y=130)
tanj=Button(a,text = "tan",bg='goldenrod2',width="4",height="2")
tanj.bind("<Button-1>" , tan)
tanj.place(x=114+54+45+45,y=180)
pi=Button(a,text = "P",bg='goldenrod2',width="4",height="1")
pi.bind("<Button-1>" , p)
pi.place(x=114+54,y=280)
e=Button(a,text = "e",bg='goldenrod2',width="4",height="1")
e.bind("<Button-1>" , mok)
e.place(x=114+54,y=315)
inti=Button(a,text='int',width='4',height='1',bg='goldenrod2')
inti.bind("<Button-1>" , ini)
inti.place(x=114+54+45,y=280)
asi = Button(a,text="asin" , bg = "goldenrod2",width = '4' , height='2')
asi.bind("<Button-1>" , asinr)
asi.place(x=114+54+45+45+45,y=30)
bor = Button(a,text="Boardar" , bg = "goldenrod2",width = '5' , height='1')
bor.bind("<Button-1>" , bord)
bor.place(x=6,y=315)
chi = Button(a,text="Chr" , bg = "goldenrod2",width = '4' , height='2')
chi.bind("<Button-1>" , ch)
chi.place(x=114+54+45+45,y=30)
orib = Button(a,text="Ord" , bg = "goldenrod2",width = '4' , height='2')
orib.bind("<Button-1>" , ori)
orib.place(x=114+54+45+45,y=80)
leti = Button(a,text="Len" , bg = "goldenrod2",width = '4' , height='2')
leti.bind("<Button-1>" , let)
leti.place(x=114+54+45+45,y=130)
aco = Button(a,text="acos" , bg = "goldenrod2",width = '4' , height='2')
aco.bind("<Button-1>" , ac)
aco.place(x=114+54+45+45+45,y=80)
ach = Button(a,text="acosh" , bg = "goldenrod2",width = '4' , height='2')
ach.bind("<Button-1>" , aci)
ach.place(x=114+54+45+45+45,y=130)
asih = Button(a,text="asinh" , bg = "goldenrod2",width = '4' , height='2')
asih.bind("<Button-1>" , asu)
asih.place(x=114+54+45+45+45,y=180)
dei = Button(a,text="Degres" , bg = "goldenrod2",width = '4' , height='1')
dei.bind("<Button-1>" , det)
dei.place(x=114+54+45+45+45,y=280)
rad = Button(a,text="Radian" , bg = "goldenrod2",width = '4' , height='1')
rad.bind("<Button-1>" , radi)
rad.place(x=114+54+45+45+45,y=315)
ghi = Button(a,text="Gh-M" , bg = "goldenrod2",width = '4' , height='1')
ghi.bind("<Button-1>" , ghir)
ghi.place(x=114+54+45+45,y=280)
coti = Button(a,text="cot" , bg = "goldenrod2",width = '4' , height='1')
coti.bind("<Button-1>" , cotr)
coti.place(x=114+54+45+45,y=315)
lo = Button(a,text="log10" , bg = "goldenrod2",width = '4' , height='2')
lo.bind("<Button-1>" , logi)
lo.place(x=114+54+45+45,y=230)
lg = Button(a,text="log" , bg = "goldenrod2",width = '4' , height='2')
lg.bind("<Button-1>" , lgi)
lg.place(x=114+54+45+45+45,y=230)
l = Label(a,text="By : SAJAD.CR7 / Copyright@2015",width = "47" , height = "2")
l.place(x = 6 , y = 345)
l.bind("<Button-1>",abo)
a.mainloop()
#By : Sajad.CR7          CopyRight@2015 

 
 


