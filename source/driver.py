
class Driver(object):
    """
    This is class which represents details of a driver.
    """

    def __init__(self):
        self.age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @classmethod
    def create(cls, age):
        driver_obj = cls()
        driver_obj.age = age
        if age < 18 or age > 100:
            return None
        return driver_obj
