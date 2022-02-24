
from random import randint


juste_prix=randint(1,100)
# print(juste_prix)
print(" ----------------------------")
print("| bienvenue sur notre plateau |")
print(" ----------------------------")
print("")
while True:
    prix_devine=int(input("devine le prix d'un objet entre 1 et 100: "))
    if prix_devine < juste_prix:
        print("c'est plus")
    elif prix_devine > juste_prix:
        print("c'est moins ")
    else: 
        print(f"Félicitation vous avez gagne le prix d'un objet  {juste_prix}")
        exit()
from random import randint


