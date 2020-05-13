from random import randint

from Battle.ArmyStatus import ArmyStatus
from Battle.borders import in_borders
from Battle.wait import wait
from Battle.worker_after_wait_for_preparing import \
    worker_after_wait_for_preparing
from BattleGround.BattleFields.ClearMap import ClearMap
from Working_with_textures.choose_units_to_kill import choose_units_to_kill
from Working_with_textures.draw_commans import draw_commans
from Working_with_textures.draw_green_cell import draw_green_cell
from Working_with_textures.map_draw import map_draw
from Working_with_textures.waaar import waaar
from .borders import borders


class Battle:
    message_ = ""
    def __init__(self, first_army, second_army, window, fullscreen):
        self.fullscreen = fullscreen
        self.window = window
        self.first_army_status = ArmyStatus(first_army.hero,
                                            first_army.soldiers)
        self.second_army_status = ArmyStatus(second_army.hero,
                                             second_army.soldiers)
        self.map = ClearMap.field
        self.queue_of_creatures = []
        self.deleted_from_first = []
        self.deleted_from_second = []

    def use_info_from_message(self, message, army, attacked_army):
        for lines in message:
            if "is dead" in lines:
                creatures = None
                if message.index(lines) % 2 == 0:
                    for soldier in attacked_army.current_army:
                        if soldier.base.name == lines.split()[0]:
                            creatures = soldier
                    if attacked_army == self.first_army_status:
                        self.deleted_from_first += [creatures.base.name]
                    else:
                        self.deleted_from_second += [creatures.base.name]
                    attacked_army.current_army.pop(
                        attacked_army.current_army.index(
                            creatures
                        )
                    )
                    self.queue_of_creatures.pop(
                        self.queue_of_creatures.index(
                            creatures.base.position_on_battle_ground
                        )
                    )
                    attacked_army.army_on_field.pop(
                        attacked_army.army_on_field.index(
                            creatures.base.position_on_battle_ground
                        )
                    )
                    self.map[creatures.base.position_on_battle_ground[0]][
                        creatures.base.position_on_battle_ground[1]] = None
                    if creatures.base.length == 2:
                        self.map[creatures.base.position_on_battle_ground[0]
                                 - 1][
                            creatures.base.position_on_battle_ground[1]] = None
                        self.map[creatures.base.position_on_battle_ground[0]
                                 - 1][
                            creatures.base.position_on_battle_ground[1] + 1] \
                            = None
                        self.map[creatures.base.position_on_battle_ground[0]][
                            creatures.base.position_on_battle_ground[1] + 1] \
                            = None

                else:
                    for soldier in army.current_army:
                        if soldier.base.name == lines.split()[0]:
                            creatures = soldier
                    army.current_army.pop(
                        army.current_army.index(
                            creatures
                        )
                    )
                    self.queue_of_creatures.pop(
                        self.queue_of_creatures.index(
                            creatures.base.position_on_battle_ground
                        )
                    )
                    army.army_on_field.pop(
                        army.army_on_field.index(
                            creatures.base.position_on_battle_ground
                        )
                    )
                    self.map[creatures.base.position_on_battle_ground[0]][
                        creatures.base.position_on_battle_ground[1]] = None
                    if creatures.base.length == 2:
                        self.map[creatures.base.position_on_battle_ground[0]
                                 - 1][
                            creatures.base.position_on_battle_ground[1]] = None
                        self.map[creatures.base.position_on_battle_ground[0]
                                 - 1][
                            creatures.base.position_on_battle_ground[1] + 1] \
                            = None
                        self.map[creatures.base.position_on_battle_ground[0]][
                            creatures.base.position_on_battle_ground[1] + 1] \
                            = None
            print(lines)

    def work_with_command(self, army, command, first_army_turn=True):
        next_player = False
        if command[0] == "stash":
            if int(command[1]) >= len(army.stash):
                print("Wrong stash number")
                self.message_ = "Wrong stash number"
            else:
                creature = army.stash[int(command[1])]
                if creature.base.length == 2:
                    if int(command[3]) != \
                            borders[0 if first_army_turn else 1][1][0] or \
                            int(command[2]) < 1 or int(command[2]) > 9:
                        print("Wrong place")
                        self.message_ = "Wrong place"
                    elif self.map[int(command[2])][int(command[3])] is not \
                            None or \
                            self.map[int(command[2]) - 1][int(command[3])] is \
                            not None or \
                            self.map[int(command[2])][int(command[3]) + 1] is \
                            not None or \
                            self.map[int(command[2]) - 1][int(command[3]) + 1] \
                            is not None:
                        print("Wrong place to put")
                        self.message_ = "Wrong place to put"
                        return next_player
                    else:
                        army.stash.pop(int(command[1]))
                        self.map[int(command[2])][int(command[3])] = \
                            creature.base.name
                        self.map[int(command[2]) - 1][int(command[3])] = \
                            creature.base.name
                        self.map[int(command[2])][int(command[3]) + 1] = \
                            creature.base.name
                        self.map[int(command[2]) - 1][int(command[3]) + 1] = \
                            creature.base.name
                        army.army_on_field += [[int(command[2]),
                                                int(command[3])]]
                        creature.base.position_on_battle_ground = [int(
                            command[2]), int(command[3])]
                        print("Creature was placed on coordinates:\n x" + \
                              (command[2]) + " y " + command[3] + \
                              "\nx" + str(int(command[2]) - 1) + " y 1\n" + \
                              "x" + str(int(command[2]) - 1) + " y 0\n" + \
                              "x" + str(int(command[2]) - 1) + " y 1\n")
                else:
                    if int(command[3]) > borders[0 if first_army_turn else
                    1][1][1] or \
                            int(command[3]) < borders[0 if first_army_turn
                    else 1][1][0] or \
                            int(command[2]) < 0 or int(command[2]) > 9:
                        print("Wrong place")
                        self.message_ = "Wrong place"
                    elif self.map[int(command[2])][int(command[3])] is not \
                            None:
                        print("Wrong place to put")
                        self.message_ = "Wrong place to put"
                        return next_player
                    else:
                        army.stash.pop(int(command[1]))
                        army.army_on_field += [[int(command[2]),
                                                int(command[3])]]
                        self.map[int(command[2])][int(command[3])] = \
                            creature.base.name
                        creature.base.position_on_battle_ground = [int(
                            command[2]), int(command[3])]
                        print("Creature was placed on coordinates:\n x" + \
                              (command[2]) + " y " + command[3])
        elif command[0] == "move":
            if self.map[int(command[1])][int(command[2])] is None:
                print("Wrong from coordinates")
                self.message_ = "Wrong from coordinates"
            else:
                if [int(command[1]), int(command[2])] in army.army_on_field:
                    if command[3] == "stash":
                        for creature in army.current_army:
                            if creature.base.name == \
                                    self.map[int(command[1])][int(command[2])]:
                                army.stash += [creature]
                                self.map[int(command[1])][int(command[2])] = \
                                    None
                                creature.base.position_on_battle_ground \
                                    = None
                                if creature.base.length == 2:
                                    self.map[int(command[1]) - 1][int(
                                        command[2])] = None
                                    self.map[int(command[1]) - 1][int(
                                        command[2]) + 1] = None
                                    self.map[int(command[1])][int(
                                        command[2]) + 1] = None
                                army.army_on_field.pop(
                                    army.army_on_field.index([int(command[1]),
                                                              int(command[2])])
                                )
                                return next_player
                        print("Wrong creature")
                        self.message_ = "Wrong creature"
                    elif command[3] == "to":
                        if self.map[int(command[4])][int(command[5])] is not \
                                None or \
                                int(command[4]) > borders[0 if first_army_turn
                        else 1][0][1] or \
                                int(command[4]) < borders[0 if first_army_turn
                        else 1][0][0] or \
                                int(command[5]) > borders[0 if first_army_turn
                        else 1][1][1] or \
                                int(command[5]) < borders[0 if first_army_turn
                        else 1][1][0]:
                            print("Wrong place to put")
                            self.message_ = "Wrong place to put"
                            return next_player
                        for creature in army.current_army:
                            if creature.base.name == \
                                    self.map[int(command[1])][int(command[2])]:
                                self.move_creature(creature,
                                                   int(command[1]),
                                                   int(command[2]),
                                                   int(command[4]),
                                                   int(command[5]))
                                return next_player
                        print("Wrong creature")
                        self.message_ = "Wrong creature"
                    else:
                        print("Wrong command")
                        self.message_ = "Wrong command"
                else:
                    print("Wrong creature")
                    self.message_ = "Wrong creature"
        elif command[0] == "end":
            next_player = True
        else:
            print("Wrong command")
            self.message_ = "Wrong command"
        return next_player

    def preparing(self):
        print(
            '''Preparing phase was activated
        use commands:
         stash number_of_creature_in_stash x_coord y_coord
         move x_from y_from to x_to y_to
         move x_from y_from stash
         end
         ''')
        for creature in self.first_army_status.current_army:
            self.first_army_status.stash += [creature]
        for creature in self.second_army_status.current_army:
            self.second_army_status.stash += [creature]
        continuing = True
        first_player = True
        while continuing:
            try:
                names = []
                print("Your stash:", end=" ")
                if first_player:
                    for creatures in self.first_army_status.current_army:
                        names += [creatures.base.name]
                    for creature in self.first_army_status.stash:
                        print(creature.base.name, end="|")
                    buttons_list = choose_units_to_kill(
                        self.window,
                        self.fullscreen,
                        self.first_army_status.stash
                    )
                else:
                    for creatures in self.second_army_status.current_army:
                        names += [creatures.base.name]
                    buttons_list = choose_units_to_kill(
                        self.window,
                        self.fullscreen,
                        self.second_army_status.stash
                    )
                    for creature in self.second_army_status.stash:
                        print(creature.base.name, end="|")
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
                map_draw(self.window, self.map, self.fullscreen, self.message_)
                wait_, click1, click2, mouse_x1, mouse_y1, mouse_x2, mouse_y2 = wait(
                    buttons_list)
                command, self.message_ = worker_after_wait_for_preparing(wait_, click1, click2,
                                                          mouse_x1, mouse_y1,
                                                          mouse_x2, mouse_y2,
                                                          names, self.window)
                while command == "Nothing happened":
                    wait_, click1, click2, mouse_x1, mouse_y1, mouse_x2, mouse_y2 = wait(
                    buttons_list)
                    command, self.message_ = worker_after_wait_for_preparing(wait_, click1, click2,
                                                          mouse_x1, mouse_y1,
                                                          mouse_x2, mouse_y2,
                                                          names, self.window)
                command = command.split()
                if first_player:
                    next_player = self.work_with_command(
                        self.first_army_status,
                        command)
                    if next_player:
                        first_player = False
                else:
                    next_player = self.work_with_command(
                        self.second_army_status,
                        command, False)
                    if next_player:
                        self.make_queue()
                        return
                #self.message_ = ""
            except Exception:
                print("wrong command")
                self.message_ = "Wrong command"
    def make_queue(self):
        all_army = self.first_army_status.army_on_field + \
                   self.second_army_status.army_on_field
        while len(all_army) != 0:
            self.queue_of_creatures += [all_army.pop(randint(0,
                                                             len(all_army) -
                                                             1))]

    def move_creature(self, creature, coordinate_x, coordinate_y,
                      coordinate_x_to, coordinate_y_to):
        if not in_borders([coordinate_x, coordinate_y]) or \
                not in_borders([coordinate_x_to, coordinate_y_to]):
            print("Wrong to coordinates")
            self.message_ = "Wrong o coordinates"
            return
        if creature.base.length == 2:
            if coordinate_y_to >= 11 or coordinate_y_to < 0 or \
                    coordinate_x_to < 1 or coordinate_x_to > 9:
                print("Wrong to coordinates")
                self.message_ = "Wrong o coordinates"
                return
        self.map[coordinate_x][coordinate_y] = None
        self.map[coordinate_x_to][coordinate_y_to] = creature.base.name
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
        if creature.base.length == 2:
            self.map[coordinate_x][coordinate_y + 1] = None
            self.map[coordinate_x_to][coordinate_y_to + 1] = creature.base.name
            self.map[coordinate_x - 1][coordinate_y + 1] = None
            self.map[coordinate_x_to - 1][coordinate_y_to + 1] = \
                creature.base.name
            self.map[coordinate_x - 1][coordinate_y] = None
            self.map[coordinate_x_to - 1][coordinate_y_to] = creature.base.name
        return creature.move([coordinate_x_to, coordinate_y_to])

    def next_turn(self, creature):
        self.queue_of_creatures.pop(0)
        if int(len(
                self.queue_of_creatures) * 10 / creature.base.initiative) == 0:
            self.queue_of_creatures.insert(
                1,
                creature.base.position_on_battle_ground
            )
        else:
            self.queue_of_creatures.insert(int(len(
                self.queue_of_creatures) * 10 / creature.base.initiative),
                                           creature.base.position_on_battle_ground)
        for key in creature.base.improvement_duration.keys():
            if creature.base.improvement_duration[key] > 0:
                creature.base.improvement_duration[key] -= 1
                if creature.base.improvement_duration[key] == 0:
                    creature.base.__setattr__(
                        creature.base.improvement_characteristics[key][0],
                        creature.base.__getattribute__(
                            creature.base.improvement_characteristics[key][0]
                        ) - creature.base.improvement_characteristics[key][1]
                    )

    def battle(self):
        self.preparing()
        first_win = True
        print("Battle was begun")
        self.message_ = "Battle was begun"
        while len(self.first_army_status.army_on_field) != 0 and len(
                self.second_army_status.army_on_field) != 0:
            '''try:'''
            tmp = self.queue_of_creatures[0]
            print(tmp)
            print(self.map[tmp[0]][tmp[1]] + " turn")
            print('''Use commands:
            move x_to y_to
            attack x_attacked y_attacked
            move_attack x_to y_to x_attacked y_attacked
            wait
            defend
            exit''')
            creature = None
            buttons = draw_commans(self.window, self.fullscreen)
            if tmp in self.first_army_status.army_on_field:
                army = self.first_army_status
                attacked_army = self.second_army_status
            else:
                army = self.second_army_status
                attacked_army = self.first_army_status
            for soldier in army.current_army:
                if soldier.base.name == self.map[tmp[0]][tmp[1]]:
                    creature = soldier
            if hasattr(creature, "range_attack") and \
                    creature.base.shots != 0 and \
                    creature.base.shots is not None:
                print("\trange_attack attacked_creature_coordinate_x y")
            print(creature.base.position_on_battle_ground)
            map_draw(self.window, self.map, self.fullscreen, self.message_)
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    if self.map[i][j] is None:
                        if abs(creature.base.position_on_battle_ground[0] -
                               i) + \
                                abs(
                                    creature.base.position_on_battle_ground[
                                        1] - j) <= \
                                creature.base.speed:
                            print("%s" % "|____++____|", end=" ")
                            draw_green_cell(self.window, i, j)
                        else:
                            print("%s" % "|__________|", end=" ")
                    else:
                        print("%s" % self.map[i][j].center(12), end=" ")
                print()

            com = waaar(buttons, ["move", "attack", "move_attack",
                                  "Wait", "Defend", "Exit", "range_attack"])
            com = com.split()
            if com[0] == "move":
                if (abs(int(com[1]) - int(tmp[0])) +
                    abs(int(com[2]) - int(tmp[1]))) > creature.base.speed:
                    print("Can't move so far")
                    self.message_ = "Can't move so far"
                    continue
                print(
                    self.move_creature(creature, int(tmp[0]), int(tmp[1]),
                                       int(com[1]), int(com[2])))
                self.next_turn(creature)
            elif com[0] == "move_attack":
                if (abs(int(com[1]) - int(tmp[0])) +
                    abs(int(com[2]) - int(tmp[1]))) > creature.base.speed:
                    print("Can't move so far")
                    self.message_ = "Can't move so far"
                    continue
                if creature.base.length == 1:
                    if abs(int(com[3]) - int(com[1])) > 1 or \
                            abs(int(com[4]) - int(com[2])) > 1:
                        print("Can't attack so far", creature.base.length)
                        continue
                else:
                    if not (abs(int(com[3]) - int(com[1])) <= 1 and
                            abs(int(com[4]) - int(com[2])) <= 1 or
                            abs(int(com[3]) - int(com[1]) - 1) <= 1 and
                            abs(int(com[4]) - int(com[2])) <= 1 or
                            abs(int(com[3]) - int(com[1]) - 1) <= 1 and
                            abs(int(com[4]) - int(com[2]) + 1) <= 1 or
                            abs(int(com[3]) - int(com[1])) <= 1 and
                            abs(int(com[4]) - int(com[2]) + 1) <= 1):
                        print("Can't attack so far", creature.base.length)
                        continue
                attacked_creature = None
                for soldier in attacked_army.current_army:
                    if soldier.base.name == self.map[int(com[3])][
                        int(com[4])]:
                        attacked_creature = soldier
                if attacked_creature is None:
                    print("Wrong target.")
                    self.message_ = "Wrong target"
                    continue
                else:
                    self.map[tmp[0]][tmp[1]] = None
                    self.map[int(com[1])][int(com[2])] = creature.base.name
                    if creature.base.length == 2:
                        self.map[tmp[0] - 1][tmp[1]] = None
                        self.map[int(com[1]) - 1][int(com[2])] = \
                            creature.base.name
                        self.map[tmp[0] - 1][tmp[1] + 1] = None
                        self.map[int(com[1]) - 1][int(com[2]) + 1] = \
                            creature.base.name
                        self.map[tmp[0]][tmp[1] + 1] = None
                        self.map[int(com[1])][int(com[2]) + 1] = \
                            creature.base.name
                    self.queue_of_creatures[
                        self.queue_of_creatures.index(tmp)
                    ] = [int(com[1]), int(com[2])]
                    army.army_on_field[army.army_on_field.index(tmp)] = [
                        int(com[1]), int(com[2])]
                    tmp2 = attacked_creature.base.position_on_battle_ground
                    attacked_creature.base.position_on_battle_ground = [int(
                        com[3]), int(com[4])]
                    message = creature.move_and_melee_attack(
                        attacked_creature,
                        [int(com[1]), int(com[2])],
                        army,
                        attacked_army
                    )
                    attacked_creature.base.position_on_battle_ground = tmp2
                    print(message[0])
                    self.use_info_from_message(message[1::], army,
                                               attacked_army)
                    self.next_turn(creature)
            elif com[0] == "exit":
                if army == self.first_army_status:
                    first_win = False
                else:
                    first_win = True
                break
            elif com[0] == "range_attack":
                if creature.base.shots == 0 or creature.base.shots is None:
                    print("could't attack on distance")
                    self.message_ = "Could't attack on distance"
                    continue
                attacked_creature = None
                for soldier in attacked_army.current_army:
                    if soldier.base.name == self.map[int(com[1])][
                        int(com[2])]:
                        attacked_creature = soldier
                if attacked_creature is None:
                    print("Wrong target.")
                    self.message_ = "Wrong target"
                    continue
                else:
                    message = creature.range_attack(attacked_creature,
                                                    attacked_army)
                    self.use_info_from_message(message, army,
                                               attacked_army)
                    self.next_turn(creature)
            elif com[0] == "attack":
                if creature.base.length == 1:
                    if abs(int(com[1]) - tmp[0]) > 1 or \
                            abs(int(com[2]) - tmp[1]) > 1:
                        print("Can't attack so far")
                        self.message_ = "Can't attack so far"
                        continue
                else:
                    if not (abs(int(com[1]) - tmp[0]) <= 1 and
                            abs(int(com[2]) - tmp[1]) <= 1 or
                            abs(int(com[1]) - tmp[0] - 1) <= 1 and
                            abs(int(com[2]) - tmp[1]) <= 1 or
                            abs(int(com[1]) - tmp[0] - 1) <= 1 and
                            abs(int(com[2]) - tmp[1] + 1) <= 1 or
                            abs(int(com[1]) - tmp[0]) <= 1 and
                            abs(int(com[2]) - tmp[1] + 1) <= 1):
                        print("Can't attack so far")
                        self.message_ = "Can't attack so far"
                        continue
                attacked_creature = None
                for soldier in attacked_army.current_army:
                    if soldier.base.name == self.map[int(com[1])][
                        int(com[2])]:
                        attacked_creature = soldier
                if attacked_creature is None:
                    print("Wrong target.")
                    self.message_ = "Wrong target"
                    continue
                else:
                    message = creature.melee_attack(attacked_creature,
                                                    army,
                                                    attacked_army)
                    self.use_info_from_message(message, army,
                                               attacked_army)
                    self.next_turn(creature)
            elif com[0] == "wait":
                print(creature.wait())
                self.next_turn(creature)
            elif com[0] == "defend":
                print(creature.defend())
                self.next_turn(creature)
            else:
                print("wrong command")
                self.message_ = "Wrong command"
        if len(self.first_army_status.army_on_field) == 0:
            first_win = False
        if len(self.second_army_status.army_on_field) == 0:
            first_win = True
        self.end_battle()
        print("The game was ended")
        return first_win

    def end_battle(self):
        if self.first_army_status.hero is not None:
            first_names = []
            for creature in self.first_army_status.starting_army:
                first_names += [creature.name]
            for name in self.deleted_from_first:
                self.first_army_status.starting_army.pop(
                    first_names.index(name)
                )
                first_names.pop(first_names.index(name))

        if self.second_army_status.hero is not None:
            second_names = []
            for creature in self.first_army_status.starting_army:
                second_names += [creature.name]
            for name in self.deleted_from_second:
                self.second_army_status.starting_army.pop(
                    second_names.index(name)
                )
                second_names.pop(second_names.index(name))
