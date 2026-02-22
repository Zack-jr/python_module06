def validate_ingredients(ingredients : str) -> str:
    valid = ["fire", "water", "earth", "air"]

    if ingredients in valid:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"

if __name__ == '__main__':
    print(validate_ingredients("salope"))