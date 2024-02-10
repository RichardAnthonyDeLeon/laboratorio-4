from collections import deque
import time

def cola(lista):
    lista_cola = []
    cola = deque(lista_cola)
    
    for element in lista:
        print(f'Atendiendo a {element}') #Atendiendo a los elementos que contiene la cola
        cola.append(element)
        time.sleep(1)
        print('En cola:',cola)
        time.sleep(1)
        
    print("\n")
    print("Desencolando: \n")
    
    while cola:
        print(cola)
        time.sleep(1)
        print(f'{cola[0]} atendido')
        time.sleep(1)
        cola.popleft() #Desencolando a los elementos de la cola.
        
            
lista = input('Ingresa los nombres de los clientes separándolos por espacio\nPara que sean atendidos de manera ordenada : ').split()
cola(lista)
        