
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
        print("votre prix est inferieur que le juste prix")
    elif prixDevine > justPrix:
        print("votre prix est superieur que l juste prix")
    else: 
        print(f"felicitation vous avez gagne le prix d'un objet est {justPrix}")
        exit()
from random import randint


