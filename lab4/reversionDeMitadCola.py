from collections import deque

def reversionMitad(lista):
    pseduCola = []
    cola = deque(pseduCola)
    pila = []
    N = len(lista) #Longitud de la lista 
    n = len(lista) // 2 #Mitad de la longitud de la lista
    i = 0
    for x in lista:
        cola.append(x)       
    print('Cola normal Ingresada: ',cola)
    for i in range(N):
        if i < n:
            elementoReversion = cola.popleft() 
            pila.insert(0,elementoReversion) #Agregando a la pila los elementos revertidos necesarios
            i = i +1
        else:
            pila.append(cola.popleft()) #Agregando el resto de elemento no revertidos a la pila
    print('Cola con mitad revertida: ',pila)
       
lista = input('\n\nIngrese la cantidad de elementos separados por espacio para guardarlos en una cola\ny que a este se le revierta la mitad de sus elementos: ').split()
reversionMitad(lista)                
