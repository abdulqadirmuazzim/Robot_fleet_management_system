# Bismillah
from Task import Task
from Maps import Map
from Robot import Robot
from matplotlib import pyplot as plt
from Alert import Alert


class FleetAdmiral(Alert):
    """
    This is the Main class of the project it's responsibility is to
    coordinate the robots, assign tasks to them, give them positions to
    move to and monitor their status and the status of their task
    """

    def __init__(self):
        self.__tasks = []
        self.__robots = []
        self.current_map = Map(figsize=(16, 12))

    def accept_tasks(self, task: list | tuple):
        """
        This method accepts a task which is in tuple form contining `ID`, `description` and `location`
        respectively, you can also pass a list of tasks. Example usage:<br>
        ```
        commander = FleetAdmiral()
        commander.assign_tasks((1, "Get freshly shipped goods from Docking are to warehouse", "DA"))
        ```python
        or<br>
        ```
        tasks = [
            (1, "Get freshly shipped goods from Docking are to warehouse", "DA"),
            (2, "Take the goods to the delivery station", "DS")
            ]
        commander.assign_tasks(tasks)
        ```python
        """
        if isinstance(task[0], list) or isinstance(task[0], tuple):
            for t in task:
                new_task = Task(*t)
                self.__tasks.append(new_task)
                # alert user
                self.alert_user(
                    f"New task assigned:\nID: {new_task.id}, Description: {new_task.description}, location: {new_task.from_} to {new_task.to}"
                )
        elif type(task) == tuple:
            new_task = Task(*task)
            self.__tasks.append(new_task)
            self.alert_user(
                f"-------New task assigned-------:\nID: {new_task.id}, Description: {new_task.description}, location: {new_task.from_} to {new_task.to}"
            )

    def assign_tasks(self, save_animation=False):
        """
        This method is to be used after the `accept_tasks` method, it assigns each task to a robot
        and alerts the user which robot has taken which task, it also starts the animation of the
        robots on the map. Example usage:<br>
        ```python
        commander = FleetAdmiral()
        commander.accept_tasks((1, "Get freshly shipped goods from Docking are to warehouse", "DA"))
        anim = commander.assign_tasks()
        plt.show()
        ```
        """
        # one robot for each task
        for robot_index, task in enumerate(self.__tasks, start=1):
            speed_map = {"green": 2, "blue": 3.5, "red": 5}
            speed = speed_map.get(task.priority.lower(), 3.5)

            robot = Robot(
                robot_index,
                f"Robot{robot_index}",
                task,
                routes=[task.from_, task.to],
                speed=speed,
            )
            # alert user which robot had taken a specific task
            self.alert_user(
                f"Task id: {task.id}, description: {task.description}. assigned to {robot.name}\n\n"
            )
            task.status = "In progress"
            # add robot to fleet
            self.__robots.append(robot)
            # check task priority
        anim = self.current_map.animate(self.__robots)
        if save_animation:
            anim.save("fleet_animation.mp4", writer="ffmpeg", fps=30)
        plt.show()
        # alert user all tasks are completed
        self.alert_user("All tasks are completed!")

    def alert_user(self, message):
        return super().alert_user(message)

    def task_status(self, id_):
        for task in self.__tasks:
            if task.id == id_:
                return task.status
        return "Task not found"


commander = FleetAdmiral()

# Example


print("---- Enter the tasks or list of tasks you want completed ----")
print("--- To quit submit empty input on the 'description' input --- ")
print(
    "--- Task locations are coded as ---: DA = Docking Area,\n WH = Warehouse,\n DS = Delivery Station,\n CS = Charging Station,\n DA = Docking Area"
)


# Example tasks
tasks = [
    (
        1,
        "Get freshly shipped goods from Docking are to warehouse",
        "DA",
        "WH",
        "normal",
    ),
    (
        2,
        "delivery of goods from warehouse to delivery station",
        "WH",
        "DS",
        "low",
    ),
    (
        3,
        "Move goods from docking area directly to delivery station",
        "DA",
        "DS",
        "high",
    ),
    (
        4,
        "return stuff from delivery to warehouse",
        "DS",
        "WH",
        "normal",
    ),
    (
        5,
        "return some goods from delivery station to docking area",
        "DS",
        "DA",
        "low",
    ),
    (
        6,
        "Urgent delivery of goods from Warehouse to delivery station",
        "WH",
        "DS",
        "high",
    ),
    (
        7,
        "return goods quickly to docking area from warehouse",
        "WH",
        "DA",
        "high",
    ),
    (
        8,
        "Move goods from docking area directly to delivery station",
        "DA",
        "DS",
        "low",
    ),
]

# fleet manager accecpts tasks from user
commander.accept_tasks(tasks)

# fleet manager assigns tasks to robots to execute
commander.assign_tasks()


# user input for tasks
# tasks = []
# id_ = 0
# while True:
#     description = input("Enter task description: ")

#     if not description:
#         break

#     from_ = input("Enter task starting location code: ")
#     to = input("Enter task destination location code: ")
#     priority = input("Task priority: ")

#     task = (id_, description, from_, to, priority)
#     tasks.append(task)
#     id_ += 1
