
from random import randint


justPrix=randint(1,100)
print(justPrix)
print(" ----------------------------")
print("| bienvenue sur notre plateau |")
print(" ----------------------------")
print("")
while True:
    prixDevine=int(input("devine le prix d'un objet entre 1 et 100: "))
    if prixDevine < justPrix:
        print("C’est moins")
    elif prixDevine > justPrix:
        print("c'est plus")
    else: 
        print(f"felicitation vous avez gagne le prix d'un objet est {justPrix}")

from random import randint


