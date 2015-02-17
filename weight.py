from consts import *
from day import *


class Weight:
    def __init__(self, current_value):
        self.current_value = current_value
        self.history = []

        today = Day.today()
        self.add(current_value, today)

    def __str__(self):
        return("{} kg".format(self.current_value))

    @staticmethod
    def ask():
        isOk = False
        while not isOk:
            try:
                req_weight = float(input(fr.NEW_WEIGHT_QUESTION))
                if req_weight < 0 or req_weight > 200:
                    raise(ValueError)

            except ValueError:
                print(fr.INPUT_WEIGHT_VALUE_ERROR)

            else:
                isOk = True
        return(req_weight)

    def add(self, weight, date):
        for record in self.history:
            if date in record:
                raise(ValueError)
        self.history += [(date, weight)]
        self.history = sorted(self.history)

    def delete(self, weight, date):
        pass

    def save(self):
        isOk = False
        while not isOk:
            req_weight = Weight.ask()
            req_day = Day.ask()
            try:
                self.add(req_weight, req_day)
            except ValueError:
                print(fr.INPUT_DATE_EXISTING_ERROR)
            else:
                isOk = True

    def remove(self):
        pass

    def quit(self):
        pass

    def display(self):
        print(fr.WEIGHT_INFOS.format(self))
        print(fr.SEPARATOR)
        for record in self.history:
            print("{} :  {} kg".format(*record))
        print(fr.SEPARATOR)

    def menu(self):
        menu_choices = [(fr.WEIGHT_MENU_PRINT_INFOS, self.display),
                        (fr.WEIGHT_MENU_ADD_ENTRY, self.save),
                        (fr.WEIGHT_MENU_REMOVE_ENTRY, self.remove),
                        (fr.WEIGHT_MENU_RETURN, self.quit)
                        ]

        utils.menu(menu_choices, "weight")
