import Libreria.Clases as cla #Importa las clases creadas

Dat=[]

f=open("C:/Users/Juan Pablo/Downloads/Combustible.csv", encoding="utf8") #Abre la base de datos a través de la ruta de archivo.
for T in  f:
    Dat.append(T.split(",")) #Convierte la base de datos en una matriz (lista de listas).
f.close()

P=cla.Proceso([]) #Dato de clase Proceso vacío
In=0
for k in range(2017,2023): #Busca datos desde el año 2017 al 2022
    Anual=[]
    for l in range(1,13): #Busca datos del 1 al 12, estos representan los meses
        Anual.append(cla.Dato("Periodo",str(k),"Mes",str(l)).Tomar(Dat,"Precio",str(k)+"-"+str(l),True)) #Se hace uso de los métodos de las clases
    P[In]=Anual
    In+=1

P.mostrar(True) #Se grafica la información