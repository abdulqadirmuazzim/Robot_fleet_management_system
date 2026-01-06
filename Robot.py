# Robot class goes here
import numpy as np
from Maps import get_route


class Robot:
    def __init__(self, ID, name, task, routes: list, speed):
        self.__id = ID
        self.name = name
        self.position = "CS"  # All robots are at the charging station by default
        self.task = task
        self.speed = speed
        routes = [self.position] + routes
        stack = []
        for num in range(len(routes)):
            if num == len(routes) - 1:
                break
            route = get_route(routes[num], routes[num + 1])
            stack.append(route)

        self.route = np.vstack(stack)
