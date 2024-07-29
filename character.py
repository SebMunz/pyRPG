class Character:
    def __init__ (self, name, char_class): #Objeto inicial, __init__ inicializa la instancia del objeto con algunos atributos
        self.name = name    
        self.char_class = char_class
        self.stats = {'STR': 0, 'AGI': 0, 'INT': 0, 'HP': 0, 'DMG': 0,
                    'HIT': 0, 'EVA': 0, 'MGDMG': 0}
        self.skills = None
        self.set_initial_stats()
    
    """
    TODO: Mejorar sistema de stats.
    Stats por clase.
    Stats base: STR, AGI, INT.
    Stats expandir: HP, DAÑO, HIT, EVA, MGDMG.
    """
    
    def set_initial_stats(self):
        if self.char_class == "Warrior":
            self.stats['STR'] = 10
            self.stats['AGI'] = 7
            self.stats['INT'] = 3
            self.stats['HP'] = round(50 + self.stats['STR'] * 0.25)
            self.stats['DMG'] = round(self.stats['STR'] * 0.15)
            self.stats['HIT'] = round((self.stats['STR'] * 0.1) + (self.stats['AGI'] * 0.05) + (self.stats['INT'] * 0.05))
            self.stats['EVA'] = round((self.stats['AGI'] * 0.1) + (self.stats['INT'] * 0.05))
            self.stats['MGDMG'] = round(self.stats['INT'] * 0.2)
            self.skills = 'Bash'
        elif self.char_class == 'Thief':
            self.stats['STR'] = 7
            self.stats['AGI'] = 10
            self.stats['INT'] = 5
            self.stats['HP'] = round(50 + self.stats['STR'] * 0.2)
            self.stats['DMG'] = round((self.stats['STR']*0.1) + (self.stats['AGI'] * 0.1))
            self.stats['HIT'] = round((self.stats['STR']*0.05) + (self.stats['AGI'] * 0.15) + (self.stats['INT'] * 0.05))
            self.stats['EVA'] = round((self.stats['AGI'] * 0.15) + (self.stats['INT'] * 0.05))
            self.stats['MGDMG'] = round(self.stats['INT'] * 0.2)
            self.skills = 'Pilfer'
        elif self.char_class == 'Mage':
            self.stats['STR'] = 5
            self.stats['AGI'] = 5
            self.stats['INT'] = 10
            self.stats['HP'] = round(50 + self.stats['STR'] * 0.2)
            self.stats['DMG'] = round((self.stats['STR']*0.1) + (self.stats['AGI'] * 0.05))
            self.stats['HIT'] = round((self.stats['STR']*0.05) + (self.stats['AGI'] * 0.1) + (self.stats['INT'] * 0.1))
            self.stats['EVA'] = round((self.stats['AGI'] * 0.05) + (self.stats['INT'] * 0.1))
            self.stats['MGDMG'] = round(self.stats['INT'] * 0.25)
            self.skills = 'Fireball'
        else: print("Clase no válida")
    
    # mostrar datos personaje
    def display_character(self):
        print(f"""Your Character:
            Name: {self.name}
            Class: {self.char_class}
            Skills: {self.skills}
            """)
        print(f"""Stats:
            STR {self.stats['STR']}, the capacity to deal damage, sustain damage and to a lesser extent, Hit your target. 
            AGI {self.stats['AGI']}, how hard it is to hit you, how frecuently you hit your target. Also increase a little how much damage you do.
            INT {self.stats['INT']}, how intelligent you are. Greatly increases magical damage but it also influence your combat smarts a little (damage, hit, eva)
            HP {self.stats['HP']}, your life force. If it hits 0 it's game over.
            DMG {self.stats['DMG']}, how much damage you deal to your targets.
            HIT {self.stats['HIT']}, how frequently you hit.
            EVA {self.stats['EVA']}, how hard it is to hit you.
            MAGIC DAMAGE {self.stats['MGDMG']}, how much damage you deal with magical imbued weapons or magic.
            """)

# la creación
def create_char():
    name = input("Choose a name: ")
    print("Choose a class by its number:")
    print("""
        1.- Warrior. Main stat STR. Higher HP and DMG, most balanced.
        2.- Thief. Main stat AGI. Higher HIT and EVA, lower DMG and HP than warrior
        3.- Mage. Main stat INT. Higher magical DMG, strongest attack, lowest hp.
        """)
    class_choice = input("Selection: ")
    if class_choice == "1":
        char_class = 'Warrior'
    elif class_choice == "2":
        char_class = 'Thief'
    elif class_choice == "3":
        char_class = 'Mage'
    else: 
        print("Not a valid class. Follow the instructions clearly.")
        return create_char()
    
    character = Character(name, char_class) #variable character que es igual al objeto Character de la linea 1
    character.display_character() #llama función display_character para mostrar los datos del personaje
    return character