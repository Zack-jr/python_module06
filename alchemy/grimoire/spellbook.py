def record_spell(spell_name: str, ingredients : str) -> str
    from .validatoir import validate_ingredients
    validation_result = validate_ingredients(str)

    if "INVALID" in validation_result:
        return f"Spell rejected: {validation_result}"
    else
        return f"Spell recorded: {validation_result}"