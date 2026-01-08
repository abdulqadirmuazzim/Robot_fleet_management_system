class Task:
    def __init__(
        self,
        ID,
        description: str,
        from_,
        to,
        priority: str = "green" or "blue" or "red",
    ):
        """`priority`: either `green` for low , `blue` for normal or `red`, high"""

        self.id = ID
        self.description = description
        self.from_ = from_
        self.to = to
        self.status = "Pending"
        self.priority = priority

    def update_status(self, status):
        return self.status
