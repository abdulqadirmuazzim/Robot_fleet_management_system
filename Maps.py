from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation as fa
from PIL import Image
import numpy as np


class Map:
    def __init__(self, **kwargs):
        self.routes = {
            "CS_DA": np.array([[45, 570], [45, 40], [410, 40]]),
            "DA_CS": np.array([[410, 70], [75, 70], [75, 570]]),
            "DA_WH": np.array([[570, 100], [570, 300]]),
            "WH_DA": np.array([[610, 300], [610, 100]]),
            "CS_WH": np.array([[120, 665], [475, 665], [475, 460]]),
            "WH_CS": np.array([[515, 460], [515, 700], [120, 700]]),
            "DA_DS": np.array([[735, 100], [735, 730]]),
            "DS_DA": np.array([[770, 730], [770, 100]]),
            "WH_DS": np.array([[600, 460], [600, 730]]),
            "DS_WH": np.array([[635, 730], [635, 460]]),
            "DS_CS": np.array([[570, 770], [120, 770]]),
        }
        self.__fig, self.__ax = plt.subplots(**kwargs)

    def get_route(self, current_location, destination) -> str:
        """
        This function gets the paths to your `destination` from your
        `current_location`. If either current location or destination does
        not exsist it'll raise a value error. Please use the following keys
        for various places: <br>
        Docking Area: `DA` <br>
        Warehouse: `WH` <br>
        Charging Station: `CS` <br>
        Delivery Station: `DS` <br>
        Example usage: <br>
        ```
        new_map = Map()
        route = new_map.get_route("CS", "DA")
        print(route)
        ```
        returns and numpy array of x and y coordinates
        """
        route = current_location + "_" + destination
        route = self.routes.get(route)
        if route is not None:
            return route
        else:
            raise ValueError(
                "Could not plan route, current location or destination doesn't exsist!"
            )

    def __plot_map(self, map_image: str):
        # plots the map in which the robot will be moving in
        opened_map = Image.open(map_image)
        opened_map = np.array(opened_map)

        self.__ax.imshow(opened_map)
        return self.__fig, self.__ax

    def show_animation(self, current_pos, destination, speed):
        """
        Shows the movement of the robots on the map
        """

        route = self.get_route(current_pos, destination)
        self.__plot_map("robot_map.png")
        self.__pos = route[0]
        self.__target = route
        self.__target_index = 1
        robot = self.__ax.scatter(*self.__pos, s=20)

        def update(frame):
            if self.__target_index >= len(self.__target):
                return (robot,)

            direction = self.__target[self.__target_index] - self.__pos

            # the movement
            if np.linalg.norm(direction) > 0.1:
                self.__pos = self.__pos + speed * direction / np.linalg.norm(direction)

            robot.set_offsets(self.__pos)

            if np.array_equal(
                self.__target[self.__target_index], self.__pos
            ):  # checks of the robot has reached the target
                print("next target")
                self.__target_index += 1  # next target

            return (robot,)

        # animation
        anim = fa(self.__fig, update, frames=500, interval=50)
        plt.show()

        return self.__fig, self.__ax


if __name__ == "__main__":
    map_ = Map(figsize=(12, 10))

    map_.show_animation("CS", "DA", 5)
