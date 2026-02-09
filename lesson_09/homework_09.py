class Romb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.side_b = None
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Сторона ромба повинна бути більше 0")
            object.__setattr__(self, name, value)
            object.__setattr__(self, "side_b", value)

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут має бути в межах (0, 180)")
            object.__setattr__(self, name, value)
            # автоматично обчислюємо суміжний кут
            object.__setattr__(self, "angle_b", 180 - value)

        elif name == "angle_b":
            raise AttributeError("Кут B обчислюється автоматично")

        else:
            object.__setattr__(self, name, value)



#romb_1 = Romb(side_a=1, angle_a=180)
#romb_2 = Romb(side_a=-3, angle_a=60)
romb_3 = Romb(side_a=0.5, angle_a=60)
print(romb_3.side_b)