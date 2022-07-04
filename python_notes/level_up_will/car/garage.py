class Car():
    def __init__(self, make, model, top_speed, color, doors):
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.color = color
        self.doors = doors
        self.engine = "OFF"
        self.speed = 0

    def start_engine(self):
        self.engine = "ON"

    def accelerate(self):
        if self.engine == "ON":
            while self.speed < self.top_speed:
                self.speed += 1
        else:
            print("Turn the engine on, fool!")

    def deccelerate(self):
        print("Emergency Stop! Don't hit that Nun!")
        self.speed = 0


