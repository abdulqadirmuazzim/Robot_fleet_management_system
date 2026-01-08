from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation as fa
from PIL import Image
import numpy as np


routes = {
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
    "CS_DS": np.array([[120, 665], [475, 665], [475, 460], [600, 460], [600, 730]]),
}


def get_route(current_location, destination) -> np.ndarray:
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
    route = routes.get(route)
    if route is not None:
        return route
    else:
        raise ValueError(
            "Could not plan route, current location or destination doesn't exsist!"
        )


class Map:
    def __init__(self, **kwargs):
        self.__fig, self.__ax = plt.subplots(**kwargs)

    def __plot_map(self, map_image: str):
        # plots the map in which the robot will be moving in
        opened_map = Image.open(map_image)
        opened_map = np.array(opened_map)

        self.__ax.imshow(opened_map)
        return self.__fig, self.__ax

    def animate(self, robots: list):
        # plot out the map
        self.__plot_map("robot_map.png")
        # plot robots
        scatters = [
            self.__ax.scatter(r.route[0, 0], r.route[0, 1], s=20, c=r.task.priority)
            for r in robots
        ]

        def update(frame):
            artists = []

            for i, robot in enumerate(robots):
                if robot.path_index >= len(robot.route):
                    continue
                # target
                target = robot.route[robot.path_index]

                # current position
                direction = target - robot.pos
                dist = np.linalg.norm(direction)

                if dist > robot.speed:
                    robot.pos += robot.speed * direction / dist
                else:
                    robot.path_index += 1

                scatters[i].set_offsets(robot.pos)

                artists.append(scatters[i])

            return artists

        anim = fa(self.__fig, update, frames=600, interval=50)

        return anim
