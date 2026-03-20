import random
print("The Game.")
salud_enemiga=100
salud_heroe=100
pociones=3
game=False
#funcion de de turno del jugador
def turn_jugador(salud_heroe,salud_enemiga,pocion):
    generador_daño=random.randint(10,25)
    daño_habilidad=random.randint(30,50)
    cura=20
    accion = input("turno del jugar (ataque,habilidad,pocion)")
    if accion==ataque:
        ataque=salud_enemiga-generador_daño
        print("heroe esta atacando daño causa es:",generador_daño)
        print("vida restante del enemigo es",ataque)
    elif accion == habilidad:
        probalidad_acetar= random.randint(1,2)
        if probalidad_acetar==1:
            habilidad=salud_enemiga-daño_habilidad
            print("el heroe esta usando su habilidad daño causado es",daño_habilidad)
            print("vida restante del enemigo es:",habilidad)
        else:
            print("el heroe fallo la avilidad")
    elif accion ==pocion:
        if pociones> 0:
            pocion=salud_heroe+cura
            pociones-=1
            print("el heroe esta usando una pocion se cura",cura)
            print("salud restante del heroe es :",pocion)
        else:
            print("no hay pociones disponibles")
    else:
        print("el jugador debe elegir una de las opciones")
    return salud_heroe ,salud_enemiga,pocion
    
turn_jugador(ataque="ataque",habilidad="habilidad",pocion="pocion")
    
def turn_enemigo (salud_heroe):
    daño_enemigo=random.randint(15,20)
    vida_restante= salud_heroe - daño_enemigo
    print("el enemigo ataca daño recibi es:",daño_enemigo)
    print("salud restante del heroe es:",vida_restante)
    return vida_restante

def resultado(hp_h,hp_e):
    if hp_e<=0:
        print("You win")
        game=True
    elif hp_h<=0:
        print("You lose")
        game=True

fin = resultado(salud_heroe, salud_enemiga)

if fin:
    print("Juego terminado")
while not game:  # 👈 importante
    print("Star")

    if salud_heroe <= 0 or salud_enemiga <= 0: