from room import Room
from player import Player
from item import Item

#Declare all the items
items = {
    'sword': Item("sword", "nice and sharp")
}

# Declare all the rooms
rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items["sword"]]),

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


# Make a new player object that is currently in the 'outside' room.\
first_player = Player("BraveHeart", rooms['outside'])



def check_command(player, player_input):
    room_items = [ item.name for item in player.current_room.items ]
    player_items = [ item.name for item in player.inventory ]
    possible_commands = ['take', 'drop']
    splitted_command = player_input.split()
    if player_input in ['n', 's', 'w', 'e', 'q']:
        if player_input == 'q':
            print(f"Goodbye {first_player.name}")
            exit(1)
        if not advance_room(first_player, player_input):
            print('You shall not pass! Read the description and choose your path carefully!')
        return True
    elif splitted_command[0] in possible_commands:
        if splitted_command[0] == 'take':
            if splitted_command[1] in room_items:
                item_name = splitted_command[1]
                item = player.current_room.remove_item(item_name)
                player.add_item(item)
                return True
            else:
                print(f'{splitted_command[1]} does not exist in this room!')
                return True
        elif splitted_command[0] == 'drop':
            if splitted_command[1] in player_items:
                item_name = splitted_command[1]
                item = player.remove_item(item_name)
                player.current_room.add_item(item)
                return True
            else:
                print(f'You do not have the item called {splitted_command[1]} to drop')
                return True

possible_inputs = ['n', 's', 'w', 'e', 'q', 'pick sword', 'drop sword']
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

print('Enter "n" for North, "s" for South, "e" for East, "w" for West and "q" to quit the game. \nTo pick up an item type "take item name", to drop the item type "drop item name"')
while True:
    print(first_player)
    for item in first_player.current_room.items:
        print(f'There is {item.description} {item.name} in this room!')
    player_input = input("-> ")

    if not check_command(first_player, player_input):
        print('Invalid command! \nPlease enter "n" for North, "s" for South, "e" for East, "w" for West and "q" to quit the game.')





