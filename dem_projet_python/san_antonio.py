# -*- coding: utf8 -*-

import random

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks",
    "Babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "Kirikou"
]



def get_random_item_in(my_list):
    rand_numb = random.randint(0,len(my_list)-1)
    item = my_list[rand_numb]
    user_answer = input("Tapez entrée pour découvrir une autre citation ou B pour quitter le prgrm.")

    while user_answer != 'B':
        print(item)
        return (get_random_item_in(quotes))



    return "prgrm is over"


print("{} a dit : {}".format("Babar", "Tout n'est pas cirose"))

print(get_random_item_in(quotes))
