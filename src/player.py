# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        super().__init__()
        self.name = name
        self.current_room = room

    def __str__(self):
        return f"{self.name}, you entered {self.current_room}"
