import random
import sys

try_again = 5
secret_number = str(random.randint(0, 100))

print("*** Le jeu du nombre mystère ***")
while try_again > 0:
    print(f"Il te reste {try_again} essai{'s' if try_again > 1 else ''}")
    user_number = input("Devine le nombre : ")
    if user_number.isdigit():
        try_again -= 1

        if (user_number > secret_number):
            print(f"Le nombre mystère est plus petit que {user_number}")
        elif (user_number < secret_number):
            print(f"Le nombre mystère est plus grand que {user_number}")
        else:
            print(f"Bravo ! Le nombre mystère était bien {secret_number} !")
            print(f"Tu as trouvé en {5 - try_again} essai{'s' if 5 - try_again > 1 else ''}")
            sys.exit()
    else:
        print("Veuillez entrer un nombre valide.")

print(f"Dommage le nombre mystère était {secret_number}")
print("Fin du jeu.")
sys.exit()
