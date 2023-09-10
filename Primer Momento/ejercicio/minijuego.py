import random

def chances():

    vidas = 5
    puntos = 0

    while vidas != 0:
    
        num = random.randint(0,9)
    
        if num == 0:
            # vidas -= vidas
            vidas = vidas - 1
            print("\n" + f" ------> Te quedan {vidas} vidas \n")
        else : 
            # puntos += 1
            puntos = puntos + 1
            print(f"Has ganado {puntos} puntos")