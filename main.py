import random

# Bonjour et bienvenue dans ce jeu de pierre-papier-ciseaux
# Author: @Anna-el
# Licence: MIT
# Language: Python
# email: aerabenadrasana@gmail.com

life = 10
computerWin = 0
userWin = 0

print("\tBonjour et bienvenue dans ce jeu de pierre-papier-ciseaux\n")
print("\t\tveuillez choisir entre pierre, papier ou ciseaux\n")
print("\t\t\tpierre = r, papier = p, ciseaux = c\n")

while (life>0):
    print(f"\n[Vous avez {life} Tentative, {computerWin} victoires de l'ordinateur et {userWin} victoires de l'utilisateur]\n")
    life -= 1
    userInput = input("Votre choix: ")
    print("")
    userInput = userInput.lower()
    computerInput = random.choice(["r", "p", "c"])
    
    if userInput == "q":
        print("Merci d'avoir joué, à bientôt...!!!")
        break
    elif userInput == computerInput:
        print("Egalité")
    elif userInput == "r" and computerInput == "p":
        print("La machine Gagne et Vous avez perdu...!!!")
        computerWin += 1
    elif userInput == "r" and computerInput == "c":
        print("Vous avez gagné...!!!")
        userWin += 1
    elif userInput == "p" and computerInput == "r":
        print("Vous avez gagné...!!!")
        userWin += 1
    elif userInput == "p" and computerInput == "c":
        print("La machine Gagne et Vous avez perdu...!!!")
        computerWin += 1
    elif userInput == "c" and computerInput == "r":
        print("La machine Gagne et Vous avez perdu...!!!")
        computerWin += 1
    elif userInput == "c" and computerInput == "p":
        print("Vous avez gagné...!!!")
        userWin += 1
    else:
        print("Veuillez entrer une valeur valide, r pour pierre, p pour papier et c pour ciseaux")

print(f"\nScore de la machine {computerWin}\n Votre score {userWin}") 