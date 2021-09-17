import time
from os import system, waitpid

atbash = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A', '.':'?', '?':'.'}

def atbash_cypher(message):
    finalMessage = ""
    for letter in message.upper():
        if letter != " ":
            finalMessage += atbash[letter]
        else:
            finalMessage += " "

    finalMessage = finalMessage.lower().capitalize()

    return finalMessage

def procesando (message):
    system("cls")
    y = message
    counter = 0 
    puntos = 0

    print(y)
    time.sleep(1)
    system("cls")
    while counter < 7:
        if puntos < 3:
            y += "."
            puntos += 1
            print(y)
            time.sleep(1)
            system("cls")
        else:
            y = message
            puntos = 0
            print(y)
            time.sleep(1)
            system("cls")

        counter += 1

def menu ():
    print("Hola niña de mis sueños")
    time.sleep(3)
    print("Aquí podrás descifrar los mensajes que te envie")
    time.sleep(5)
    inputVale = str(input("Pégalo aquí: "))
    mensaje = atbash_cypher(inputVale)
    print("..................................................................")
    print("Conecté más de 6 neuronas para hacer esto :')")
    print("..................................................................")
    time.sleep(2)
    procesando("Procesando su mensaje")
    procesando("Ya falta poquito")
    procesando("Te quiero muchito")
    print("..................................................................")
    print("Mensaje: " , mensaje)
    print("..................................................................")
    time.sleep(50)
menu()
    
