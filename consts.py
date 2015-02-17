class utils:
    @staticmethod
    def printHeader(title):
        decoration = "#" + "-"*(len(title)+2) + "#"
        print("\n" + decoration)
        print("| {} |".format(title))
        print(decoration)

    @staticmethod
    def menu(menu_choices, menu_type):
        req = 0
        while req != len(menu_choices):
            utils.printHeader(fr.MENU_INTRO[menu_type])
            for choice in menu_choices:
                print("{}. {}".format(menu_choices.index(choice)+1, choice[0]))

            try:
                req = int(input(fr.MENU_QUESTION))
                if req > len(menu_choices):
                    raise(ValueError)

            except ValueError:
                print(fr.INPUT_MENU_VALUE_ERROR)
                choice = 0

            else:
                res = menu_choices[req-1][1]
                res()


class fr:
    GREETING = "\n#------------------------------#\n  Bienvenue sur Life Manager !  \n#------------------------------#"
    SEPARATOR = "---------------------------"

    MENU_INTRO = {"main": "Menu principal",
                  "life": "Gérer son profil",
                  "weight": "Menu poids",
                  "money": "Menu argent",
                  }

    MENU_QUESTION = "\nEntrez le numéro de votre choix : "
    FILE_QUESTION = "\nEntrez le nom du fichier : "

    MAIN_MENU_NEW_FILE = "Créer un nouveau fichier"
    MAIN_MENU_OPEN_FILE = "Ouvrir un fichier existant"
    MAIN_MENU_SAVE_FILE = "Sauvegarder le fichier courant"
    MAIN_MENU_ACCESS_FILE = "Accéder au profil actuel"
    MAIN_MENU_QUIT_APP = "Quitter le programme"

    LIFE_INFOS = "\n-------------------\nProfil actuel :\n{}\nPoids : {} kg\nArgent : {} €\n-------------------"
    LIFE_MENU_PRINT_INFOS = "Afficher les informations sur le profil courant"
    LIFE_MENU_MANAGE_WEIGHT = "Gérer son poids"
    LIFE_MENU_MANAGE_WALLET = "Gérer son argent"
    LIFE_MENU_RETURN = "Retour au menu principal"

    NEW_LIFE_NAME_QUESTION = "\nEntrez le nom du profil : "
    NEW_LIFE_CASH_QUESTION = "\nEntrez le montant actuel de votre compte en banque (0 pour ignorer) : "

    WEIGHT_INFOS = "\nPoids actuel : {}"
    WEIGHT_HISTORY = "{} : {}"
    WEIGHT_MENU_PRINT_INFOS = "Afficher les informations sur votre poids"
    WEIGHT_MENU_ADD_ENTRY = "Enregistrer un nouveau poids"
    WEIGHT_MENU_REMOVE_ENTRY = "Supprimer un poids enregistré"
    WEIGHT_MENU_RETURN = "Retour au menu de profil"

    NEW_WEIGHT_QUESTION = "\nPoids : "
    NEW_DAY_QUESTION = "\nDate (JJ/MM/AAAA) : "

    INPUT_FILE_NOT_FOUND_ERROR = "\nFichier introuvable, veuillez entrer un nom de fichier valide !"
    INPUT_MENU_VALUE_ERROR = "\nVeuillez entrer un nombre parmi ceux proposés ci-dessus."
    INPUT_WEIGHT_VALUE_ERROR = "\nVeuillez entrer un nombre compris entre 0 et 200."
    INPUT_DATE_VALUE_ERROR = "\nVeuillez entrer une date au format JJ/MM/AAAA."
    INPUT_DATE_EXISTING_ERROR = "\nUn poids est déjà enregistré à cette date, veuillez le supprimer pour en sauver un nouveau."
    NO_LIFE_ERROR = "\nAucun profil n'est couramment sélectionnée."

    JAN = "Janvier"
    FEB = "Février"
    MAR = "Mars"
    APR = "Avril"
    MAY = "Mai"
    JUN = "Juin"
    JUL = "Juillet"
    AUG = "Août"
    SEP = "Septembre"
    OCT = "Octobre"
    NOV = "Novembre"
    DEC = "Décembre"
