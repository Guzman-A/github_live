import random

range = input("Starting range: ")
range2 = input("Ending range: ")
rand_number = random.randint(int(range), int(range2))

print("Starting from {} and Ending at {}".format(range, range2))

print("Random Number: {}".format(rand_number))
