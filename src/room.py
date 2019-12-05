# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f'{self.name} {self.description} {self.items}'

    def remove_item(self, item_name):
        for index, item in enumerate(self.items):
            if item.name == item_name:
                removed_item = self.items.pop(index)
                return removed_item
    
    def add_item(self, item):
        self.items.append(item)