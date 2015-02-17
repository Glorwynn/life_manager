import pickle

from consts import *
from life import *
from day import *


class Application():
    def __init__(self,):
        self.life = None

    def mainMenu(self):
        menu_choices = [(fr.MAIN_MENU_NEW_FILE, self.newFileMenu),
                        (fr.MAIN_MENU_OPEN_FILE, self.openFileMenu),
                        (fr.MAIN_MENU_SAVE_FILE, self.saveFileMenu),
                        (fr.MAIN_MENU_ACCESS_FILE, self.accessLife),
                        (fr.MAIN_MENU_QUIT_APP, exit)
                        ]

        utils.menu(menu_choices, "main")

    def newFileMenu(self):
        req = input(fr.FILE_QUESTION)
        req_name = input(fr.NEW_LIFE_NAME_QUESTION)

        req_weight = Weight.ask()

        isOk = False
        while not isOk:
            try:
                req_cash = float(input(fr.NEW_LIFE_CASH_QUESTION))

            except ValueError:
                print(fr.INPUT_VALUE_ERROR)

            else:
                isOk = True

        self.life = Life(req_name, req_weight, req_cash)
        file_cl = open("saves/{}.lfm".format(req), "wb")
        pickle.dump(self.life, file_cl)

        self.life.menu()

    def openFileMenu(self):
        isOk = False
        while not isOk:
            req = input(fr.FILE_QUESTION)
            try:
                self.life = pickle.load(open("saves/{}.lfm".format(req), "rb"))
            except FileNotFoundError:
                print(fr.INPUT_FILE_NOT_FOUND_ERROR)
            else:
                isOk = True

        self.life.menu()

    def saveFileMenu(self):
        req = input(fr.FILE_QUESTION)
        pickle.dump(self.life, open("saves/{}.lfm".format(req), "wb"))

    def accessLife(self):
        try:
            if not self.life:
                raise(AttributeError)
            self.life.menu()

        except AttributeError:
            print(fr.NO_LIFE_ERROR)
