print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroad = input("you're at a crossroad, where do you want to go? Type \"left\" or \"right\".").lower()
lake = input("you've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swijm across.").lower()
door = input("you arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?").lower()

if crossroad == 'left':
    if lake == 'wait':
        if door == 'yellow':
            print("you found the treasure! You win!")
            #treasure pic
        else: print("failed")
    else: print("failed")
else: print("failed")