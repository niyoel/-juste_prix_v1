
from random import randint
juste_prix=randint(1,100)
# print(juste_prix)
print(" ----------------------------")
print("| Bienvenue sur notre plateau |")
print(" ----------------------------")
print("")
loop_count=1
essais_count=9
while loop_count<=10:
        prix_devine=int(input(f"Devinez le prix d'un objet entre 1 et 100. Attention! Vous avez {essais_count+1} seulement: "))
        if prix_devine < juste_prix:
            print("C'est plus")
            loop_count=loop_count+1
            essais_count=essais_count-1
        elif prix_devine > juste_prix:
            print("C'est moins")
            loop_count=loop_count+1
            essais_count=essais_count-1
        else:
            print(f"Félicitations vous avez gagne  à la {loop_count}éme essais  le juste prix est: {juste_prix}")
            exit()
print(f"La partie est terminée. Vous avez echoué! Le prix est:{juste_prix} ")
            
 
