import random

class Chooser():
    restaurant_list = []

    def append_restaurant(self, choice):
        self.restaurant_list.append(choice)

    def random_restaurant(self):
        x = random.randint(0,len(self.restaurant_list)-1)
        return self.restaurant_list[x]

def main():
    choice = None
    count = 0
    object2 = Chooser()

    while((choice != 'QUIT') & (count != 5)):
        choice = input("Insert Restaurant Name: ")
        object2.append_restaurant(choice)
        count += 1

    print(object2.random_restaurant())

if __name__ == "__main__":
    main()
