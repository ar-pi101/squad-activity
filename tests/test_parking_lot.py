import unittest
import env
from source import parking


class TestParkingLot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parking = parking.Parking()
        cls.allocated_slot = 1

    def test_a_create_parking_lot(self):
        parking_slots = 6
        self.parking.Create_parking_lot(parking_slots)
        self.assertEqual(len(self.parking.slots), parking_slots,
                         msg="Wrong parking lot created")

    def test_b_park(self):
        reg_no = "MH-12-FF-2017"
        age = 21
        command = "driver_age"
        self.parking.Park(reg_no, command, age)
        self.assertFalse(
            self.parking.slots[self.allocated_slot].available, "Park failed.")
        for i in self.parking.slots.values():
            if not i.available and i.car and i.driver:
                self.assertEqual(i.car.reg_no, reg_no, "Park failed")
                self.assertEqual(i.driver.age, age, "Park failed")

    def test_c_leave(self):
        self.parking.Leave(self.allocated_slot)
        self.assertTrue(
            self.parking.slots[self.allocated_slot].available, "Leave failed.")

    @classmethod
    def tearDownClass(cls):
        del cls.parking


if __name__ == '__main__':
    unittest.main()
