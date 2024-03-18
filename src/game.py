from graphics import Window, Point, Line
from horse import Horse

class Game:
    def __init__(self, number_of_horses, num_spaces, window="None"):
        self._number_of_horses = number_of_horses
        self._num_spaces = num_spaces
        self._win = window
        self.draw_track()

    def new_game(self):
        horses = [Horse(color="blue"), Horse(color="red")]
        for i in range(self._number_of_horses):
            offset = Point(self.start.x, self.start.y - 3 - (20* i))
            horses[i].draw_horse(offset, self._win)
            print(horses[i]._color)

        # next hint = free

        # calculate all turns of game
            # for all horses move 1-6 spaces in order of leader ->
            # track horse order and location of each turn
            # if a horse crosses finish line, end game and snapshot order
        
        pass

    def draw_track(self):
        # draw a line for the track
        if self._win == None:
            return
        side_margin = 100
        top_margin = 200
        self.start = Point(side_margin, top_margin)
        self.end = Point(self._win.width - side_margin, top_margin)
        track = Line(self.start, self.end)
        self._win.draw_line(track, "black", 5)

        # draw a tick marks for each of the spaces
        length_of_track = track.p2.x - track.p1.x
        spaces_x = int(length_of_track / (self._num_spaces + 2))

        for i in range(0, self._num_spaces + 3):
            space_tick_y1 = Point(self.start.x + (i * spaces_x) + 1, self.start.y - 2)
            space_tick_y2 = Point(self.start.x + (i * spaces_x) + 1, self.start.y + 10)
            space_tick = Line(space_tick_y1, space_tick_y2)
            if i == 1:
                self._win.draw_line(space_tick, "green", 4)
            elif i == self._num_spaces + 1:
                self._win.draw_line(space_tick, "red", 4)
            else: 
                self._win.draw_line(space_tick)

