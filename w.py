import time

smiley = [
    "    😊😊   ",
    "  😊    😊  ",
    " 😊      😊 ",
    " 😊      😊 ",
    "  😊    😊  ",
    "    😊😊   "
]

def clear_screen():
    print("\033c", end="")

def display_smiley(smiley):
    for row in smiley:
        print(row)
    print()
    time.sleep(0.2)

def move_smiley(smiley, distance):
    clear_screen()
    for row in smiley:
        print(" " * distance + row)
    print()

distance = 0
while distance < 40:
    move_smiley(smiley, distance)
    distance += 1

clear_screen()