import unittest
from random import randint

from ArmyGenerator.GenerateInferno import inferno
from ArmyGenerator.GenerateShadowLeague import Shadow
from ArmyGenerator.GenerateMage import mage
from ArmyGenerator.GenerateOrden import orden
from ArmyGenerator.GenerateNature import Nature
from ArmyGenerator.GenerateNecropolis import necro
from Battle.ArmyStatus import ArmyStatus
from Battle.BattleDecorators.Attack_and_move_back import Attack_and_move_back
from Battle.BattleDecorators.Attack_without_return import Attack_without_return
from Battle.BattleDecorators.BattleUnit import BattleUnit
from Battle.BattleDecorators.DamageIncreasingWithMovement import \
    DamageIncreasingWithMovement
from Battle.BattleDecorators.KillingOneCreature import KillingOneCreature
from Battle.BattleDecorators.LifeStealCreature import LifeStealCreature
from Battle.BattleDecorators.RangeAttack import RangeAttackCreature
from Battle.BattleDecorators.TripleAttackCreature import TripleAttackCreature
from Battle.arrays import attack_without_return, attack_and_move_back, \
    triple_attack_creatures, damage_increasing_with_movement, life_stealing, \
    Killing_one_creature
from Battle.count_damage import count_min_damage, count_max_damage


