from random import randint

from BattleGround.BattleFields.ClearMap import ClearMap
from Heroes.Hero_init import Hero
from ArmyGenerator.GenerateOrden import orden
from ArmyGenerator.GenerateNature import Nature


class ArmyStatus:
    def __init__(self, hero_: Hero,
                 army_: list):
        self.hero = hero_
        self.starting_army = army_
        self.current_army = army_
        self.stash = []
        self.army_on_field = []


def count_damage(first_creature, second_creature):
    base_damage = first_creature.min_damage + randint(
        first_creature.min_damage, first_creature.max_damage)
    if first_creature.attack > second_creature.protection:
        attack_defense_modifier = 1 + (first_creature.attack -
                                       second_creature.protection) * 0.05
    else:
        attack_defense_modifier = 1 / (1 + (first_creature.attack -
                                            second_creature.protection) * 0.05)
    return first_creature.count * base_damage * attack_defense_modifier


class Battle:
    def __init__(self, first_army, second_army):
        self.first_army_status = ArmyStatus(first_army.hero,
                                            first_army.soldiers)
        self.second_army_status = ArmyStatus(second_army.hero,
                                             second_army.soldiers)
        self.map = ClearMap.field
        self.queue_of_creatures = []

    def work_with_command(self, army, command, first_army_turn=True):
        next_player = False
        if command[0] == "stash":
            if int(command[1]) >= len(army.stash):
                print("Wrong stash number")
            else:
                creature = army.stash[int(command[1])]
                if first_army_turn:
                    if creature.length == 2:
                        if int(command[3]) >= 1 or int(command[3]) < 0 or \
                                int(command[2]) < 1 or int(command[2]) > 9:
                            print("Wrong place")
                        elif self.map[int(command[1])][int(command[2])] is not \
                                None:
                            print("Wrong place to put")
                            return next_player
                        else:
                            army.stash.pop(int(command[1]))
                            self.map[int(command[2])][0] = creature.name
                            self.map[int(command[2]) - 1][0] = creature.name
                            self.map[int(command[2])][1] = creature.name
                            self.map[int(command[2]) - 1][1] = creature.name
                            army.army_on_field += [[int(command[2]),
                                                    int(command[3])]]
                            army.starting_army.position_on_battle_ground = [
                                int(
                                    command[2]), int(command[3])]
                            print("Creature was placed on coordinates:\n x" + \
                                  (command[2]) + " y 0\n" + \
                                  "x" + str(int(command[2]) - 1) + " y 1\n" + \
                                  "x" + str(int(command[2]) - 1) + " y 0\n" + \
                                  "x" + str(int(command[2]) - 1) + " y 1\n")
                    else:
                        if int(command[3]) > 1 or int(command[3]) < 0 or \
                                int(command[2]) < 0 or int(command[2]) > 9:
                            print("Wrong place")
                        elif self.map[int(command[1])][int(command[2])] is not \
                                None:
                            print("Wrong place to put")
                            return next_player
                        else:
                            army.stash.pop(int(command[1]))
                            army.army_on_field += [[int(command[2]),
                                                    int(command[3])]]
                            self.map[int(command[2])][int(command[3])] = \
                                creature.name
                            creature.position_on_battle_ground = [int(
                                command[2]), int(command[3])]
                            print("Creature was placed on coordinates:\n x" + \
                                  (command[2]) + " y " + command[3])
                else:
                    if creature.length == 2:
                        if int(command[3]) <= 10 or int(command[3]) > 11 or \
                                int(command[2]) < 0 or int(command[2]) > 9:
                            print("Wrong place")
                        else:
                            army.stash.pop(int(command[1]))
                            self.map[int(command[2])][0] = creature.name
                            self.map[int(command[2]) - 1][0] = creature.name
                            self.map[int(command[2])][1] = creature.name
                            self.map[int(command[2]) - 1][1] = creature.name
                            army.army_on_field += [[int(command[2]),
                                                    int(command[3])]]
                            army.starting_army.position_on_battle_ground = [
                                int(
                                    command[2]), int(command[3])]
                            print("Creature was placed on coordinates:\n x" + \
                                  (command[2]) + " y 0\n" + \
                                  "x" + str(int(command[2]) - 1) + " y 1\n" + \
                                  "x" + str(int(command[2]) - 1) + " y 0\n" + \
                                  "x" + str(int(command[2]) - 1) + " y 1\n")
                    else:
                        if int(command[3]) < 10 or int(command[3]) > 11 or \
                                int(command[2]) < 0 or int(command[2]) > 9:
                            print("Wrong place")
                        else:
                            army.stash.pop(int(command[1]))
                            army.army_on_field += [[int(command[2]),
                                                    int(command[3])]]
                            self.map[int(command[2])][int(command[3])] = \
                                creature.name
                            creature.position_on_battle_ground = [int(
                                command[2]), int(command[3])]
                            print("Creature was placed on coordinates:\n x" + \
                                  (command[2]) + " y " + command[3])
        elif command[0] == "move":
            if self.map[int(command[1])][int(command[2])] is None:
                print("Wrong from coordinates")
            else:
                if [int(command[1]), int(command[2])] in army.army_on_field:
                    if command[3] == "stash":
                        for creature in army.starting_army:
                            if creature.name == \
                                    self.map[int(command[1])][int(command[2])]:
                                army.stash += [creature]
                                self.map[int(command[1])][int(command[2])] = \
                                    None
                                creature.position_on_battle_ground \
                                    = None
                                if creature.length == 2:
                                    self.map[int(command[1]) - 1][int(
                                        command[2])] = None
                                    self.map[int(command[1]) - 1][int(
                                        command[2]) + 1] = None
                                    self.map[int(command[1])][int(
                                        command[2]) + 1] = None
                                return next_player
                        print("Wrong creature")
                    elif command[3] == "to":
                        if self.map[int(command[4])][int(command[5])] is not \
                                None:
                            print("Wrong place to put")
                            return next_player
                        for creature in army.starting_army:
                            if creature.name == \
                                    self.map[int(command[1])][int(command[2])]:
                                self.move_creature(creature,
                                                   int(command[1]),
                                                   int(command[2]),
                                                   int(command[4]),
                                                   int(command[5]))
                                return next_player
                        print("Wrong creature")
                else:
                    print("Wrong creature")
        elif command[0] == "end":
            next_player = True
        else:
            print("Wrong command")
        return next_player

    def preparing(self):
        print(
            '''Preparing phase was activated
        use commands:
         stash number_of_creature_in_stash x_coord y_coord
         move x_from y_from to x_to y_to
         move stash
         end
         ''')
        for creature in self.first_army_status.starting_army:
            self.first_army_status.stash += [creature]
        for creature in self.second_army_status.starting_army:
            self.second_army_status.stash += [creature]
        continuing = True
        first_player = True
        while continuing:
            print("Your stash:", end=" ")
            if first_player:
                for creature in self.first_army_status.stash:
                    print(creature.name, end=" ")
            else:
                for creature in self.second_army_status.stash:
                    print(creature.name, end=" ")
            print()
            print("Your army on field:", end=" ")
            if first_player:
                if len(self.first_army_status.army_on_field) == 0:
                    print("Empty")
            else:
                if len(self.second_army_status.army_on_field) == 0:
                    print("Empty")
            if first_player:
                for creature in self.first_army_status.army_on_field:
                    print(self.map[creature[0]][creature[1]] + " " +
                          str(creature))
            else:
                for creature in self.second_army_status.army_on_field:
                    print(self.map[creature[0]][creature[1]] + " " +
                          str(creature))
            command = input().split()
            if first_player:
                next_player = self.work_with_command(self.first_army_status,
                                                     command)
                if next_player:
                    first_player = False
            else:
                next_player = self.work_with_command(self.second_army_status,
                                                     command, False)
                if next_player:
                    self.make_queue()
                    return

    def make_queue(self):
        all_army = self.first_army_status.army_on_field + \
                   self.second_army_status.army_on_field
        while len(all_army) != 0:
            self.queue_of_creatures += [all_army.pop(randint(0,
                                                             len(all_army) -
                                                             1))]

    def move_creature(self, creature, coordinate_x, coordinate_y,
                      coordinate_x_to, coordinate_y_to):
        if coordinate_y_to >= 12 or coordinate_y_to < 0 or \
                coordinate_x_to < 0 or coordinate_x_to > 9:
            return
        if creature.length == 2:
            if coordinate_y_to >= 11 or coordinate_y_to < 0 or \
                    coordinate_x_to < 1 or coordinate_x_to > 9:
                return
        self.map[coordinate_x][coordinate_y] = None
        self.map[coordinate_x_to][coordinate_y_to] = creature.name
        if [coordinate_x, coordinate_y] in \
                self.first_army_status.army_on_field:
            self.first_army_status.army_on_field[
                self.first_army_status.army_on_field.index([coordinate_x,
                                                            coordinate_y])] \
                = [coordinate_x_to, coordinate_y_to]
        else:
            self.second_army_status.army_on_field[
                self.second_army_status.army_on_field.index([coordinate_x,
                                                             coordinate_y])] \
                = [coordinate_x_to, coordinate_y_to]
        creature.position_on_battle_ground = [coordinate_x_to, coordinate_y_to]
        if creature.length == 2:
            self.map[coordinate_x][coordinate_y + 1] = None
            self.map[coordinate_x_to][coordinate_y_to + 1] = creature.name
            self.map[coordinate_x - 1][coordinate_y + 1] = None
            self.map[coordinate_x_to - 1][coordinate_y_to + 1] = creature.name
            self.map[coordinate_x - 1][coordinate_y] = None
            self.map[coordinate_x_to - 1][coordinate_y_to] = creature.name

    def move_and_attack(self, creature, coordinate_x, coordinate_y,
                        coordinate_x_to, coordinate_y_to,
                        attacked_coordinate_x, attacked_coordinate_y,
                        attacked_army):
        self.move_creature(creature, coordinate_x, coordinate_y,
                           coordinate_x_to, coordinate_y_to)
        if [attacked_coordinate_x, attacked_coordinate_y] not in \
                attacked_army.army_on_field:
            print("Wrong target. Only moved")
        second_creature = attacked_army.current_army[
            attacked_army.army_on_field.index([attacked_coordinate_x,
                                               attacked_coordinate_y])]
        message = second_creature.get_damaged(count_damage(creature,
                                                           second_creature))
        print(message)
        if "is dead" in message:
            attacked_army.army_on_field.pop(
                attacked_army.army_on_field.index([attacked_coordinate_x,
                                                   attacked_coordinate_y]))
            self.map[attacked_coordinate_x][attacked_coordinate_y] = None

    def next_turn(self, creature, coordinates):
        self.queue_of_creatures.pop(0)
        self.queue_of_creatures.insert(int(len(
            self.queue_of_creatures) * 10 / creature.initiative), coordinates)

    def battle(self):
        self.preparing()
        print('''Battle was begun
        Use commands:
            move x_from y_from x_to y_to
            move_attack x_from y_from x_to y_to x_attacked y_attacked
            exit
        ''')
        while len(self.first_army_status.army_on_field) != 0 and len(
                self.second_army_status.army_on_field) != 0:
            for line in self.map:
                for element in line:
                    print(element, end=" ")
                print()
            tmp = self.queue_of_creatures[0]
            print(tmp)
            print(self.map[tmp[0]][tmp[1]] + " turn")
            if tmp in self.first_army_status.army_on_field:
                army = self.first_army_status
                attacked_army = self.second_army_status
            else:
                army = self.second_army_status
                attacked_army = self.first_army_status
            for soldier in army.current_army:
                if soldier.name == self.map[tmp[0]][tmp[1]]:
                    creature = soldier
            com = input().split()
            if com[0] == "move":
                if [int(com[1]), int(com[2])] != tmp:
                    print("wrong command")
                    continue
                self.move_creature(creature, int(com[1]),
                                   int(com[2]), int(com[3]), int(com[4]))
                self.next_turn(creature, [int(com[3]), int(com[4])])
            elif com[0] == "move_attack":
                if [int(com[1]), int(com[2])] != tmp:
                    print("wrong command")
                    continue
                self.move_and_attack(creature, int(com[1]),
                                     int(com[2]), int(com[3]), int(com[4]),
                                     int(com[5]), int(com[6]), attacked_army)
                self.next_turn(creature, [int(com[3]), int(com[4])])
            elif com[0] == "exit":
                break
            else:
                print("wrong command")
        print("The game was ended")


class army:
    def __init__(self, hero_, soldiers):
        self.hero = hero_
        self.soldiers = soldiers


first = orden()
second = Nature()
first.first_creature.add_count(first.first_creature, 40)
first.second_creature.add_count(first.second_creature, 20)
first.third_creature.add_count(first.third_creature, 10)
first.fourth_creature.add_count(first.fourth_creature, 5)
second.first_creature.add_count(second.first_creature, 40)
second.second_creature.add_count(second.second_creature, 20)
second.third_creature.add_count(second.third_creature, 10)
second.fourth_creature.add_count(second.fourth_creature, 5)

first_army = army(None, [first.first_creature,
                         first.second_creature,
                         first.third_creature,
                         first.fourth_creature])
second_army = army(None, [second.first_creature,
                          second.second_creature,
                          second.third_creature,
                          second.fourth_creature])

battle = Battle(first_army, second_army)
battle.battle()
