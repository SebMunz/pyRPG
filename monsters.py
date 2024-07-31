class Monster:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.calculate_monster_stats()
        self.skills = None

    def calculate_monster_stats(self):
        self.stats['DMG'] = round((self.stats['STR']*0.1) + (self.stats['AGI']*0.05))
        self.stats['HIT'] = round((self.stats['STR']*0.05) + (self.stats['AGI']*0.1))
        self.stats['EVA'] = round((self.stats['AGI']*0.1) + (self.stats['INT']*0.05))
        self.stats['MGDMG'] = round((self.stats['INT']*0.2))

class Slime(Monster):
    def __init__(self):
        stats = {'STR': 5,
                    'AGI': 3,
                    'INT': 1,
                    'HP': 20,
                }
        super().__init__("Slime", stats)

class Fungus(Monster):
    def __init__(self):
        stats = {'STR': 2,
                    'AGI': 4,
                    'INT': 5,
                    'HP': 15
                }
        super().__init__("Fungus", stats)