https://github.com/aalhaidary/asg-9.git

from random import randint

shipboard = []

for x in range(5):
    shipboard.append(["O"] * 5)

def print_shipboard(shipboard):
    for row in shipboard:
        print " ".join(row)


print "start Battleship"
print_shipboard(shipboard)


def random_row(shipboard):
    return randint(0, len(shipboard) - 1)

def random_coll(shipboard):
    return randint(0, len(shipboard[0]) - 1)

ship_row = random_row(shipboard)
ship_coll = random_coll(shipboard)


for turn in range(4):
    guess_row = int(raw_input("Row:"))
    guess_coll = int(raw_input("Coll:"))


    if guess_row == ship_row and guess_coll == ship_coll:
        print "you win"
        break
    else:
        
        if (guess_row < 0 or guess_row > 4) or (guess_coll < 0 or guess_coll > 4):
            print "not on the board"
        
    
        elif(shipboard[guess_row][guess_coll] == "X"):
            print "You guessed that one already."
        

        else:
            print "You missed my battleship!"
            shipboard[guess_row][guess_coll] = "X"
        

        print "Turn " + str(turn+1) + " out of 4." 
        print_shipboard(shipboard)


if turn >= 3:
    print "you lose"
