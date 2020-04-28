from Heroes.Hero_init import Hero


class ArmyStatus:
    def __init__(self, hero_: Hero,
                 army_: list):
        self.hero = hero_
        self.starting_army = army_
        self.current_army = army_
        self.stash = []
        self.army_on_field = []
