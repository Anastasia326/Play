from Units.Creator import Creator
from Mage.FirstCreature import FirstUpgraded, FirstNotUpgraded
from Mage.SecondCreature import SecondUpgraded, SecondNotUpgraded
from Mage.ThirdCreature import ThirdUpgraded, ThirdNotUpgraded
from Mage.FourthCreature import FourthUpgraded, FourthNotUpgraded
from Mage.FifthCreature import FifthUpgraded, FifthNotUpgraded
from Mage.SixthCreature import SixthUpgraded, SixthNotUpgraded
from Mage.SeventhCreature import SeventhUpgraded, SeventhNotUpgraded


class mage(Creator):
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

    def create_hero(self, name):
        pass
