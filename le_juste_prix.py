# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:32:28 2019

@author: utilisateur
"""

from random import randint

entier = randint(1,1000)


print("Bienvenue dans l'émission intitulée : LE JUSTE PRIX")


for nb_essais in range(1,11):
    print("Il vous reste", 11-nb_essais,"essais(s).")
    entree = int(input("Entrez un prix :\n"))
    if nb_essais !=10:
        if entree < entier : 
            print ("C'est plus !")
        elif entree > entier : 
            print("C'est moins !")
        else:
            break
    
'''On vérifie ici la contion de victoire '''
if entree != entier :
    print("C'est perdu ! le juste prix était :",entier,"!")
else:
    print("C'est gagné !")

print("Merci d'avoir participé ! A bientôt dans le juste prix !")


