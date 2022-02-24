from random import randint
print(" ----------------------------")
print("| bienvenue sur notre plateau |")
print(" ----------------------------")
print("")
print("Choisissez un mode de difficulté parmis les modes suivants:","F pour le mode facile","N pour le mode normale","P pour le mode personnalisé",sep="\n")
mode=str(input("-"))
if mode=="F":
    juste_prix=randint(1,100)
    # print(juste_prix)
    while True:
        prix_devine=int(input("Devinez le prix d'un objet entre 1 et 100: "))
        if prix_devine < juste_prix:
            print("C'est plus")
        elif prix_devine > juste_prix:
            print("C'est moins ")
        else: 
            print(f"Félicitation vous avez gagne! Le prix d'un objet  {juste_prix}")
            exit()
if mode=="N":
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
        else:
            print(f"Félicitations vous avez gagne  à la {loop_count}éme essais  le juste prix est: {juste_prix}")
            exit()
    print(f"La partie est terminée. Vous avez echoué! Le prix est:{juste_prix} ")
            
if mode=="P":
   print ("Entrez mx pour choisir le prix maximale que tu peux devine","nbr pour le nombre d'essais que tu veux", sep="\n")
   choix=str(input("-"))
   if choix=="mx":
        max= int(input("Choisissez la limite de prix: "))
        juste_prix=randint(1,max)
        while True:
            prix_devine=int(input(f"Devinez le prix d'un objet entre 1 et {max}: "))
            if prix_devine < juste_prix:
                print("c'est plus")
            elif prix_devine > juste_prix:
                print("c'est moins ")
            else: 
                print(f"Félicitation vous avez gagne le prix d'un objet  {juste_prix}")
                exit()
   if choix=="nbr":
        nombre=int(input("Choisissez le nombre d'essais: "))
        juste_prix=randint(1,100)
        loop_count=1
        essais_count=nombre-1
        while loop_count<= nombre:
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
                    print(f"Félicitations vous avez gagne  à la {loop_count}éme essais! Le juste prix est: {juste_prix}")
                    exit()
        print(f"La partie est terminée. Vous avez echoué! Le prix est:{juste_prix} ")
                    