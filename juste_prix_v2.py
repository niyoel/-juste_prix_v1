<<<<<<< HEAD
from random import randint
from turtle import clear
juste_prix=randint(1,100)
print(juste_prix)
print(" ----------------------------")
print("| Bienvenue sur notre plateau |")
print(" ----------------------------")
print("")
i=1
j=9
while i<=10:
        prix_devine=int(input("Devinez le prix d'un objet entre 1 et 100. Attention! Vous avez 10 essais seulement "))
        if prix_devine < juste_prix:
            print(f"C'est plus, vous avez encore {j} essais" )
            i=i+1
            j=j-1
        elif prix_devine > juste_prix:
            print(f"C'est moins, vous avez encore {j} essais")
            i=i+1
            j=j-1
        else:
            print(f"Félicitations vous avez gagne  à la {i}éme essais  le juste prix est: {juste_prix}")
            exit()
    
print(f"La partie est terminée. Vous avez echoué! Le prix est:{juste_prix} ")
            
 
=======
from random import randint
from turtle import clear
juste_prix=randint(1,100)
print(juste_prix)
print(" ----------------------------")
print("| Bienvenue sur notre plateau |")
print(" ----------------------------")
print("")
i=1
j=9
while i<=10:
        prix_devine=int(input("Devinez le prix d'un objet entre 1 et 100. Attention! Vous avez 10 essais seulement "))
        if prix_devine < juste_prix:
            print(f"C'est plus, vous avez encore {j} essais" )
            i=i+1
            j=j-1
        elif prix_devine > juste_prix:
            print(f"C'est moins, vous avez encore {j} essais")
            i=i+1
            j=j-1
        else:
            print(f"Félicitations vous avez gagne  à la {i}éme essais  le juste prix est: {juste_prix}")
            exit()
    
print(f"La partie est terminée. Vous avez echoué! Le prix est:{juste_prix} ")
            
 
>>>>>>> 8987bb1d99dcea7ba70f1c8a41cb31e63a85378e
