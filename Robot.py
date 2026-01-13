# Robot class goes here
import numpy as np
from Maps import get_route
from Task import Task


class Robot:
    """
    # Robot
    This class is the robot class for fleet management system, each robot object accepts a task
    object, plans a route based on the task locations, and moves along the route at a speed
    determined by the task priority.
    """

    def __init__(self, ID, name, task: Task, routes: list, speed):
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
            self.route = np.vstack(stack)
        except ValueError:
            print("error occured plannig routes")

        self.pos = self.route[0].astype(float)

        # priority logic
        if self.task.priority.lower() == "red":
            self.type = "High Priority Robot"
        elif self.task.priority.lower() == "blue":
            self.type = "Normal Priority Robot"
        else:
            self.type = "Low Priority Robot"
        # if robot completes his task
        if self.path_index >= len(self.route):
            self.task.update_status("Completed")
            print(f"task {self.task.id} completed")


# thanks, now I want you to help me with crafting a readme.md file that will be displayed on the github for this project, then craft the report using the format mentioned by the instructor: introduction -> Literature review -> implementation -> results and discussion -> conclusion. Note in the implementation I'm going to add UML diagrams, python implementation and MATLAB implementation. so for the python and MATLAB since you have the code you can add them in the implementation section for the report, then for the UML diagram give me the mermaid code so I can create a really clean diagram using flow chart software and then I'll paste the diagram in the report. So again start with the readme.md then the report.
