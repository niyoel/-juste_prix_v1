from random import randint
print(" ----------------------------")
print("| bienvenue sur notre plateau |")
print(" ----------------------------")
print("")
print("choisir un mode de difficulté parmis les modes suivants:","F pour le mode facile","N pour le mode normale","P pour le mode personnalisé",sep="\n")
mode=input("-")
if mode=="F":
        juste_prix=randint(1,100)
        # print(juste_prix)
        while True:
            prix_devine=int(input("devine le prix d'un objet entre 1 et 100: "))
            if prix_devine < juste_prix:
                print("c'est plus")
            elif prix_devine > juste_prix:
                print("c'est moins ")
            else: 
                print(f"Félicitation vous avez gagne le prix d'un objet  {juste_prix}")
                exit()
if mode=="N":
    juste_prix=randint(1,100)
print(juste_prix)
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
            
if mode=="P":
   print ("ecrire mx pour  choisir le prix maximale que tu peux devine","nbr pour le nombre d'essais que tu veux", sep="\n")
   choix=input("-")
   if choix=="max":
        max=input("choisissez la limite de prix")
        juste_prix=randint(1,max)
        while True:
            prix_devine=int(input("devine le prix d'un objet entre 1 et 100: "))
            if prix_devine < juste_prix:
                print("c'est plus")
            elif prix_devine > juste_prix:
                print("c'est moins ")
            else: 
                print(f"Félicitation vous avez gagne le prix d'un objet  {justPrix}")
                exit()
   if choix=="nbr":
        nombre=input("entre le nombre de prix: ")
        juste_prix=randint(1,nombre)
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
                    
        