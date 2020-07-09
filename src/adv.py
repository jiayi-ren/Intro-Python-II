import sys
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Make a new player object that is currently in the 'outside' room.
player = Player(input("Please enter your name:"), room['outside'])

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
print("\nWelcome to the adventure")
print(f"Hey {player.name}, you are {player.current_room}\n")

while True:


    player_command = None

    def command():
        global player_command
        print("***Enter a command to continue***\
            \n q: quit\
            \n n: go North\
            \n s: go South\
            \n e: go East\
            \n w: go West")
        player_command = input(">> ")

    command()

    if player_command == 'q':
        print("\nSee you back soon")
        sys.exit(1)

    elif player_command == 'n':
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
            print(f"\n{player}\n")
        else:
            print(f"Sorry {player.name}, no rooms to enter in the North\n")
    elif player_command == 's':
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
            print(f"\n{player}\n")
        else:
            print(f"Sorry {player.name}, no rooms to enter in the South\n")
    elif player_command == 'w':
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to
            print(f"\n{player}\n")
        else:
            print(f"Sorry {player.name}, no rooms to enter in the West\n")
    elif player_command == 'e':
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to
            print(f"\n{player}\n")
        else:
            print(f"Sorry {player.name}, no rooms to enter in the East\n")