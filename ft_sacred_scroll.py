import alchemy


def ft_sacred_scroll():

    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
        print(f"alchemy.create_water(): {alchemy.create_water()}")
        alchemy.create_earth()
        alchemy.create_air()
    except Exception as e:
        print(f"alchemy.create_earth(): {type(e).__name__} - not exposed")
        print(f"alchemy.create_air(): {type(e).__name__} - not exposed")

    print("\nPackage metadata:")
    print(alchemy.__version__)
    print(alchemy.__author__)


if __name__ == '__main__':
    ft_sacred_scroll()

# absolute imports = scanning from the root (import example)
# relative import = getting the file in the same directory as the import
# (import .example)
# structure: importing the alchemy package
# first using the functions without passing by the elemets module
# then using the functions by accessing them directly (passing by init)
