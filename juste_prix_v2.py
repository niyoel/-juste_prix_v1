from random import randint
from turtle import clear
juste_prix=randint(1,100)
print(juste_prix)
print(" ----------------------------")
print("| bienvenue sur notre plateau |")
print(" ----------------------------")
print("")
i=1
j=9
while i<=10:
        prix_devine=int(input("devine le prix d'un objet entre 1 et 100, attention! vous avez 10 essais seulement "))
        if prix_devine < juste_prix:
            print(f"c'est plus, vous avez encore {j} essais" )
            i=i+1
            j=j-1
        elif prix_devine > juste_prix:
            print(f"c'est moins, vous avez encore {j} essais")
            i=i+1
            j=j-1
        else:
            print(f"Félicitation vous avez gagne  à la {i}éme essais  le juste prix est: {juste_prix}")
            exit()
    
print(f"partie est terminée vous avez echoué le prix est:{juste_prix} ")
            
 