class TestClass(unittest.TestCase):
    def setUp(self, class_=None) -> None:
        self.class__ = class_
        if class_ is not None:
            hero = orden()
            hero.create_hero_First()
            self.first_army = class_()
            self.taking_damage_creature = orden().first_creature
            self.taking_damage_creature.count = 10000000000
            self.taking_damage_creature.position_on_battle_ground = [1, 1]
            self.taking_damage_creature_second = orden().first_creature
            self.taking_damage_creature_second.count = 10000000000
            self.taking_damage_creature_second.position_on_battle_ground = [1, 0]
            self.taking_damage_creature_third = orden().first_creature
            self.taking_damage_creature_third.count = 10000000000
            self.taking_damage_creature_third.position_on_battle_ground = [0, 1]
            self.other_army = ArmyStatus(hero.first_hero, [
                self.taking_damage_creature,
                self.taking_damage_creature_second,
                self.taking_damage_creature_third
            ])
            self.taking_damage_creature = BattleUnit(self.taking_damage_creature)
            self.taking_damage_creature_second = BattleUnit(
                self.taking_damage_creature_second
            )
            self.taking_damage_creature_third = BattleUnit(
                self.taking_damage_creature_third
            )
            self.taking_damage_creature.can_conter_attack = 100000000
            self.taking_damage_creature_second.can_conter_attack = 100000000
            self.taking_damage_creature_third.can_conter_attack = 100000000
            self.other_army.army_on_field = [[1, 1], [1, 0], [0, 1]]
            self.army_list = [
                self.first_army.first_creature,
                self.first_army.first_creature_upgraded,
                self.first_army.second_creature,
                self.first_army.second_creature_upgraded,
                self.first_army.third_creature,
                self.first_army.third_creature_upgraded,
                self.first_army.fourth_creature,
                self.first_army.fourth_creature_upgraded,
                self.first_army.fifth_creature,
                self.first_army.fifth_creature_upgraded,
                self.first_army.sixth_creature,
                self.first_army.sixth_creature_upgraded,
                self.first_army.seventh_creature,
                self.first_army.seventh_creature_upgraded
            ]
            for i in range(len(self.army_list)):
                self.army_list[i].count = randint(1, 100)
                self.army_list[i].position_on_battle_ground = [0, 0]
                self.army_list[i] = BattleUnit(self.army_list[i])
                if self.army_list[i].base.shots is not None and \
                        self.army_list[i].base.shots > 0:
                    self.army_list[i] = RangeAttackCreature(
                        self.army_list[i])
                if self.army_list[i].base.name in attack_without_return:
                    self.army_list[i] = Attack_without_return(
                        self.army_list[i])
                if self.army_list[i].base.name in attack_and_move_back:
                    self.army_list[i] = Attack_and_move_back(
                        self.army_list[i])
                if self.army_list[i].base.name in triple_attack_creatures:
                    self.army_list[i] = TripleAttackCreature(
                        self.army_list[i])
                if self.army_list[i].base.name in \
                        damage_increasing_with_movement:
                    self.army_list[i] = DamageIncreasingWithMovement(
                        self.army_list[i])
                if self.army_list[i].base.name in life_stealing:
                    self.army_list[i] = LifeStealCreature(self.army_list[i])
                if self.army_list[i].base.name in Killing_one_creature:
                    self.army_list[i] = KillingOneCreature(self.army_list[i])

    def test_army_creating(self):
        if self.class__ is None:
            return
        print(str(self.class__) + "is checking")
        for i in range(len(self.army_list)):
            self.assertLess(self.army_list[i].base.count, 1001,
                            "Wrong count. Greater then must be")
            self.assertGreater(self.army_list[i].base.count, 0,
                               "Wrong count. Less then must be")
            if self.army_list[i].base.shots is not None and \
                    self.army_list[i].base.shots > 0:
                self.assertIsInstance(self.army_list[i],
                                      RangeAttackCreature,
                                      self.army_list[i].base.name + " must be "
                                                                    "range attack")
            elif self.army_list[i].base.name in attack_without_return:
                self.assertIsInstance(
                    self.army_list[i],
                    Attack_without_return,
                    self.army_list[
                        i].base.name + " must be attack_without_return"
                )
            elif self.army_list[i].base.name in attack_and_move_back:
                self.assertIsInstance(
                    self.army_list[i],
                    Attack_and_move_back,
                    self.army_list[
                        i].base.name + " must be attack_and_move_back"
                )
            elif self.army_list[
                i].base.name in damage_increasing_with_movement:
                self.assertIsInstance(
                    self.army_list[i],
                    DamageIncreasingWithMovement,
                    self.army_list[
                        i].base.name + " must be damage_increasing_with_movement"
                )
            elif self.army_list[i].base.name in Killing_one_creature:
                self.assertIsInstance(
                    self.army_list[i],
                    KillingOneCreature,
                    self.army_list[
                        i].base.name + " must be Killing_one_creature"
                )
            elif self.army_list[i].base.name in life_stealing:
                self.assertIsInstance(
                    self.army_list[i],
                    LifeStealCreature,
                    self.army_list[i].base.name + " must be life_stealing"
                )
            elif self.army_list[i].base.name in triple_attack_creatures:
                self.assertIsInstance(
                    self.army_list[i],
                    TripleAttackCreature,
                    self.army_list[i].base.name + " must be triple_attack"
                )
            else:
                self.assertIsInstance(
                    self.army_list[i],
                    BattleUnit,
                    self.army_list[i].base.name + " must be battle_unit"
                )

    def test_army_battle(self):
        if self.class__ is None:
            return
        print(str(self.class__) + "is checking battle")
        print(str(len(self.army_list))+" units were ckecked")
        for i in range(len(self.army_list)):
            if hasattr(self.army_list[i], "range_attack"):
                shots_were = self.army_list[i].base.shots
                message = self.army_list[i].range_attack(
                    self.taking_damage_creature
                )
                self.assertEqual(self.army_list[i].base.shots, shots_were - 1)
                min_damage = count_min_damage(self.army_list[i].base,
                                              self.taking_damage_creature.base)
                min_damage = int(min_damage) + (int(min_damage * 10) % 10 >= 5)
                max_damage = count_max_damage(self.army_list[i].base,
                                              self.taking_damage_creature.base)
                max_damage = int(max_damage) + (int(max_damage * 10) % 10
                                                >= 5)
                for line in message:
                    words = line.split()
                    if "is dead" in line:
                        self.assertEqual(words[0],
                                         self.taking_damage_creature.base.name)
                    else:
                        self.assertEqual(words[1],
                                         self.taking_damage_creature.base.name)
                        self.assertGreaterEqual(int(words[3]),
                                                min_damage,
                                                "Damage is Less than must be")
                        self.assertLessEqual(int(words[3]),
                                             max_damage,
                                             "Damage is Less than must be")
            if isinstance(self.army_list[i], TripleAttackCreature):
                if self.army_list[i].base.length == 2:
                    self.army_list[i].base.position_on_battle_ground = [0, 2]
                message = self.army_list[i].melee_attack(
                    self.taking_damage_creature,
                    None,
                    self.other_army
                )
                if self.army_list[i].base.length == 2:
                    self.assertEqual(
                        len(message),
                        3,
                        "wrong triple attack. creature is " +
                        self.army_list[i].base.name
                    )
                    self.assertTrue("is dead" in message[2], "Didn't die")
                else:
                    self.assertEqual(
                        len(message),
                        4,
                        "wrong triple attack. creature is " +
                        self.army_list[i].base.name
                    )
                    self.assertTrue("is dead" in message[3], "Didn't die")
            if isinstance(self.army_list[i], Attack_without_return):
                message = self.army_list[i].melee_attack(
                    self.taking_damage_creature,
                    None,
                    self.other_army
                )
                self.assertEqual(len(message), 1, "get conterattacked")
            if isinstance(self.army_list[i], KillingOneCreature):
                message = self.army_list[i].melee_attack(
                    self.taking_damage_creature,
                    None,
                    self.other_army
                )
                self.assertGreaterEqual(int(message[0].split()[0]), 1,
                                        "Didn't kill")


test = TestClass()
test.setUp(orden)
test.test_army_creating()
test.test_army_battle()
test.setUp(necro)
test.test_army_creating()
test.test_army_battle()
test.setUp(mage)
test.test_army_creating()
test.test_army_battle()
test.setUp(inferno)
test.test_army_creating()
test.test_army_battle()
test.setUp(Nature)
test.test_army_creating()
test.test_army_battle()
test.setUp(Shadow)
test.test_army_creating()
test.test_army_battle()
