# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player:
    def __init__(self, name, current_room, inventory = None):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory if inventory is not None else []

    def __str__(self):
        return_str = f'{self.name}, you are at \'{self.current_room.name}\' and {self.current_room.description} \nYour inventory: '
        for item in self.inventory:
            return_str = return_str + item.name
        return return_str

    def add_item(self, item):
        self.inventory.append(item)
    
    def remove_item(self, item_name):
        for index, item in enumerate(self.inventory):
            if item.name == item_name:
                removed_item = self.inventory.pop(index)
                return removed_item