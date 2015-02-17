from consts import *
from application import *


def printGreetings():
    print(fr.GREETING)


def main():
    printGreetings()

    app = Application()
    app.mainMenu()

main()
