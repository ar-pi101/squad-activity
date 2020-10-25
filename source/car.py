from re import compile


class Car(object):
    """
    This is class which represents details of a car.
    """

    def __init__(self):
        self._reg_no = None

    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value

    @classmethod
    def create(cls, reg_no):
        car_obj = cls()
        car_obj.reg_no = reg_no
        reg_format = compile(
            '^[A-Z]{2}[-][0-9]{1,2}(?:[-][A-Z])?(?:[-][A-Z]*)?[-][0-9]{4}$')
        if not reg_format.match(reg_no):
            return None
        return car_obj
