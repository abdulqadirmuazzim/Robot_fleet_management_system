import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation as fa
from matplotlib import patches 
from PIL import Image


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
    }

# Map
image_path  = "robot_map.png"

map_image = Image.open(image_path)


array = np.array(map_image)

# Initial and target positions
pos = routes["CS_DA"][0]
target = routes["CS_DA"]
target_index = 1
# map space


# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

map_ = ax.imshow(array)

# robot
robot = ax.scatter(pos[0], pos[1], s=10)


def update(frame):
    global pos, target_index

    if target_index >= len(target):
        return robot,

    direction =  target[target_index] - pos

    if np.linalg.norm(direction) > 0.1:
        pos = pos + 5 * direction / np.linalg.norm(direction)

    robot.set_offsets(pos)

    if (np.array_equal(target[target_index], pos)):
        print("Next")
        target_index = target_index + 1

    return robot,

ani = fa(fig, update, frames=500, interval=50)
plt.show()

# paths
