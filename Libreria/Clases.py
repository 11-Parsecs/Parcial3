from types import NoneType
import matplotlib.pyplot as plt
from numpy import linspace

Txt1="No se pueden operar Contables con diferentes asignaciones."
Txt2="Tipos de dato incorrectos."

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
    def __str__(self): #Representación
        return str(self.m)+"}->"+str(self.n)+"]->"+str(self.a)
    def __add__(self,other): #Suma con +
        if self.m==other.m and self.n==other.n:
            return Contable(self.m,self.n,self.a+other.a)
        else:
            print(Txt1)
    def __truediv__(self,other): #División con /
        if self.m==other.m and self.n==other.n:
            return Contable(self.m,self.n,self.a/other.a,self.T+other.T)
        else:
            print(Txt1)
    def __iadd__(self, other): #Suma con +=
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
    def __str__(self): #Representación
        return str(self.N)+"}->"+str(self.n)+"-s-"+str(self.m)+"<-{"+str(self.M)
    def Tomar(self,A,a,Txt="",Prom=False):
        '''
        Devuelve un Contable sumando los valores de la base de datos "A" coincidentes
        a la fila y a las columnas "self.n" de "self.N" y "self.m" de "self.M"
        ----------
        A : list of lists
            Matriz con la información de una base de datos
        a : str
            Nombre de la columna de datos a tomar
        Txt : str, optional
            Guarda el Contable de salida bajo un nombre
        Prom : bool, optional
            True si el Contable de salida es el promedio de los datos y False si es sólo la suma
        '''
        Cuenta=0
        U=Contable(self.M,self.n,0)
        f1=A[0].index(self.N)
        f2=A[0].index(a)#Columna de datos a tomar
        f3=A[0].index(self.M)
        for L in A:
            if L[f1]==self.n and L[f3]==self.m:
                try:
                    Cuenta+=1
                    U+=Contable(self.M,self.n,eval(L[f2]))#Suma los datos tomados
                except:
                    Cuenta+=1
                    U+=Contable(self.M,self.n,0)
        if Cuenta!=0 and Prom:
            if Prom:
                U=U/Contable(self.M,self.n,Cuenta,Txt)#Promedio de los datos
        else:
            U=NoneType #Si hay algún error
        return U

class Proceso:
    '''
    Almacena y opera con Contables de una matriz
    '''
    def __init__(self,A):
        self.A=A
    def __str__(self): #Representación
        return "[{"+str(self.A)+"}]"
    def __setitem__(self,N_Dato,Valor): #Mutabilidad
        try:
            self.A[N_Dato]=Valor
        except IndexError:
            self.A.append(Valor)
    def __getitem__(self,N_Dato): #Itemización
        return self.A[N_Dato]
    def mostrar(self,reg=False):
        '''
        Grafica los datos de contenidos en la clase Proceso. El término "self.A" debe 
        ser una lista de listas de clases Contable.
        ----------
        reg: bool, optional
            True para graficar regresión lineal.
        '''
        if type(self.A)==list:
            Tiempo=0
            X=[]
            Y=[]
            for L in self.A:
                if type(L)==list: #Se asegura del tipo de datos
                    for D in L:
                        if type(D)==Contable:
                            X.append(D.T) #Texto asociado a los Contable
                            Y.append(D.a)
                            Tiempo+=2
                        else:
                            break
                else:
                    print(Txt2)

            fig=plt.figure() #Crea la figura
            fig.set_figwidth(20)
            fig.set_figheight(6.5)
            ax=fig.add_subplot(1,1,1)
            ax.plot(X,Y,'-og') #Muestra los datos unidos por líneas
            
            if reg: #Hace la regresión en caso de pedirla
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
            print(Txt2)