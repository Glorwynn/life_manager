import re

from datetime import date

from consts import *


class Day(date):
    nb_to_str = {1: fr.JAN, 2: fr.FEB, 3: fr.MAR, 4: fr.APR, 5: fr.MAY, 6: fr.JUN,
                 7: fr.JUL, 8: fr.AUG, 9: fr.SEP, 10: fr.OCT, 11: fr.NOV, 12: fr.DEC}

    def __init__(self, year, month, day):
        date.__init__(year, month, day)

    def __str__(self):
        return("{} {} {}".format(self.day, Day.nb_to_str[self.month], self.year))

    @staticmethod
    def ask():
        isOk = False
        pattern = re.compile(r'^../../....$')
        while not isOk:
            try:
                day = input(fr.NEW_DAY_QUESTION)
                if not pattern.search(day):
                    raise(ValueError)

            except ValueError:
                print(fr.INPUT_DATE_VALUE_ERROR)

            else:
                isOk = True

        date = day.split("/")
        for i in range(len(date)):
            date[i] = int(date[i])

        req_day = Day(date[2], date[1], date[0])

        return(req_day)
