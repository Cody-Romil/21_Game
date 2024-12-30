import random
import os

class Game_21():
    def __init__(self):
        os.system("cls")
        self.not_disqualified = True
        self.num_list = []
        self._mainloop()

    def _mainloop(self):
        self.chance_no = input("Do you want to start first or second (F/S): ").lower()
        if self.chance_no == "f":
            print("You will play first.")
        elif self.chance_no == "s":
            print("Computer will play first. You will play second.")
        else:
            print("Invalid input, Please Try Again!")

        while self.not_disqualified:
            break


if __name__=="__main__":
    Game_21()