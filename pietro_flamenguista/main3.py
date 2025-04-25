from infos import *

while True:
    print("Bem vindo!")
    print("Escolha a sua classe!")
    print("[1] - Mago | [2] - Guerreiro")

    classe = input("Your answer: ")

    if classe == "1":
        print("You chose to be a wizard")
        print("What will your name be? ")
        classe = class_mage
        nome = input("Your answer: ")
    else:
        print("You chose to be a warrior")
        print("What will your name be? ")
        classe = class_warrior
        nome = input("Your answer: ")

    print("Welcome", nome)

    print("Tell us which map you would like to explore: ")
    print(
        "*******[1] - Floresta dos Elfos | [2] - Deserto dos Assassinos | [3] - Esgoto dos Crocodilos"
    )
    local = input("Your answer: ")

    if local == "1":
        print("Welcome to Forest of the Elves")
        print("You will face *****Guardian_Comrronpido")

        print("É sua vez de atacar:")
        print("[1] - Ataque normal - [2] - Ataque Magic")
        atack = input("Your answer:")

        if atack == "1":
            print("The life of monster is this: ", forest["life"] - classe["attack"])
        else:
            print(
                "The life of monster is this: ",
                forest["life"] - classe["magic"] * classe["spell"]["hit"],
            )

    elif local == "2":
        print("Welcome  to Desert of the Assassins")
        print("You will face Verme_tempsareia")
    else:
        print("Welcome to Sewer of the Crocodiles")
        print("You will face Crocodile ")

    break
