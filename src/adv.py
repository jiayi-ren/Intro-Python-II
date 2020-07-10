import sys
import os
from room import Room
from player import Player
from item import Item

rock = Item("Rock", "a small rock than can be thrown")
stick = Item("Stick", "a piece of wood stick, easy to break")
crystal = Item("Crystal", "shiny crystal")
empty_backpack = Item("Backpack", "empty backpack from earlier adventurers")
sword = Item("Sword", "rusty sword")
coins = Item("Coins", "unknown coins")


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [rock, stick]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [rock, stick, empty_backpack]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [rock, crystal]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [rock, coins]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [sword]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# os.system('cls')
possible_directions = ['n', 's', 'e', 'w', 'i']
# Make a new player object that is currently in the 'outside' room.
player = Player(input("Please enter your name:"), room['outside'])
# os.system('cls')
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


show_special = False

player_command = None

while True:

    if show_special is True:
        print(f"{player.show_items()}")
    else:
        pass

    print(f"Your location: {player.current_room}\n")

    def command():
        global player_command
        print("***Enter a command to continue***\
            \n q: quit\
            \n i: show your items\
            \n n: go North\
            \n s: go South\
            \n e: go East\
            \n w: go West\
            \n g [item]: get item\
            \n d [item]: drop item")
        player_command = input(">> ")

    command()

    if player_command == 'q':
        print("See you back soon")
        sys.exit(1)
    elif player_command == 'i':
        show_special = True
    elif player_command[0] == 'g':
        show_special = False
        player.get_item(player_command[2:].lower())
    elif player_command[0] == 'd':
        show_special = False
        player.drop_item(player_command[2:].lower())
    elif player_command in possible_directions:
        show_special = False
        player.try_direction(player_command)
    else:
        show_special = False
        print("I don't understand your command. Try again\n")

