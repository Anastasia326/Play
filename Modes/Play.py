from collections import deque

import pygame

from ArmyForDuel.Sverchok_army import Swerchok_army
from ArmyForDuel.Zexir_army import Zexir_army
from Battle.Battle_ import Battle
from Battle.army import Army
from Map.Medium import MediumMap
from Map.Quick import QuickMap
from Map.Work_with_resources.City import City
from Map.Work_with_resources.Hero_resouces import Resources
from Map.Work_with_resources.Miner import Miner
from Map.imports import ways, resources, building_array, improving_skills_list, \
    miner_array, building_in_city_types, building_in_city_cost
from Working_with_textures.drow_map import drow_map
from Working_with_textures.wait_klick import wait_klick


class Play:
    def __init__(self, first: Army, second: Army, Mode: str, window,
                 fullscreen):
        self.window = window
        self.fullscreen = fullscreen
        self.first_army = first
        self.first_resources = Resources(first.hero.name)
        self.second_resources = Resources(second.hero.name)
        self.first_city = City(first.hero.name, self.first_resources)
        self.second_city = City(second.hero.name, self.second_resources)
        self.second_army = second
        if Mode == "Quick":
            M = QuickMap(self.first_army, self.second_army)
            self.Map = M.Map
            self.first_neutral_army = M.neutral_first
            self.second_neutral_army = M.neutral_second
        else:
            M = MediumMap(self.first_army, self.second_army)
            self.Map = M.Map
            self.first_neutral_army = M.neutral_first
            self.second_neutral_army = M.neutral_second
        self.miners = []
        for i in range(len(self.Map)):
            for j in range(len(self.Map[0])):
                if self.Map[i][j] in miner_array:
                    miner = Miner(self.Map[i][j], [i, j])
                    miner.add_hero_resources(self.first_resources)
                    miner.add_hero_resources(self.second_resources)
                    self.miners += [miner]
        self.first_player_turn = True
        self.day = 0
        self.playing()

    def playing(self):
        button_list = []
        hero_coordinads = []
        for i in range(len(self.Map)):
            for j in range(len(self.Map[0])):
                if self.first_player_turn:
                    if self.Map[i][j] == self.first_army.hero.name:
                        button_list = drow_map(window, False, "grass", "Quick",
                                               i, j, self.Map)
                        hero_coordinads = [i, j]
                        break
                else:
                    if self.Map[i][j] == self.second_army.hero.name:
                        button_list = drow_map(window, False, "grass", "Quick",
                                               i, j, self.Map)
                        hero_coordinads = [i, j]
                        break
        command = [""]
        while command[0] != "end" and command[0] != "Exit":
            command = wait_klick(button_list, 800, 600)
            print(command)
            command = command.split()
            if command[0] == "move":
                path = self.make_path([hero_coordinads[0], hero_coordinads[1]],
                                      [int(command[1]), int(command[2])])
                if self.first_player_turn:
                    self.move(path, self.first_army.hero.name)
                else:
                    self.move(path, self.second_army.hero.name)
                for i in range(len(self.Map)):
                    for j in range(len(self.Map[0])):
                        print(self.Map[i][j].center(15), end=" ")
                    print()
                print("___________________")
                for i in range(len(self.Map)):
                    for j in range(len(self.Map[0])):
                        if self.first_player_turn:
                            if self.Map[i][j] == self.first_army.hero.name:
                                button_list = drow_map(window,
                                                       False,
                                                       "grass",
                                                       "Quick",
                                                       i, j, self.Map)
                                hero_coordinads = [i, j]
                                break
                        else:
                            if self.Map[i][j] == self.second_army.hero.name:
                                button_list = drow_map(window, False,
                                                       "grass", "Quick",
                                                       i, j, self.Map)
                                hero_coordinads = [i, j]
                                break
            else:
                print("command is not move in playing")
        print("left")
        if command[0] != "Exit":
            self.next_turn()
        else:
            self.end()

    def next_turn(self):
        if self.first_player_turn:
            self.first_resources.next_turn()
            self.first_player_turn = False
            self.day += 1
        else:
            self.second_resources.next_turn()
            self.first_player_turn = True
            if self.day == 7:
                self.day = 0
                self.first_city.next_week()
                self.second_city.next_week()
        self.playing()

    def move(self, path, hero_name):
        walked_points = 0
        cur_pos = [0, 0]
        print(path)
        if len(path) > 1:
            while walked_points < self.first_army.hero.movement and cur_pos != \
                    path[1]:
                walked_points += 1
                cur_pos = path[- walked_points]
                if walked_points != 1:
                    self.Map[path[-walked_points + 1][0]][path[-walked_points + 1][
                        1]] = "Road"
                self.Map[cur_pos[0]][cur_pos[1]] = hero_name
                drow_map(window, False, "grass", "Quick", cur_pos[0], cur_pos[
                    1], self.Map)
            print(self.Map[path[0][0]][path[0][1]])
            if self.Map[path[0][0]][path[0][1]] == "Road":
                self.Map[path[1][0]][path[1][1]] = "Road"
                self.Map[path[0][0]][path[0][1]] = hero_name
            elif self.Map[path[0][0]][path[0][1]] in resources:
                string = self.Map[path[0][0]][path[0][1]].split("Count")
                if self.first_player_turn:
                    self.first_resources.add_resource(string[0], string[1])
                else:
                    self.second_resources.add_resource(string[0], string[1])
            elif self.Map[path[0][0]][path[0][1]] in building_array:
                print("in buildings")
                if self.first_player_turn:
                    print(self.first_army.hero.improve_skill(
                        improving_skills_list[
                            building_array.index(
                                self.Map[path[0][0]][path[0][1]])
                        ],
                        2
                    ))
                else:
                    print(self.second_army.hero.improve_skill(
                        improving_skills_list[
                            building_array.index(
                                self.Map[path[0][0]][path[0][1]])
                        ],
                        2
                    ))
                self.Map[path[0][0]][path[0][1]] = "Road"
            elif self.Map[path[0][0]][path[0][1]] in miner_array:
                for miner in self.miners:
                    if miner.position_on_map == [path[0][0], path[0][1]]:
                        if self.first_player_turn:
                            miner.get_under_control(self.first_army.hero.name)
                        else:
                            miner.get_under_control(self.second_army.hero.name)
                        break
            elif "City" in self.Map[path[0][0]][path[0][1]]:
                if self.first_player_turn:
                    if "Second" in self.Map[path[0][0]][path[0][1]]:
                        self.Map[path[0][0]][path[0][1]] = "Road"
                        self.first_resources.add_resource("Gold", 10000)
                    else:
                        self.enter_city(self.first_city, self.first_army)
                else:
                    if "First" in self.Map[path[0][0]][path[0][1]]:
                        self.Map[path[0][0]][path[0][1]] = "Road"
                        self.first_resources.add_resource("Gold", 10000)
                    else:
                        self.enter_city(self.first_city, self.second_army)
            elif self.Map[path[0][0]][path[0][1]] == self.second_army.hero.name \
                    and self.first_player_turn or \
                    self.Map[path[0][0]][
                        path[0][1]] == self.second_army.hero.name \
                    and not self.first_player_turn:
                battle = Battle(self.first_army, self.second_army, self.window,
                                self.fullscreen)
                if battle.battle():
                    print("First Win")
                    self.end()
                else:
                    print("Second Win")
                    self.end()
            else:
                neutral_army = None
                print("fight")
                for creature in self.first_neutral_army.creatures:
                    if creature.name == self.Map[path[0][0]][path[0][1]]:
                        neutral_army = Army(None, [creature])
                        break
                for creature in self.second_neutral_army.creatures:
                    if creature.name == self.Map[path[0][0]][path[0][1]]:
                        neutral_army = Army(None, [creature])
                        break
                if neutral_army is not None:
                    if self.first_player_turn:
                        if Battle(self.first_army, neutral_army,
                                  self.window, self.fullscreen).battle():
                            print("Win")
                            self.Map[path[0][0]][path[0][1]] = \
                                self.first_army.hero.name
                            self.Map[path[1][0]][path[1][1]] = "Road"
                        else:
                            print("Loose")
                            self.end()
                    else:
                        if Battle(self.second_army, neutral_army,
                                  self.window, self.fullscreen).battle():
                            print("Win")
                            self.Map[path[0][0]][path[0][1]] = \
                                self.second_army.hero.name
                            self.Map[path[1][0]][path[1][1]] = "Road"
                        else:
                            print("Loose")
                            self.end()

    def enter_city(self, city: City, army: Army):
        '''
        show_city_menu() - nado меню города(в самом простом варианте - меню
        есть возможность улучшить здание или нанять солдат,
        предлагаю слева 7 вариантов построек. Справа перечислины бойцы и число
        сколько можно нанять, при этом можно располагать бойцов напротив
        соответствующих зданий. Если уровень строения 0 - бойцов нельзя нанять
        если 1 - только не улучшенных, если 2 - можно и улучшенных
        есть еще возможность улучшать существо, если хватает денег и есть
        здание 2 уровня соответствующие)
        '''
        while True:
            command = input()  # here must be click
            command = command.split()
            if command[0] == "exit":
                return
            elif command[0] == "upgrade":
                if command[1] not in building_in_city_types:
                    for creature in army.soldiers:
                        if creature.name == command[1]:
                            if creature.upgrade_cost is not None:
                                required = [
                                    creature.upgrade_cost * creature.count
                                ]
                                required += [0, 0, 0, 0, 0]
                                if hasattr(creature, "special_resource"):
                                    required[
                                        resources.index(
                                            creature.special_resource
                                        )
                                    ] = creature.count
                                if city.able_resources.can_do(required):
                                    city.upgrade_units(creature)
                else:
                    city.able_resources.can_do(
                        building_in_city_cost[
                            building_in_city_types.index(command[1])
                        ]
                    )
            elif command[0] == "buy":
                pass
            else:
                print("Wrong command")

    def make_path(self, coordinates_from, coordinates_to):
        print("make path")
        if 10 <= coordinates_from[0] <= 39:
            coordinates_to[0] += coordinates_from[0] - 10
        elif coordinates_from[0] > 39:
            coordinates_to[0] += 28
        print(coordinates_from)
        print(coordinates_to)
        curr_coord = coordinates_from
        parent_map = [[]]
        queue = deque()
        add_counter, wave_counter = 0, 1
        queue.append(curr_coord)
        for i in range(len(self.Map[0])):
            parent_map[0] += [[-1, -1]]
        for j in range(len(self.Map)):
            parent_map += [parent_map[0][::]]
        while curr_coord != coordinates_to and \
                not len(queue) == 0:
            if wave_counter == 0:
                wave_counter = add_counter

            curr_coord = queue.popleft()
            wave_counter -= 1

            for i in range(8):
                tmp = [curr_coord[0] + ways[i][0], curr_coord[1] + ways[i][1]]
                if (0 < tmp[0] < len(self.Map) - 1 and 0 < tmp[1] < len(
                        self.Map[0]) - 1 and
                    self.Map[tmp[0]][tmp[1]] == "Road" or
                    tmp == coordinates_to) and parent_map[tmp[0]][tmp[1]] == \
                        [-1, -1]:

                    if tmp == coordinates_to:
                        print(self.Map[coordinates_to[0]][coordinates_to[1]])
                        if self.Map[coordinates_to[0]][coordinates_to[1]] == \
                                "NoWay":
                            coordinates_to = curr_coord
                        else:
                            parent_map[tmp[0]][tmp[1]] = curr_coord
                    else:
                        parent_map[tmp[0]][tmp[1]] = curr_coord
                        queue.append(tmp)
                        add_counter += 1

        if parent_map[coordinates_to[0]][coordinates_to[1]] == [-1, -1]:
            return []
        else:
            curr_coord = coordinates_to
            path = []
            while curr_coord != coordinates_from:
                path += [curr_coord]
                curr_coord = parent_map[curr_coord[0]][curr_coord[1]]
            path += [coordinates_from]
            return path

    def end(self):
        pygame.quit()


first_army = Swerchok_army
second_army = Zexir_army
pygame.init()
window = pygame.display.set_mode((800, 600))
Play(first_army, second_army, "Quick", window, False)
