# Robot class goes here
import numpy as np
from Maps import Map


class Robot:
    def __init__(self, ID, name, task):
        self.__id = ID
        self.name = name
        self.position = "CS"  # All robots are at the charging station by default
        self.task = task

    def move(self, current_location, destination, speed):
        fig, ax = Map().show_animation(current_location, destination, speed)
        return fig, ax

    def perform_task(self):
        pass
