class Task:
    def __init__(
        self,
        ID,
        description: str,
        from_,
        to,
        priority: str = "low" or "normal" or "high",
    ):
        """`priority`: either `low` for low priority, `normal` for normal priority, or `high` for high priority"""

        self.id = ID
        self.description = description
        self.from_ = from_
        self.to = to
        self.__status = "Pending"
        priority_map = {"low": "green", "normal": "blue", "high": "red"}
        self.priority = priority_map.get(priority.lower(), "blue")

    def update_status(self, status):
        self.__status = status
        return self.__status
    
    def get_status(self):
        return self.__status
