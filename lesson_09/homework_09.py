class Romb:
    def __init__(self, side_a: float, angle_a: float):
        self.side_a = side_a
        self.side_b = None #можливо треба 0
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Сторона ромба повинна бути більше 0")
            object.__setattr__(self, name, value)
            object.__setattr__(self, "side_b", value) #додано щоб звертатись до side_b

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут має бути в межах (0, 180)")
            object.__setattr__(self, name, value)
            object.__setattr__(self, "angle_b", 180 - value)

        elif name == "angle_b":
            raise AttributeError("Кут B обчислюється автоматично")

        else:
            object.__setattr__(self, name, value)



#romb_1 = Romb(side_a=1, angle_a=180)
#romb_2 = Romb(side_a=-3, angle_a=60)
romb_3 = Romb(side_a=0.5, angle_a=60)
#print(romb_3.side_b)

import unittest


class TestRomb(unittest.TestCase):

    def test_valid_romb(self):
        r = Romb(5, 60)
        self.assertEqual(r.side_a, 5)
        self.assertEqual(r.side_b, 5)
        self.assertEqual(r.angle_a, 60)
        self.assertEqual(r.angle_b, 120)

    def test_invalid_side(self):
        with self.assertRaises(ValueError):
            Romb(0, 60)

    def test_invalid_angle(self):
        with self.assertRaises(ValueError):
            Romb(5, 180)

    def test_angle_b_is_read_only(self):
        r = Romb(5, 60)
        with self.assertRaises(AttributeError):
            r.angle_b = 100


if __name__ == "__main__":
    unittest.main()