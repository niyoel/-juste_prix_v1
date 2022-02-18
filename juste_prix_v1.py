
from random import randint


justPrix=randint(1,100)
print(justPrix)
print(" ----------------------------")
print("| bienvenue sur notre plateau |")
print(" ----------------------------")
print("")
while True:
    prix_devine=int(input("devine le prix d'un objet entre 1 et 100: "))
    if prix_devine < justPrix:
        print("c'est plus")
    elif prix_devine > justPrix:
        print("c'est moins ")
    else: 
        print(f"Félicitation vous avez gagne le prix d'un objet  {justPrix}")
        exit()
from random import randint


