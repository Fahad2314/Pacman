# sampleAgents.py
# parsons/07-oct-2017
#
# Version 1.1
#
# Some simple agents to work with the PacMan AI projects from:
#
# http://ai.berkeley.edu/
#
# These use a simple API that allow us to control Pacman's interaction with
# the environment adding a layer on top of the AI Berkeley code.
#
# As required by the licensing agreement for the PacMan AI we have:
#
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# The agents here are extensions written by Simon Parsons, based on the code in
# pacmanAgents.py

from pacman import Directions
from game import Agent
import api
import random
import game
import util
import collections

# RandomAgent
#
# A very simple agent. Just makes a random pick every time that it is
# asked for an action.

# SensingAgent
#
# Doesn't move, but reports sensory data available to Pacman
class PartialAgent(Agent):
    def __init__(self):
        self.flag = 0
        self.counter = 0
        # persistent food list that pacman sees as he travels the grid
        self.food_list = list()
        # persistent list which follows pacmans footsetps
        self.pacman_steps = list()
        
        # list containing food which is not in pacmans steps so he does not unnecessarily go over his steps in search for food
    def final(self,state):
        self.flag = 0
        self.counter = 0
        self.food_list = list()
        self.pacman_steps = list()
        
    def getAction(self, state):
        corners = api.corners(state)
        wall_location = api.walls(state)
        my_location = api.whereAmI(state)
        food_location = api.food(state)
        ghost_location = api.ghosts(state)
        
        
        

        global flag
        global food_list
        global pacman_steps
        global counter
        global goal
        
        if ghost_location:
            legal = api.legalActions(state)
            
            
            for ghost in ghost_location:
                dist_to_ghost= util.manhattanDistance(my_location,ghost)
                print("manhattan distance:", dist_to_ghost)
                print("Ghost coordinates:", ghost)
                if dist_to_ghost <=3 :
                    pathlist_to_ghost = self.bfs(my_location,ghost,wall_location)
                    print("pathlist to ghost", pathlist_to_ghost)
                    if pathlist_to_ghost:
                        
                        banned = pathlist_to_ghost[1]
                        if banned[0] > my_location[0]:
                            legal.remove(Directions.EAST)
                            if Directions.WEST in legal: 
                                return api.makeMove(Directions.WEST,legal)
                            else:
                                return api.makeMove(random.choice(legal),legal)
                        elif banned[0] < my_location[0]:
                            legal.remove(Directions.WEST)
                            if Directions.EAST in legal:
                                return api.makeMove(Directions.EAST,legal)
                            else:
                                return api.makeMove(random.choice(legal),legal)
                        elif banned[1] > my_location[1]:
                            legal.remove(Directions.NORTH)
                            if Directions.SOUTH in legal:
                                return api.makeMove(Directions.SOUTH,legal)
                            else:
                                return api.makeMove(random.choice(legal),legal)
                        elif banned[1] < my_location[1]:
                            legal.remove(Directions.SOUTH)
                            if Directions.NORTH in legal:
                                return api.makeMove(Directions.NORTH,legal)
                            else:
                                return api.makeMove(random.choice(legal),legal)
                        else:
                            return api.makeMove(Directions.STOP,legal)
                       
                        
                        
 
        
                

        if self.flag == 0:
            # set self flag == 0
            print("Flag is 0")
            #raw_input("Press Enter")
            legal = api.legalActions(state)
            # increase self flag so that the getAction will return the next if block

            x, y = corners[0]
            # bottom left
            x = x + 1
            y = y + 1
            goal = (x, y)
            if goal not in wall_location:
                pathlist = self.bfs(my_location, goal, wall_location)
                direc = self.mapRoute(my_location, pathlist, legal, self.flag)

                # print("Food visible:", food_location)
                # add all visible food to the persistent food_location variable
                for food in food_location:
                    # print(food)
                    if food not in self.food_list:
                        self.food_list.append(food)
                # add every location that pacman is ever at to the persistent pacman_steps list
                self.pacman_steps.append(my_location)

                print("pacman location", my_location)
                print("direc:", direc)
                return api.makeMove(direc, legal)
            else:
                self.flag = 1

        if self.flag == 1:

            print("Flag is 1")
            #raw_input("Press Enter")
            legal = api.legalActions(state)
            # increase self flag so that the getAction will return the next if block

            x, y = corners[2]
            # top left
            x = x + 1
            y = y - 1
            goal = (x, y)
            if goal not in wall_location:
                pathlist = self.bfs(my_location, goal, wall_location)
                direc = self.mapRoute(my_location, pathlist, legal, self.flag)
                # updates the food_list a persistent list of food that pacman see's on his travels
                print("Food visible:", food_location)
                for food in food_location:
                    # print(food)
                    if food not in self.food_list:
                        self.food_list.append(food)
                self.pacman_steps.append(my_location)

                print("pacman location", my_location)
                print("direc:", direc)
                return api.makeMove(direc, legal)

            else:
                self.flag = 2

        if self.flag == 2:
            print("Flag is 2")
            #raw_input("Press Enter")
            legal = api.legalActions(state)

            x, y = corners[3]
            # top right
            x = x - 1
            y = y - 1
            goal = (x, y)
            if goal not in wall_location:
                pathlist = self.bfs(my_location, goal, wall_location)
                direc = self.mapRoute(my_location, pathlist, legal, self.flag)

                for food in food_location:
                    # print(food)
                    if food not in self.food_list:
                        self.food_list.append(food)
                self.pacman_steps.append(my_location)

                print("pacman location", my_location)
                print("direc:", direc)
                return api.makeMove(direc, legal)
            else:
                self.flag = 3

        if self.flag == 3:
            print("Flag is 3")
            #raw_input("Press Enter")
            legal = api.legalActions(state)

            x, y = corners[1]
            # bottom right
            x = x - 1
            y = y + 1
            goal = (x, y)
            if goal not in wall_location:
                # pathlist is the bfs which returns the path to the food location
                pathlist = self.bfs(my_location, goal, wall_location)
                # pass the bfs pathlist into the direc function
                direc = self.mapRoute(my_location, pathlist, legal, self.flag)

                # print("Food visible:", food_location)
                for food in food_location:
                    # print(food)
                    if food not in self.food_list:
                        self.food_list.append(food)

                self.pacman_steps.append(my_location)

                print("pacman location", my_location)
                print("direc:", direc)
                global remaining_food

                remaining_food = list(set(self.food_list) - set(self.pacman_steps))

                print("length of remaining food:", len(remaining_food))


                return api.makeMove(direc, legal)
            else:
                self.flag = 4
                return api.makeMove(Directions.STOP, legal)

        # loop through the list how many times it requires to end the remaining food list
        while self.flag >=4 :

            #raw_input("Press Enter")
            legal = api.legalActions(state)
            print("the final flag is ", self.flag)
            # # print("the counter is: ", self.counter)
            # print("THE GOAL IS :", goal)
            print("Ordered Food Remaining 1 ", remaining_food)
            self.pacman_steps.append(my_location)
            print self.pacman_steps
            remaining_food = list(set(self.food_list) - set(self.pacman_steps))
            # for fruit in remaining_food:
            #     dist_array=[]
            #     distance = util.manhattanDistance(my_location,fruit)
            #     dist_array.append(distance)
            #     x = dist_array.index(min(dist_array))

            remaining_food_with_distances = []
            for i in remaining_food:
                remaining_food_with_distances.append((i, util.manhattanDistance(my_location,i)))
            min = 1000
            for i in range(len(remaining_food_with_distances)):
                if remaining_food_with_distances[i][1] < min:
                    min = remaining_food_with_distances[i][1]
                    #global goal
                    goal = remaining_food_with_distances[i][0]
            #goal = remaining_food[0]
            print("Ordered Food Remaining 2 ", remaining_food)

            pathlist_f = self.bfs(my_location, goal, wall_location)
            print("PACMAN IS AT:", my_location)

            print("THE PATHLIST TO THE GOAL IS: ", pathlist_f)
            direc = self.mapRouteFinal(my_location, pathlist_f, legal, self.flag, self.counter)
            return api.makeMove(direc, legal)




    def mapRoute(self, current_location, next_location, legal, flag):
        # current location calls the api.whereAmI for pacman location, next_location is the pathlist
        next_location.pop(0)
        # removes the current location from the pathlist
        len_of_list = len(next_location)
        for i in range(len_of_list):

            # loop runs until the pathlist is empty
            if len_of_list > 1:
                # print(next_location)
                # print("Pacman was at :", current_location)
                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (1, 0):
                    print("Went East to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.EAST in legal:
                        return Directions.EAST
                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (
                -1, 0):
                    print("Went  West to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.WEST in legal:
                        return Directions.WEST
                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (0, 1):
                    print("Went  North to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.NORTH in legal:
                        return Directions.NORTH
                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (
                0, -1):
                    print("Went  South to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.SOUTH in legal:
                        return Directions.SOUTH
            if len_of_list == 1:
                print(next_location)
                print("steps left:", len_of_list)
                print("NEW FLAG !!!!!!")
                # self.flag =1
                self.flag = self.flag + 1

                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (1, 0):
                    print("Went East to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.EAST in legal:
                        return Directions.EAST
                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (
                -1, 0):
                    print("Went  West to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.WEST in legal:
                        return Directions.WEST
                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (0, 1):
                    print("Went  North to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.NORTH in legal:
                        return Directions.NORTH
                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (
                0, -1):
                    print("Went  South to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.SOUTH in legal:
                        return Directions.SOUTH

    def mapRouteFinal(self, current_location, next_location, legal, flag, counter):
        # current location calls the api.whereAmI for pacman location, next_location is the pathlist
        next_location.pop(0)
        # removes the current location from the pathlist
        len_of_list = len(next_location)
        for i in range(len_of_list):

            # loop runs until the pathlist is empty
            if len_of_list > 1:
                print(next_location)
                print("Pacman was at :", current_location)

                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (1, 0):
                    print("Went East to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.EAST in legal:
                        return Directions.EAST
                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (
                -1, 0):
                    print("Went  West to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.WEST in legal:
                        return Directions.WEST
                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (0, 1):
                    print("Went  North to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.NORTH in legal:
                        return Directions.NORTH
                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (
                0, -1):
                    print("Went  South to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.SOUTH in legal:
                        return Directions.SOUTH
            if len_of_list == 1:
                print(next_location)
                print("steps left:", len_of_list)
                print("NEW FLAG !!!!!!")
                # self.flag =1
                self.flag = self.flag + 1
                self.counter = self.counter + 1
                # print("new flag:", self.flag)
                #print("new counter:", self.counter)

                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (1, 0):
                    print("Went East to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.EAST in legal:
                        return Directions.EAST
                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (
                -1, 0):
                    print("Went  West to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.WEST in legal:
                        return Directions.WEST
                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (0, 1):
                    print("Went  North to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.NORTH in legal:
                        return Directions.NORTH
                if ((next_location[0][0] - current_location[0]), (next_location[0][1] - current_location[1])) == (
                0, -1):
                    print("Went  South to:", next_location[0])
                    print("steps left:", len_of_list)
                    if Directions.SOUTH in legal:
                        return Directions.SOUTH

    def mapRouteGhost(self, current_location, next_location, legal, flag):
        # current location calls the api.whereAmI for pacman location, next_location is the pathlist

        # removes the current location from the pathlist
        len_of_list = len(next_location)
        for i in range(len_of_list):
            if util.manhattanDistance(current_location, next_location[1]) == 2 :

                # loop runs until the pathlist is empty
                if next_location[1][0] > current_location[0]:
                    if Directions.EAST in legal:
                        return legal.remove("East")
                if next_location[1][0] < current_location[0]:
                    if Directions.WEST in legal:
                        return legal.remove("West")
                if next_location[1][1] > current_location[1]:
                    if Directions.NORTH in legal:
                        return legal.remove("North")
                if next_location[1][1] < current_location[1]:
                    if Directions.SOUTH in legal:
                        return legal.remove("South")

    def bfs(self, start, goal, wall_location):

        queue = collections.deque()
        visited = set()
        meta = dict()

        # initialize
        meta[start] = (None, None)
        # append the start/root to the queue for frontier
        queue.append(start)

        while queue:
            # current node is the current node being explored in the frontier from queue
            start = queue.popleft()
            # if the current node is the goal then call the construct_path function with current, and meta dict
            if start == goal:
                return (self.construct_path(start, meta, goal))

            # for child in current node
            for child, action in self.get_successor(start):

                if child in visited:
                    continue
                elif (child not in queue) and (child not in wall_location):
                    meta[child] = (start, action)
                    queue.append(child)

            visited.add(start)

            # print(visited)

    def get_successor(self, my_location):
        # create a list of children for the current location from pacman api
        # print(my_location)
        x, y = my_location
        children = []
        east = ((x + 1, y), (1, 0))
        west = ((x - 1, y), (-1, 0))
        north = ((x, y + 1), (0, 1))
        south = ((x, y - 1), (0, -1))
        children.append(east)
        children.append(west)
        children.append(north)
        children.append(south)
        # print(children)

        return children

    def construct_path(self, node, meta, goal):
        action_list = []
        while (meta[node][0] != None):
            node, action = meta[node]
            action_list.append(node)

        action_list.reverse()
        action_list = (action_list) + [goal]
        # print(action_list)
        return action_list

    def order_list(self, unordered_list):
        unordered_list.sort()
        unordered_list.reverse()
        return unordered_list


