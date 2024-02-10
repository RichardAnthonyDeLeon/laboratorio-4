import time

def pila(lista):
    pila = []
    print('Pila Creada: ')
    for elemento in lista:
        print(f'Elemento "{elemento}" entrando a la Pila')#Elementos entrando a la pila
        time.sleep(1)
        pila.append(elemento)
        print(pila)
    print('\n')
    
    print("Elementos saliendo de la pila:\n")
    while pila:
        print(pila)
        print(f'Elemento "{elemento}" saliendo de la Pila')#Elementos saliendo de la Pila
        elemento = pila.pop()
        time.sleep(1)
        
    lista_invertida = []
    while lista:
        ultimo = lista.pop()
        lista_invertida.append(ultimo) #Reversión de elementos de la pila
    
    print("\nLista Invertida utilizando la PILA creada:", lista_invertida)
        

lista = input("Ingrese la lista separada por espacios: ").split()
pila(lista)
        