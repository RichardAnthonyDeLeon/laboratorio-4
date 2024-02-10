
def parentesisBalanceados(cadena):
    pila = []
    for caracter in cadena:
        if caracter == '(': 
            pila.append(caracter) 
        elif caracter == ')':#Se verifica si la cadena tiene una apertura '(' y un cierre ')'
            if pila:        
                pila.pop()
            else:
                return False 
    
    return not pila #Retorna True o False si la pila está vacía

cadena = input('Ingresa una cadena que contenga paréntesis para verificar si son balanceados: ')
if(parentesisBalanceados(cadena)):
    print('Secuencia de paréntesis balanceada!')
else:
    print('Secuencia de paréntesis no balanceada!')
    