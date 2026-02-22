# method 1
import alchemy.elements

#method 2 & 4
from alchemy.elements import create_water, create_fire, create_earth

#method 3
from alchemy.potions import healing_potion as heal, strength_potion


def ft_import_transmutation():
    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}\n")

    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}")

    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")

    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}\n")

    print("All import transmutation methods mastered!")

if __name__ == '__main__':
    ft_import_transmutation()
