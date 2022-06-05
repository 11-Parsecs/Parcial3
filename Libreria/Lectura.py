from types import NoneType
import matplotlib.pyplot as plt
from numpy import linspace

Txt1="No se pueden sumar Contables con diferentes asignaciones."

class Contable:
    '''
    Crea un tipo de dato que se asemeja a las unidades; sólo se pueden operar los datos
    con la misma asignación. Sirve para agrupar datos asoaciados a dos variables, por
    ejemplo, puede ser usado para sumar sólo los datos de precio de febrero del año 2019.
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

class Espec_Contable(Contable):
    '''
    Contable con sólo una asignación. Por ejemplo, puede ser usado
    para sumar todos los datos de precio del año 2019.
    '''
    def init(self,n,a,T=""):
        super().__init__(0,n,a,T)

class Dato:
    '''
    Relaciona y mezcla los datos correspondientes entre filas y columnas.
    '''
    def __init__(self,N,n,M,m):
        self.N=N
        self.M=M
        self.n=n
        self.m=m
    def __str__(self):
        return str(self.N)+"}->"+str(self.n)+"-s-"+str(self.m)+"<-{"+str(self.M)
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
            U=NoneType
        return U

class Proceso:
    '''
    Almacena y opera con Contables de una matriz
    '''
    def __init__(self,A):
        self.A=A
    def __str__(self):
        return "[{"+str(self.A)+"}]"
    def __setitem__(self,N_Dato,Valor):
        try:
            self.A[N_Dato]=Valor
        except IndexError:
            self.A.append(Valor)
    def __getitem__(self,N_Dato):
        return self.A[N_Dato]
    def mostrar(self,reg=False):
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
            fig.set_figwidth(20)
            fig.set_figheight(6.5)
            ax=fig.add_subplot(1,1,1)
            ax.plot(X,Y,'-og')
            
            if reg:
                Xn=[]
                Sxi=0
                Sxi2=0
                Syi=0
                Sxy=0
                n=0
                for yi in Y:
                    n+=1
                    Syi+=int(yi)
                    Sxi+=n
                    Sxi2+=n**2
                    Sxy+=n*yi
                B=(n*Sxy-Sxi*Syi)/(n*Sxi2-(Sxi)**2)
                A=(Syi-B*Sxi)/n
                Xn=linspace(0,n+40,n+40)
                C=B*Xn+A
                ax.plot(Xn,C,'-or')

            ax.tick_params(axis='x', which='major', labelsize=7)
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

P=Proceso([])
In=0
for k in range(2017,2023):
    Anual=[]
    for l in range(1,13):
        Anual.append(Dato("Periodo",str(k),"Mes",str(l)).Tomar(Dat,"Precio",str(k)+"-"+str(l)))
    P[In]=Anual
    In+=1

P.mostrar(True)