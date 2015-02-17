from consts import *
from wallet import *
from weight import *


class Life:
    def __init__(self, name, weight, cash):
        self.name = name
        self.wallet = Wallet(cash)
        self.weight = Weight(weight)

    def __str__(self):
        return(fr.LIFE_INFOS.format(self.name, self.weight.current_value, self.wallet.cash))

    def quit(self):
        pass

    def display(self):
        print(self)

    def menu(self):
        print(self)

        menu_choices = [(fr.LIFE_MENU_PRINT_INFOS, self.display),
                        (fr.LIFE_MENU_MANAGE_WEIGHT, self.weight.menu),
                        (fr.LIFE_MENU_MANAGE_WALLET, self.wallet.menu),
                        (fr.LIFE_MENU_RETURN, self.quit)
                        ]

        utils.menu(menu_choices, "life")
