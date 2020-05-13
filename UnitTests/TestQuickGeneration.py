import unittest

import pygame

from ArmyGenerator.GenerateOrden import orden
from ArmyGenerator.GenerateInferno import inferno
from Battle.army import Army
from Map.Quick import QuickMap
from Map.Medium import MediumMap
from Working_with_textures.drow_map import drow_map
from Working_with_textures.Main_menu import create_window


class TestQuick(unittest.TestCase):
    def setUp(self) -> None:
        first_class = orden()
        first_class.create_hero_First()
        second_class = inferno()
        second_class.create_hero_First()
        first_class.first_creature.count = 40
        second_class.first_creature.count = 40
        first_army = Army(first_class.first_hero,
                          [first_class.first_creature])
        second_army = Army(second_class.first_hero,
                           [second_class.first_creature])
        self.QuickMap = QuickMap(first_army, second_army)

    def test_quick(self):
        for i in range(50):
            for j in range(11):
                print("%s" % self.QuickMap.Map[i][j].center(15), end=" ")
            print()
        self.assertEqual(len(self.QuickMap.Map), 50)
        self.assertEqual(len(self.QuickMap.Map[0]), 11)
        for i in range(49):
            if i < 5 or i > 43:
                self.assertNotEqual(self.QuickMap.Map[i],
                                    self.QuickMap.Map[i + 1])

class TestMedium(unittest.TestCase):
    def setUp(self) -> None:
        first_class = orden()
        first_class.create_hero_First()
        second_class = inferno()
        second_class.create_hero_First()
        first_class.first_creature.count = 40
        second_class.first_creature.count = 40
        first_army = Army(first_class.first_hero,
                          [first_class.first_creature])
        second_army = Army(second_class.first_hero,
                           [second_class.first_creature])
        self.Medium = MediumMap(first_army, second_army)

    def test_medium(self):
        for i in range(100):
            for j in range(20):
                print("%s" % self.Medium.Map[i][j].center(15), end=" ")
            print()
        self.assertEqual(len(self.Medium.Map), 100)
        self.assertEqual(len(self.Medium.Map[0]), 20)
