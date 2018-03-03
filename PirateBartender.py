#Pirate Bartendar Project

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

from random import randint

#Inquire with customers
def inquirecust():
    for keys, values in questions.items():
        answer=input(values)
        if answer.lower() == "yes":
            for tastes in ingredients[keys]:
                print("Thank ye. I will give ye a '", ingredients[keys][randint(0, len(ingredients[keys])) -1], "'.")
                break
        else:
            continue
        
#Implementation
inquirecust()