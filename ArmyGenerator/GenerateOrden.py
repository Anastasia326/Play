from Units.Creator import Creator
from Orden.FirstCreature import FirstUpgraded, FirstNotUpgraded
from Orden.SecondCreature import SecondUpgraded, SecondNotUpgraded
from Orden.ThirdCreature import ThirdUpgraded, ThirdNotUpgraded
from Orden.FourthCreature import FourthUpgraded, FourthNotUpgraded
from Orden.FifthCreature import FifthUpgraded, FifthNotUpgraded
from Orden.SixthCreature import SixthUpgraded, SixthNotUpgraded
from Orden.SeventhCreature import SeventhUpgraded, SeventhNotUpgraded
from Heroes.HeroCatalog.Orden.Ivanhoe import Knight
from Heroes.HeroCatalog.Orden.Swerchok import Priest

class orden(Creator):
    def create_first_type_creatures(self):
        self.first_creature = FirstNotUpgraded()
        self.first_creature_upgraded = FirstUpgraded()

    def create_second_type_creatures(self):
        self.second_creature = SecondNotUpgraded()
        self.second_creature_upgraded = SecondUpgraded()

    def create_third_type_creatures(self):
        self.third_creature = ThirdNotUpgraded()
        self.third_creature_upgraded = ThirdUpgraded()

    def create_fourth_type_creatures(self):
        self.fourth_creature = FourthNotUpgraded()
        self.fourth_creature_upgraded = FourthUpgraded()

    def create_fifth_type_creatures(self):
        self.fifth_creature = FifthNotUpgraded()
        self.fifth_creature_upgraded = FifthUpgraded()

    def create_sixth_type_creatures(self):
        self.sixth_creature = SixthNotUpgraded()
        self.sixth_creature_upgraded = SixthUpgraded()

    def create_seventh_type_creatures(self):
        self.seventh_creature = SeventhNotUpgraded()
        self.seventh_creature_upgraded = SeventhUpgraded()

    def create_hero_First(self):
        self.first_hero = Knight()

    def create_hero_Second(self):
        self.second_hero = Priest()
