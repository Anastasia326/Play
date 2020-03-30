import unittest
from Orden.FirstCreature import FirstNotUpgraded


class TestVillager(unittest.TestCase):
    def setUp(self) -> None:
        self.unit = FirstNotUpgraded()

    def test_unit(self):
        self.assertEqual(self.unit.count, 0, "Not zero count")
        self.assertEqual(self.unit.name, "Villager", "wrong name")
        self.assertEqual(self.unit.attack, 1, "wrong attack")
        self.assertEqual(self.unit.protection, 1, "wrong protection")
        self.assertEqual(self.unit.min_damage, 1, "wrong min_damage")
        self.assertEqual(self.unit.max_damage, 1, "wrong max_damage")
        self.assertEqual(self.unit.health_points, 3, "wrong health")
        self.assertEqual(self.unit.initiative, 8, "wrong initiative")
        self.assertEqual(self.unit.speed, 4, "wrong speed")
        self.assertEqual(self.unit.shots, None, "wrong shots")
        self.assertEqual(self.unit.mana, None, "wrong mana")
        self.assertEqual(self.unit.cost, 15, "wrong cost")
        self.assertEqual(self.unit.upgrade_cost, 10, "wrong upgrade")
        self.assertEqual(self.unit.length, 1, "wrong length")
        self.assertEqual(self.unit.width, 1, "wrong width")
        self.assertEqual(self.unit.spells, None, "wrong spells")
        self.unit.add_count(5)
        self.assertEqual(self.unit.count, 5, "wrong added")  # count
        self.assertEqual(self.unit.get_damaged(1), "0 Villager died. 1 was "
                                                   "taken")
        self.assertEqual(self.unit.get_damaged(2), "1 Villager died. 2 was "
                                                   "taken")
        self.assertEqual(self.unit.get_damaged(7), "2 Villager died. 7 was "
                                                   "taken")
        self.assertEqual(self.unit.count, 2)


if __name__ == '__main__':
    unittest.main()
