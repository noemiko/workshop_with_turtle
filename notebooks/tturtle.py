from ipyturtle import Turtle as OldTurtle


class Turtle(OldTurtle):

    def reset(self):
        super().reset()
        self.pencolor("black")

    def goto(self, x, y):
        self._turtle_location_x = float(x)
        self._turtle_location_y = float(y)

turtle = Turtle()
