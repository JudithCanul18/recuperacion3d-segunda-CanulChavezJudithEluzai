#enviar git
#Canul Chavez Judith Eluzai
#n. control: 18390034
#examen de recuperacion 3D
import numpy as np
import matplotlib.pyplot as plt 
import keyboard #instalar el keyboard: pip install keyboard <-- en la terminal
from math import sin, cos, radians,sqrt

def plotTriangle(x,y,z):
    plt.axis([0,180,140,0])
    plt.axis('on')
    plt.grid(True)

    #ploteo del triangulo A
    plt.plot([x[0],x[1]],[y[0],y[1]],color='k') 
    plt.plot([x[1],x[2]],[y[1],y[2]],color='k')
    plt.plot([x[2],x[0]],[y[2],y[0]],color='k')
    plt.text(70,67,'A',color='k')#etiqueta para A

    #Hitpoint
    plt.scatter(x[3],y[3],s=18,color='r')

    #trazado
    plt.plot([x[0],x[3]],[y[0],y[3]],linestyle=':',color=('r')) 
    plt.plot([x[1],x[3]],[y[1],y[3]],linestyle=':',color=('r'))
    plt.plot([x[2],x[3]],[y[2],y[3]],linestyle=':',color=('r'))

    #Etiqueta para identificar las esquinas
    plt.text(35,63,'0', color='blue') 
    plt.text(25,10,'1', color='blue')
    plt.text(83,63,'2', color='blue')
    plt.text(x[3]+2,y[3],'3', color= 'blue')

    #Calcular distancia como perimetro Triangulo A utilizando: (lado a,b,c)(0,1, 2)
    A=sqrt(((x[1]-x[0])*(x[1]-x[0])) + ((y[1]-y[0])*(y[1]-y[0])))
    B=sqrt(((x[2]-x[0])*(x[2]-x[0])) + ((y[2]-y[0])*(y[2]-y[0])))
    C=sqrt(((x[2]-x[1])*(x[2]-x[1])) + ((y[2]-y[1])*(y[2]-y[1])))

    perimetroA = A+B+C
    spA = perimetroA/2
    AreaA= sqrt((spA*(spA-A)*(spA-B)*(spA-C)))
    plt.text(70,80,'Area=', color='k') 
    dle='%7.0f'% (AreaA)
    dls=str(dle)
    plt.text(85,80,dls)

    #Calcular distancia como perimetro Triangulo A1 utilizando: (lado a,b,c) (0,1,3)
    A1=sqrt(((x[1]-x[0])*(x[1]-x[0])) + ((y[1]-y[0])*(y[1]-y[0])))
    B1=sqrt(((x[3]-x[0])*(x[3]-x[0])) + ((y[3]-y[0])*(y[3]-y[0])))
    C1=sqrt(((x[3]-x[1])*(x[3]-x[1])) + ((y[3]-y[1])*(y[3]-y[1])))

    perimetroA1 = A1+B1+C1
    spA1 = perimetroA1/2
    AreaA1= sqrt((spA1*(spA1-A1)*(spA1-B1)*(spA1-C1)))
    plt.text(70,85,'Area 1=', color='k') 
    dle='%7.0f'% (AreaA1)
    dls=str(dle)
    plt.text(90,85,dls)

    #Calculo distancia como perimetro Triangulo A2 utilizando: (lados a,b,c) (0, 3, 2)
    A2=sqrt(((x[3]-x[0])*(x[3]-x[0])) + ((y[3]-y[0])*(y[3]-y[0])))
    B2=sqrt(((x[2]-x[0])*(x[2]-x[0])) + ((y[2]-y[0])*(y[2]-y[0])))
    C2=sqrt(((x[3]-x[2])*(x[3]-x[2])) + ((y[3]-y[2])*(y[3]-y[2])))

    perimetroA2 = A2+B2+C2
    spA2 = perimetroA2/2
    AreaA2= sqrt((spA2*(spA2-A2)*(spA2-B2)*(spA2-C2)))
    plt.text(70,90,'Area 2=', color='k')
    dle='%7.0f'% (AreaA2)
    dls=str(dle)
    plt.text(90,90,dls)
    #calculo del area total
    areaTotal=AreaA1+AreaA2

    #verificacion para ver si el hit point está afuera o dentro del limite
    if(areaTotal<AreaA):
        plt.text(50,110,'El Hit point se encuentra dentro de los limites.')
    else:
        plt.text(40,110,'El Hit point se encuentra fuera de los limites.')

    #hubicamos ejes x and y
    #asignamos titulo a la grafica
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.title("recuperacion 3D")
    plt.show()

#utilizamos el keyboard para poder utilizar la tecla ESC para finalizar la ejecucion y para que se de clic en Enter para empezar la ejecucion
print("Ingrese Enter para continuar, para terminar proceso presione tecla Esc")
while True:
    if keyboard.is_pressed('ENTER'):
        input()    
        #solicitar los puntos de las coordenadas x and y del hitpoint
        puntox=float(input('ingresa la coordena x del hitpoint:'))
        puntoy=float(input('ingresa la coordena y del hitpoint:'))
        #plano
        x=[40,30,80,puntox] 
        y=[60,10,60,puntoy]
        z=[0,0,0,0]
        plotTriangle(x,y,z)
    #texto que aparece al final para avisar que finalizo la ejecucion
    if keyboard.is_pressed('ESC'):
        print("La ejecucion ha finalizado.")
        break

