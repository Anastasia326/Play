from Map.Work_with_resources.Hero_resouces import Resources


class Miner:
    def __init__(self, producing_resource: str, position: list):
        if producing_resource == "Gold":
            self.increase = ("Gold", 2000)
        else:
            self.increase = (producing_resource, 2)
        self.belongs_to = None
        self.receiver = []
        self.position_on_map = position

    def get_under_control(self, hero_name: str):
        if hero_name != self.belongs_to:
            for i in self.receiver:
                if self.belongs_to is None:
                    if i.belongs_to == hero_name:
                        i.update(self.increase[0] + " " + hero_name + " " +
                                 str(self.increase[1]))
                else:
                    i.update(self.increase[0] + " " + hero_name + " " + str(
                        self.increase[1]))
            self.belongs_to = hero_name

    def add_hero_resources(self, res: Resources):
        self.receiver += [res]
