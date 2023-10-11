#                                 GUIA 7 WHAT NOW??
import random

#1.1
def pertenece(lista:list[any],x:any) -> bool:
    res:bool=False
    for i in lista:
        if i == x:
            res:bool=True
    return res

#1.2
def divide_a_todos(lista:list[int],x:int) -> bool:
    res:bool=True
    for i in lista:
        if i%x != 0:
            res:bool=False
    return res

#1.3
def suma_total(lista:list[int]) -> int:
    res:int=0
    for i in lista:
        res+=i
    return res

#1.4
def ordenados(lista:list[int]) -> bool:
    res:bool=True
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            res:bool=False
    return res  

#1.5
def la_tiene_larga(palabras:list[str]) -> bool:
    res:bool=False
    for palabra in palabras:
        if len(palabra) >= 7:
            res:bool=True
    return res

#1.6
def palindromo(texto: str) -> bool:
    texto = aplanar(texto.lower())  #Convierto en minusculas las mayusculas
    return texto == aplanar(reverso(texto))

def aplanar(texto:str) -> str:
    sin_blancos:str=''
    for i in range(len(texto)):
        if texto[i] != ' ':
            sin_blancos += texto[i]
    return sin_blancos

def reverso(texto:str) -> str:
    al_revez:str=''
    for i in range(len(texto)-1,-1,-1):
        al_revez += texto[i]
    return al_revez

#1.7
def fortaleza(password:str) -> str:
    if len(password) > 8 and es_segura(password):
        res:str="VERDE"
    elif len(password) < 5:
        res:str="ROJA"
    else:
        res:str="AMARILLA"
    return res            

def es_segura(password:str) -> bool:
    res:bool=False
    for i in password:
        if 'A' <= i <= 'Z':  #Busco una mayuscula
            for i in password:
                if 'a' <= i <= 'z':  #Busco una minuscula
                    for i in password:
                        if '0' <= i <= '9':  #Busco un numero
                            res:bool=True
    return res 

#1.8
def saldo_actual(historial:list[tuple[str,int]]) -> int:
    saldo:int=0
    for movimiento in historial:
        if movimiento[0] == "I":
            saldo += movimiento[1]
        else:
            saldo -= movimiento[1]
    return saldo

#1.9
def es_variada(palabra:str) -> bool:
    return len(solo_vocales(palabra)) >= 3

def es_vocal(letra:str) -> bool:
    if letra in ['a','e','i','o','u']:
        res:bool=True
    elif letra in ['A','E','I','O','U']:
        res:bool=True
    else:
        res:bool=False
    return res    

def solo_vocales(palabra:str) -> str:
    palabra:str=palabra.lower()
    vocales:str=''
    for i in range(len(palabra)): 
        if es_vocal(palabra[i]) and palabra[i] not in palabra[i+1:]:
            vocales += palabra[i]
    return vocales

#2.1
def cero_en_pares_inout(lista:list[any]) -> list[any]:
    for i in range(len(lista)):
        if i%2 != 0:
            lista[i] = 0
    return lista        

#2.2
def cero_en_pares_in(lista:list) -> list:
    nueva_lista:list = lista.copy()  #Copio el valor de lista en otra referencia fuera de lista.
    for i in range(len(nueva_lista)):
        if i%2 == 0:
            nueva_lista[i] = 0
    return nueva_lista

#2.3
def no_vocales(palabra:str) -> str:
    sin_vocales:str=''
    for letra in palabra:
        if not es_vocal(letra):
            sin_vocales+=letra
    return sin_vocales

#2.4
def reemplaza_vocales(palabra:str) -> str:
    hyphen:str=''
    for letra in palabra:
        if es_vocal(letra):
            hyphen += '-'
        else:
            hyphen+= letra    
    return hyphen

#2.5
'''es funcion reverso que hize en #1.6 lol.'''

#2.6
def eliminar_repetidos(palabra:str) -> str:
    sin_repetidos:str=''
    for i in range(len(palabra)):
        if palabra[i] not in palabra[i+1:]:
            sin_repetidos+=palabra[i]
    return sin_repetidos

#3.0
def buen_promedio(notas:list[int]) -> bool:
    res:bool=True
    for nota in notas:
        if nota < 4:
            res:bool=False
    return res  

def promociona_o_recursa(notas:list[int]) -> int:
    if buen_promedio(notas):
        if (suma_total(notas)/len(notas)) >= 7:
            res:int=1
        else:
            res:int=2
    else:
        res:int=3
    return res

#4.1
def mis_alumnes() -> list[str]:
    continuar: bool = True
    alumnxs: list[str] = []
    while continuar:
        entrada = input("Alumnos (escribe 'listo' para salir):")
        if entrada.lower() != "listo":
            alumnxs.append(entrada)
        else:
            continuar = False  # Actualiza continuar para salir del bucle
    return alumnxs

#4.2
def SUBE() -> list[tuple]:
    historial:list[tuple] = []
    continuar:bool=True
    while continuar == True:
        movimiento:str = input("Ingrese:\n'C' para cargar creditos\n'D' para descontar creditos\n'X' para finalizar:\n\n")
        if movimiento == "C":
            cargar:int = int(input("Monto a cargar:"))
            historial.append((movimiento,cargar))
            print(f"Movimientos:{historial}")
        elif movimiento == "D":
            cargar:int = int(input("Monto a descontar:"))
            historial.append((movimiento,cargar)) 
            print(f"Movimientos:{historial}")   
        elif movimiento == "X":
            continuar = False
    return historial

#4.3
def siete_y_medio() -> list[int]:
    continuar:bool = True
    cartas:list[float] = [1,2,3,4,5,6,7,0.5,0.5,0.5]
    inicio:int = random.choice(cartas)
    historial = [inicio]
    while True:
        if suma_total(historial) <= 7.5:
            jugada = random.randint(1,12)
            decision = input(f"Hasta ahora: {inicio}\nQue desea hacer?\n'A' Sacar otra carta:\n'B' Plantarse:\n\n")
            if decision == "A" and jugada in [8,9]:
                inicio+=0
                print(f"Sacaste :{jugada} pero no cuenta! Tienes otro intento!")
            elif decision == "A" and jugada in [10,11,12]:
                inicio+=0.5
                historial.append(0.5) 
                print(f"Sacaste:{jugada} pero vale 0.5")
            elif decision == "A" and jugada not in [10,11,12]:
                inicio+=jugada
                historial.append(jugada)
                print(f"Sacaste:{jugada}")
            elif decision == "B":
                print("Ganaste!")
                break
        else:
            print("Perdiste! Te pasaste!")
            break
    return historial         
        
           

   

            


siete()                         
  
                      
         
           




              
        


           
























       
    
         




        


                
















      


       









    


            


                






#1.7




  

       
    
        
        