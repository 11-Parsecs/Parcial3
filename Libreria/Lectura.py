from types import NoneType
import matplotlib.pyplot as plt

Txt1="No se pueden sumar Contables con diferentes asignaciones."

class Contable:
    '''
    Ah
    '''
    def __init__(self,m,n,a,T=""):
        self.m=m
        self.n=n
        self.a=a
        self.T=T
    def __str__(self):
        return str(self.m)+"}->"+str(self.n)+"]->"+str(self.a)
    def __add__(self,other):
        if self.m==other.m and self.n==other.n:
            return Contable(self.m,self.n,self.a+other.a)
        else:
            print(Txt1)
    def __truediv__(self,other):
        if self.m==other.m and self.n==other.n:
            return Contable(self.m,self.n,self.a/other.a,self.T+other.T)
        else:
            print(Txt1)
    def __iadd__(self, other):
        return self+other

class Dato(Contable):
    def __init__(self,N,n,M,m):
        self.N=N
        self.M=M
        self.n=n
        self.m=m
    def Tomar(self,A,a,Txt):
        Cuenta=0
        U=Contable(self.M,self.n,0)
        f1=A[0].index(self.N)
        f2=A[0].index(a) 
        f3=A[0].index(self.M)
        for L in A:
            if L[f1]==self.n and L[f3]==self.m:
                try:
                    Cuenta+=1
                    U+=Contable(self.M,self.n,eval(L[f2]))
                except:
                    Cuenta+=1
                    U+=Contable(self.M,self.n,0)
        if Cuenta!=0:
            U=U/Contable(self.M,self.n,Cuenta,Txt)
        else:
            U=NoneType#Contable(self.M,self.n,0)
        return U

class Proceso(Dato):
    def __init__(self,A):
        self.A=A
    def __str__(self):
        return "[{"+str(self.A)+"}]"
    def mostrar(self):
        if type(self.A)==list:
            Tiempo=0
            X=[]
            Y=[]
            for L in self.A:
                if type(L)==list:
                    for D in L:
                        if type(D)==Contable:
                            X.append(D.T)#D.n)
                            Y.append(D.a)
                            Tiempo+=2
                        else:
                            break
                else:
                    print("Eso no se puede")
            fig=plt.figure()
            fig.set_figwidth(15)
            fig.set_figheight(6.5)
            ax=fig.add_subplot(1,1,1)
            ax.plot(X,Y,'-og')
            plt.xticks(rotation=90)
            plt.grid()
            plt.show()
        else:
            print("Eso no se puede")


Dat=[]

f=open("C:/Users/Juan Pablo/Downloads/Combustible.csv", encoding="utf8")
for T in  f:
    Dat.append(T.split(","))
f.close()

Precio=[]
for k in range(2017,2023):
    Anual=[]
    for l in range(1,13):
        Anual.append(Dato("Periodo",str(k),"Mes",str(l)).Tomar(Dat,"Precio",str(k)+"-"+str(l)))
    Precio.append(Anual)

P=Proceso(Precio)
P.mostrar()