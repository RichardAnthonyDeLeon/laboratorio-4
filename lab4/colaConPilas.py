from collections import deque
import time

class ColaConPilas:
    def __init__(self, lista, cola = deque([])):
        self.lista = lista
        self.cola = cola
            
    def creacionPila1(self):
        pila1=[]
        for x in self.lista:
            pila1.append(x)
        print('Entrada de elementos a la Pila 1:\n','Pila1:',pila1) #Se crea pila1
        while pila1:
            salidaElemento= pila1.pop()
            self.cola.append(salidaElemento) #Se crea la cola insertandole los elemento de la pila1
        print('Salida de elementos de la Pila 1 y entrada de elementos a la Cola:\n','Cola:',self.cola)
        
            
        
    def salidaCola(self):
        pila2=[]#Se crea pila2
        print('Salida de elementos de la Cola y entrada de elementos a la Pila2:') #Salida de elementos de la cola para ingresarlos a pila#2
        for x in self.cola:    
            pila2.append(x)
        print(' Pila2:',pila2)
        while pila2:
            pila2.pop()
        print('Salida de elementos de la Pila2:\n','Pila2:',pila2)
        
        

print('Creación de Cola a partir de Pilas:\n')
lista1= input('Escriba Los elementos a trabajar separados por espacio: ').split()
objeto1 = ColaConPilas(lista1)
objeto1.creacionPila1()
objeto1.salidaCola()
    