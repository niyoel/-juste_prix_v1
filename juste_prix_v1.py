from random import randint


justPrix=randint(1,100)
print(justPrix)
print(" ----------------------------")
print("| bienvenue sur notre plateu |")
print(" ----------------------------")
print("")
while True:
    prixDevine=int(input("devine la prix d'un objet: "))
    if type(prixDevine)!=int:
        print(" un nombre svp")
    elif prixDevine < justPrix:
        print("C’est moins")
    elif prixDevine > justPrix:
        print("c'est plus")
    else: 
        print(f"felicitation vous avez gagne! le prix d'un obje est {justPrix}")
        exit()
