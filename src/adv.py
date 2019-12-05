from room import Room
from player import Player
from item import Item

#Declare all the items
items = {
    'sword': Item("sword", "nice and sharp"),
    'ax': Item("ax", "one big")
}

# Declare all the rooms
rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items["ax"], items["sword"]]),

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

def print_help():
    print('Enter "n" for North, "s" for South, "e" for East, "w" for West, "q" to quit and "h" for Help. '
    '\nTo pick up an item type "take item name", to drop the item type "drop item name"')

def advance_room(player, player_input):
    #assigning player input into variable
    player_attribute = f'{player_input}_to'
    #checking if the attribute exists in the object
    if hasattr(player.current_room, player_attribute):
        #assigning the player object with new room
        player.current_room = getattr(player.current_room, player_attribute)
        return True
    else:
        return False

def process_command(player, command, item_name):
    room_items = [ item.name for item in player.current_room.items ]
    player_items = [ item.name for item in player.inventory ]
    if command == 'take':
        if item_name in room_items:
            item = player.current_room.remove_item(item_name)
            player.add_item(item)
            return True
        else:
            print(f'{item_name} does not exist in this room!')
            return True
    elif command == 'drop':
        if item_name in player_items:
            item = player.remove_item(item_name)
            player.current_room.add_item(item)
            return True
        else:
            print(f'You do not have the item called {item_name} to drop')
            return True
    else:
        return False

def run_command(player, player_input):
    # splitting 2 word commands
    splitted_command = player_input.split()
    # making lists to check if the item exists
    possible_commands = ['take', 'drop']

    if player_input in ['n', 's', 'w', 'e', 'q', 'h']:
        if player_input == 'q':
            print(f"Goodbye {first_player.name}")
            exit(1)
        elif player_input == 'h':
            print_help()
        elif not advance_room(first_player, player_input):
            print('You shall not pass! Read the description and choose your path carefully!')
        return True
    elif splitted_command[0] in possible_commands:
        return process_command(player, splitted_command[0], splitted_command[1])
    else:
        return False


# Make a new player object that is currently in the 'outside' room.\
first_player = Player("BraveHeart", rooms['outside'])

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

print_help()
while True:
    print(first_player)
    for item in first_player.current_room.items:
        print(f'There is {item.description} {item.name} in this room!')
    player_input = input("-> ")

    if not run_command(first_player, player_input):
        print('Invalid command! \nPlease enter "n" for North, "s" for South, "e" for East, "w" for West and "q" to quit the game.')





