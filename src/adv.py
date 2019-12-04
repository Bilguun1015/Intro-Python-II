from room import Room
from player import Player
# Declare all the rooms

rooms = {
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

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

#
# Main
#
first_player = Player("BraveHeart", rooms['outside'])

def advance_room(player, player_input):
    if player_input == 'n':
        player.current_room = player.current_room.n_to
    elif player_input == 's':
        player.current_room = player.current_room.s_to
    elif player_input == 'e':
        player.current_room = player.current_room.e_to
    elif player_input == 'w':
        player.current_room = player.current_room.w_to
    else:
        return False

def check_bad_input(player, player_input):
    foyer_possible_inputs = ['s', 'n', 'e']
    narrow_possible_inputs = ['w','n']
    
    if player.current_room.name == 'Outside Cave Entrance' and player_input == 'n':
        return True
    elif player.current_room.name == 'Foyer' and player_input in foyer_possible_inputs:
        return True
    elif player.current_room.name == 'Grand Overlook' and player_input == 's':
        return True
    elif player.current_room.name == 'Narrow Passage' and player_input in narrow_possible_inputs:
        return True
    elif player.current_room.name == 'Treasure Chamber' and player_input == 's':
        return True
    else:
        return False

possible_inputs = ['n', 's', 'w', 'e', 'q']

print('Enter "n" for North, "s" for South, "e" for East, "w" for West and "q" to quit the game.')
while True:
    print(first_player)
    player_input = input("-> ")

    if player_input in possible_inputs:
        result = check_bad_input(first_player, player_input)
        if player_input == 'q':
            print(f"Goodbye {first_player.name}")
            break
        if result:
            advance_room(first_player, player_input)
        else:
            print('You shall not pass! Read the description carefully to choose your path!')
    else:
        print('Invalid command! Please enter "n" for North, "s" for South, "e" for East, "w" for West and "q" to quit the game.')

# def main():
# Make a new player object that is currently in the 'outside' room.\
#     player_input = input("Enter n for advancing to North:")
#     if player_input:
#         advancing_room(first_player, player_input)
# main()



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
