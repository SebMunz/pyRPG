from character import create_char
from monsters import Slime, Fungus

def main():
    player = create_char()
    print("-------------------------------")
    slime = Slime()
    print(f"Name: {slime.name}")
    print(f"Stats: {slime.stats}")
    fungus = Fungus()
    print(f"Name: {fungus.name}")
    print(f"Stats: {fungus.stats}")
    
    
if __name__ == "__main__":
    main()