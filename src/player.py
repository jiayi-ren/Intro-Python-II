# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.current_room = room
        self.items = []

    def __str__(self):
        return f"{self.name}, your location: {self.current_room}"

    def try_direction(self, command):
        attribute = command + '_to'
        if hasattr(self.current_room, attribute):
            self.current_room = getattr(self.current_room, attribute)
        else:
            print(f"Sorry {self.name}, you can't go that way!\n")

    def get_item(self, item):
        got = []
        for elem in self.current_room.inventory:
            if item == elem.name.lower():
                self.items.append(elem)
                elem.on_take()
                self.current_room.inventory.remove(elem)
                got.append(item)
        if got == []:
            print(f"Wake up adventurer, there is no such things in the room")

    def drop_item(self, item):
        got = []
        for elem in self.items:
            if item == elem.name.lower():
                self.items.remove(elem)
                elem.on_drop()
                self.current_room.inventory.append(elem)
                got.append(item)
        if got == []:
            print(f"Wake up adventurer, you don't have such item")

    def show_items(self):
        message = ""
        for item in self.items:
            message += f"{item.name},"
        if len(self.items) > 1:
            message = message[:-1]

        if self.items == "":
            print("You don't have anything")
        else:
            print(f"You have: {message}")
