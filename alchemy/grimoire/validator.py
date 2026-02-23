def validate_ingredients(ingredients: str) -> str:
    element_arr = ingredients.split(" ")
    flag = 0

    elements = "air water fire earth"
    for e in element_arr:
        if e in elements:
            pass
        else:
            flag = 1
    if flag == 1:
        return f"{ingredients} - INVALID"
    if flag == 0:
        return f"{ingredients} - VALID"
