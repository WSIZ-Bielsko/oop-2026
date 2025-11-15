from abc import ABC, abstractmethod


class Lockable(ABC):

    @abstractmethod
    def lock(self) -> bool:
        """
        lock the object; returns True if successful
        """

    @abstractmethod
    def unlock(self) -> bool:
        """
        unlock the object; returns True if successful
        """


class Persistent(ABC):

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass


class PasswordLocker(Lockable, Persistent):
    def __init__(self, password):
        self.password = password
        self.locked = False
        self.filename = "password.txt"

    def show_password(self) -> str:
        """ works if password is not locked"""
        if self.locked:
            raise Exception("locker is locked")
        return self.password

    def lock(self) -> bool:
        if self.locked:
            return False
        self.locked = True
        return True

    def unlock(self) -> bool:
        if not self.locked:
            return False
        self.locked = False
        return True

    def save(self):
        """ saves password to file"""
        with open(self.filename, "w") as f:
            f.write(self.password)

    def load(self):
        """ loads password from file"""
        with open(self.filename, "r") as f:
            self.password = f.read()


if __name__ == '__main__':
    locker = PasswordLocker("secret123")
    locker.lock()
    # locker.show_password()
    locker.unlock()
    print(locker.show_password())
    # locker.save()
    locker.load()
    print(locker.show_password())