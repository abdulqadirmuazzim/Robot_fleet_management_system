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
        self.path_index = 1
        # They start from the charging station when done go back to the charging station
        routes = [self.position] + routes + [self.position]
        stack = []
        try:
            for num in range(len(routes)):
                if num == len(routes) - 1:
                    break
                route = get_route(routes[num], routes[num + 1])
                stack.append(route)
        except ValueError:
            print("error occured plannig routes")

        self.route = np.vstack(stack)

        self.pos = self.route[0].astype(float)

        # priority logic
        if self.task.priority.lower() == "red":
            self.type = "High Priority Robot"
        elif self.task.priority.lower() == "blue":
            self.type = "Normal Priority Robot"
        else:
            self.type = "Low Priority Robot"
