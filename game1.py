import random
print("The Game.")
#funcion de de turno del jugador
def turn_jugador(ataque,habilidad,pocion):
    salud_enemiga=100
    salud_heroe=100
    generador_daño=random.randint(10,25)
    daño_habilidad=random.randint(30,50)
    cura=20
    accion = input("turno del jugar (ataque,habilidad,pocion)")
    if accion==ataque:
        ataque=salud_enemiga=salud_enemiga-generador_daño
        print("heroe esta atacando daño causa es:",generador_daño)
        print("vida restante del enemigo es",ataque)
    elif accion == habilidad:
        habilidad=salud_enemiga-daño_habilidad
        print("el heroe esta usando su habilidad daño causado es",daño_habilidad)
        print("vida restante del enemigo es:",habilidad)
    elif accion ==pocion:
        pocion=salud_heroe+cura
        print("el heroe esta usando una pocion se cura",cura)
        print("salud restante del heroe es :",pocion)
    else:
        print("el jugador debe elegir una de las opciones")

turn_jugador(ataque="ataque",habilidad="habilidad",pocion="pocion")
    




    