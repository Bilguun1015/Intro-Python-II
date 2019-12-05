# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = None):
        self.name = name
        self.description = description
        self.items = items if items is not None else []

    def __str__(self):
        return f'{self.name} {self.description} {self.items}'
        
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for index, item in enumerate(self.items):
            if item.name == item_name:
                removed_item = self.items.pop(index)
                return removed_item
