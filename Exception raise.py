class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_accident(self):
        print("Accident occur", self.msg)


try:
    raise Accident("crash between 2 cars")
except Accident as e:
    e.print_accident()
