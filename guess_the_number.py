import random





class BluePrint():

    def game(self, user_guess, again):
        self.user_guess = user_guess
        self.again = again

        x = random.randint(1,10)

        if(int(user_guess) == x):
            print("You Mind Reading Son Of Gun!")
            print("Computer guessed {}".format(x))

        else:
            print("Computer guessed {}".format(x))
            print("Care to try again Partner!? : (Y/N)")

            again = input()

            if(again == 'Y'):
                main()




            else:
                print("Ya QUITTER!")





def main():
    again = None

    instance = BluePrint()
    user_guess = input("Guess a number from 1 - 10: ")
    instance.game(user_guess, again)


if __name__ == "__main__":
    main()
