class Task:
    def __init__(
        self,
        ID,
        description: str,
        from_,
        to,
        priority: str = "low" or "normal" or "high",
    ):
        """`priority`: either `low`, `normal` or `high`"""

        self.id = ID
        self.description = description
        self.from_ = from_
        self.to = to
        self.status = "Pending"
        self.priority = priority


tasks = [
    (
        1,
        "Get freshly shipped goods from Docking are to warehouse",
        "DA",
        "WH",
        "normal",
    ),
    (2, "Take the goods from warehouse to the delivery station", "WH", "DS", "low"),
]

task1 = Task(*tasks[0])
task2 = Task(*tasks[1])
