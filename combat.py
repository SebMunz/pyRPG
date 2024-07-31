TODO: implementar lógica


from .monsters.bestiary import *
from character import Character

def combat(character, monster):
    while PERSONAJE HP > 0 Y ENEMIGO HP > 0:
        # Turno personaje
        DAÑO SERA = PERSONAJE DMG
        ENEMIGO HP -= DAÑO
        if ENEMIGO HP <= 0:
            break #terminar combate
        
        # Turno enemigo
            DAÑO ENEMIGO SERA = ENEMIGO DMG
            PERSONAJE HP -= DAÑO ENEMIGO
        if PERSONAJE HP <= 0:
            break #terminar combate
        
        if PERSONAJE HP > 0 ganar
        else ENEMIGO GANA
