class Monster:
    def __init__(self, name, level, stats):
        self.name = name
        self.level = level
        self.stats = stats
    
    def display_enemy(self):
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"""Stats:
            HP: {self.stats['HP']}
            STR: {self.stats['STR']}
            AGI: {self.stats['AGI']}
            INT: {self.stats['INT']}
            """)