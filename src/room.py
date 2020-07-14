# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        self.inventory = inventory

    def __str__(self):
        return f"{self.name}\n{self.description}\n\n{self.print_inventory()}"

    def print_inventory(self):

        inventory = ""
        for item in self.inventory:
            inventory += f"{item.name}: {item.description}\n"

        if self.inventory == []:
            return f"There is nothing here."
        else:
            return f"Around you, you see:\n{inventory}"
