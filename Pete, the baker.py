def cakes(recipe, available):
    min = float('inf')
    for k_recipe in sorted(recipe):
        # if required ingredient isn't in available ones, we cannot cook a dish
        if k_recipe not in available:
            return 0
        if available[k_recipe]//recipe[k_recipe] < min:
            min = available[k_recipe]//recipe[k_recipe]
    return min