from abc import ABC, abstractmethod


class Alert(ABC):
    """This is an abstract base class that defines the alerting mechanism for the fleet management system.
    It has and abstract method `alert_user` that must be implemented by any subclass."""

    @abstractmethod
    def alert_user(self, message):
        """
        takes in the `message` to be alerted to the user
        """
        print(message)
