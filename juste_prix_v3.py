
from ast import If, While
from random import randint
from tkinter import N, Y

print(" ----------------------------")
print("| bienvenue sur notre plateau |")
print(" ----------------------------")
print("")

# Fonction pour mode facile
def mode_facile():
    juste_prix=randint(1,100)
    while True:
            prix_devine=int(input("Devinez le prix d'un objet entre 1 et 100: "))
            if prix_devine < juste_prix:
                print("C'est plus")
            elif prix_devine > juste_prix:
                print("C'est moins ")
            else: 
                print(f"Félicitation vous avez gagne! Le prix d'un objet est {juste_prix}")
                return 0 #arrêt de la boucle while 
                   
# Fonction pour mode normal
def mode_normal():
        juste_prix=randint(1,100)
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
            elif prix_devine == juste_prix:
                print(f"Félicitations vous avez gagne  à la {loop_count}éme essais! Le juste prix est: {juste_prix}")
                return 0 #arrêt de la boucle while 
        
        print(f"La partie est terminée. Vous avez echoué! Le prix est:{juste_prix} ")
# Fonction pour mode personalise       
def mode_personalise():
    print ("Entrez mx pour choisir le prix maximale que vous pouvez devinez","nbr pour le nombre d'essais que vous voulais", sep="\n")
    choix=str(input("-"))
    if choix=="mx":
                max= int(input("Choisissez le prix maximal d'un objet: "))
                juste_prix=randint(1,max)
                while True:
                    prix_devine=int(input(f"Devinez le prix d'un objet entre 1 et {max}: "))
                    if prix_devine < juste_prix:
                        print("c'est plus")
                    elif prix_devine > juste_prix:
                        print("c'est moins ")
                    else: 
                        print(f"Félicitation vous avez gagne! Le prix d'un objet est {juste_prix}")
                        return 0 #arrêt de la boucle while 
    if choix=="nbr":
            nombre=int(input("Choisissez le nombre d'essais que vous voulais: "))
            if nombre==0:
                juste_prix=randint(1,100)
                while True:
                    prix_devine=int(input("Devinez le prix d'un objet entre 1 et 100: "))
                    if prix_devine < juste_prix:
                        print("C'est plus")
                    elif prix_devine > juste_prix:
                        print("C'est moins ")
                    else: 
                        print(f"Félicitation vous avez gagne! Le prix d'un objet est {juste_prix}")
                        return 0 #arrêt de la boucle while 
            else:
                juste_prix=randint(1,100)
                loop_count=1
                essais_count=nombre-1
                while loop_count<= nombre:
                        prix_devine=int(input(f"Devinez le prix d'un objet entre 1 et 100. Attention! Vous avez {essais_count+1} essais seulement: "))
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
                            return 0 #arrêt de la boucle while 
                print(f"La partie est terminée. Vous avez echoué! Le prix est:{juste_prix} ")
                
# Fonction de modes 
def mode():
    print("Choisissez un mode de difficulté parmis les modes suivants:","F pour le mode facile","N pour le mode normale","P pour le mode personnalisé",sep="\n")
    mode=str(input("-"))
    if mode=="F":
        mode_facile()
    if mode=="N":
       mode_normal()
    if mode=="P":
       mode_personalise()
mode()
# relence l'application 
while True:
    re_load=input("voulez-vous encore jouer? (Y) pour oui (N) pour non ")
    if re_load=="N":
           exit()
    if re_load=="Y":
        if __name__ == "__main__":
            mode()






        

        

               