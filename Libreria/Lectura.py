from matplotlib.pyplot import plot
from matplotlib.pyplot import xticks
from matplotlib.pyplot import show
from csv import reader

Txt1="No se pueden sumar Contables con diferentes asignaciones."

#Teracaloría, Gigavatio-hora, Kilotoneladas equivalentes del petróleo, Gigaunidades térmicas británicas
#Kilotón, Terajoules, Kilo-barriles de petróleo
Unidades={"TCal":2.39006*10**(-13),"GWh":2.7777777*10**(-13),"KTEP":2.38846*10**(-14),"GBTU":9.447817*10**(-13),
          "kTon":2.388459*10**(-13),"TJ":10**(12),"kBL":3.2982828*10**(-13),"Unidad Original":6.242*10**(18),"Mpc":0.000000000000922}#6.242*10**(18)}

class Contable:
    '''
    Ah
    '''
    def __init__(self,n,a):
        self.n=n
        self.a=a
    def __str__(self):
        return str(self.n)+"]->"+str(self.a)
    def __add__(self,other):
        if self.n==other.n:
            return Contable(self.n,self.a+other.a)
        else:
            print(Txt1)
    def __truediv__(self,other):
        if self.n==other.n:
            return Contable(self.n,self.a/other.a)
        else:
            print(Txt1)
    def __iadd__(self, other):
        return self+other

class Dato(Contable):
    def __init__(self,N,n):#,U
        self.N=N
        self.n=n
        #self.U=U
    def Tomar(self,A,a):
        Cuenta=0
        U=Contable(self.n,0)
        f1=A[0].index(self.N)
        f2=A[0].index(a) 
        #f3=A[0].index(self.U) 
        for L in A:
            if L[f1]==self.n:
                try:
                    Cuenta+=1
                    U+=Contable(self.n,eval(L[f2]))#/Unidades[L[f3]]*2.7777777*10**(-13))
                except:
                    Cuenta+=1
                    U+=Contable(self.n,0)
        U=U/Contable(self.n,Cuenta)
        return U

class Proceso(Dato):
    def __init__(self,A):
        self.A=A
    def __str__(self):
        return "["+str(self.A)+"]"
    def mostrar(self):
        Comprobar=True
        if type(self.A)==list:
            X=[]
            Y=[]
            for D in self.A:
                if type(D)==Contable:
                    X.append(D.n)
                    Y.append(D.a)
                else:
                    Comprobar=False
                    break
            if Comprobar:
                xticks(rotation=90)
                plot(X,Y,'-o')
                show()
            else:
                print("Eso no se puede")
        else:
            print("Eso no se puede")


Dat=[]

f=open("Combustible.csv", encoding="utf8")
for T in  f:
    Dat.append(T.split(","))
f.close()

EnergiaP=[]
for k in range(2017,2023):
    EnergiaP.append(Dato("Periodo",str(k)).Tomar(Dat,"Precio"))#,"Unidades Originales"

P=Proceso(EnergiaP)
P.mostrar()