from Heroes.Hero_init import Hero
from Battle.BattleDecorators.BattleUnit import BattleUnit
from Battle.BattleDecorators.Attack_and_move_back import Attack_and_move_back
from Battle.BattleDecorators.Attack_without_return import Attack_without_return
from Battle.BattleDecorators.DamageIncreasingWithMovement import \
    DamageIncreasingWithMovement
from Battle.BattleDecorators.KillingOneCreature import KillingOneCreature
from Battle.BattleDecorators.LifeStealCreature import LifeStealCreature
from Battle.BattleDecorators.RangeAttack import RangeAttackCreature
from Battle.BattleDecorators.TripleAttackCreature import TripleAttackCreature
from Battle.arrays import attack_and_move_back, attack_without_return, \
    triple_attack_creatures, damage_increasing_with_movement, life_stealing, \
    Killing_one_creature


class ArmyStatus:
    def __init__(self, hero_: Hero,
                 army_: list):
        self.hero = hero_
        self.starting_army = army_[::]
        self.current_army = army_
        for i in range(len(self.current_army)):
            self.current_army[i] = BattleUnit(self.current_army[i])
            if self.current_army[i].base.shots is not None and \
                    self.current_army[i].base.shots > 0:
                self.current_army[i] = RangeAttackCreature(
                    self.current_army[i])
            if self.current_army[i].base.name in attack_without_return:
                self.current_army[i] = Attack_without_return(
                    self.current_army[i])
            if self.current_army[i].base.name in attack_and_move_back:
                self.current_army[i] = Attack_and_move_back(
                    self.current_army[i])
            if self.current_army[i].base.name in triple_attack_creatures:
                self.current_army[i] = TripleAttackCreature(
                    self.current_army[i])
            if self.current_army[i].base.name in \
                    damage_increasing_with_movement:
                self.current_army[i] = DamageIncreasingWithMovement(
                    self.current_army[i])
            if self.current_army[i].base.name in life_stealing:
                self.current_army[i] = LifeStealCreature(self.current_army[i])
            if self.current_army[i].base.name in Killing_one_creature:
                self.current_army[i] = KillingOneCreature(self.current_army[i])
        self.stash = []
        self.army_on_field = []

