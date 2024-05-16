# pseudo-code :
#
# modifier json avec camelia
# parser json en python ✅
# faire une boucle for pour déterminer le nombre de camélia : méthode count() ?
# méthode sort() pour classer les camélias (si pertinent car pas de poids ; mais par nom ?)

# class Camelia:
#   def __init__(self, nom, couleur):
#     self.camelia_name = nom
#     self.camelia_color = couleur


# Étape 1 : - Combien y’a-t-il de Pokemon dans les données ?
# Étape 2 : - Quels sont ceux dont le poids est supérieur à 10 kg ?
#           - Ecrire une fonction qui permet de les classer par ordre croissant de poids et afficher le résultat.
# Étape 3 : - programmation orienté objet


# Étape 3
class Pokemon:
  def __init__(self, name, weight, height):
    self.name = name
    self.weight = weight
    self.height = height

  def pop(self):
    print(f'This {self.name}, appear in the world with {self.weight} kg')
    print('Attrapez-les tous !')

import json

with open('pokedex.json') as p:
# pokedex = p.read()                               # permet de lire le fichier JSON
  pokedex = json.load(p)                           # charge le json en dictionnaire
  list_pokemon = pokedex['pokemon']                # selectionne dans la liste l’objet 'pokemon'
  count = len(list_pokemon)                        # compter le nombre de pokemon de l’objet 'pokemon' dans pokedex.json
  #print(count)
  
  for element in list_pokemon:
    if element['weight'] == '122.0 kg':
      print(element['name'])

#print(type(pokedex))
print(type(list_pokemon))

# # étape 2
# import json

# with open('pokedex.json') as p:
# # pokedex = p.read()                               # permet de lire le fichier JSON
#   pokedex = json.load(p)                           # charge le json et le transforme en dictionnaire
#   list_pokemon = pokedex['pokemon']                # selectionne dans la liste l’objet 'pokemon'
#   count = len(list_pokemon)                        # compter le nombre de pokemon de l’objet 'pokemon' dans pokedex.json
#   #print(count)
  
#   for element in list_pokemon:
#     if element['weight'] == '122.0 kg':
#       print(element['name'])

# #print(type(pokedex))
# print(type(list_pokemon))


# # étape 1
# import json

# with open('pokedex.json') as p:
# # pokedex = p.read()                               # permet de lire le fichier JSON
#   pokedex = json.load(p)                           # charge le json et le transforme en dictionnaire
#   tableau_pokemon = pokedex['pokemon']             # selectionne dans la liste l’objet 'pokemon'
#  # print(tableau_pokemon)
#   count = len(tableau_pokemon)                     # compter le nombre de pokemon de l’objet 'pokemon' dans pokedex.json

# print(count)
# print(type(pokedex))
# print(type(tableau_pokemon))