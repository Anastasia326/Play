from ..imports import resources


class Resources:
    def __init__(self, hero_name: str):
        self.belongs_to = hero_name
        self.reserve = {
            "Gold": 1000,
            "Red": 20,
            "Yellow": 20,
            "Blue": 20,
            "Wood": 20,
            "Stone": 20
        }
        self.increasing = {
            "Gold": 500,
            "Red": 0,
            "Yellow": 0,
            "Blue": 0,
            "Wood": 0,
            "Stone": 0
        }

    def update(self, message: str):
        information = message.split()
        if information[1] == self.belongs_to:
            self.increasing[information[0]] += int(message[2])
        else:
            self.increasing[information[0]] -= int(message[2])

    def next_turn(self):
        for item in self.increasing.items():
            self.reserve[item[0]] += item[1]

    def remove_resources(self, count: list):
        for i in range(len(count)):
            self.reserve[resources[i]] -= count[i]

    def add_resources(self, count: list):
        for i in range(len(count)):
            self.reserve[resources[i]] += count[i]

    def add_resource(self, resource_name: str, resource_count: int):
        self.reserve[resources.index(resource_name)] += resource_count

    def can_do(self, required_resources: list):
        for i in range(len(required_resources)):
            if self.reserve[resources[i]] < required_resources[i]:
                return False
        return True
