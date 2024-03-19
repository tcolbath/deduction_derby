from graphics import Window, Point, Line
from horse import Horse

class Game:
    def __init__(self, number_of_horses, num_spaces, window="None"):
        self._number_of_horses = number_of_horses
        self._num_spaces = num_spaces
        self._win = window
        self.draw_track()

    def new_game(self, horses):
        colors = list(horses.keys())
        racers = []

        # Creates the horses, draws them at start and starts a list for each horse
        for i in range(self._number_of_horses):
            horse = Horse(colors[i], horses[colors[i]])
            offset = Point(self.start.x, self.start.y - (25 * (self._number_of_horses - i)) + 15)
            horse.draw_horse(offset, self._win)
            racers.append(horse)
        
        
        # next hint = free

        # calculate all turns of game
            # for all horses move 1-6 spaces in order of leader ->
            # track horse order and location of each turn
            # if a horse crosses finish line, end game and snapshot order
        race_in_progress = True
        while race_in_progress:
            for racer in racers:
                num = racer.move()
                if racer._position > self._num_spaces:
                    race_in_progress = False
                racer._rolls.append(num)
        self.get_results(racers)

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

    def draw_move(self, horse):
        pass

    def get_results(self, racers):
        for racer in racers:
            print(f"{racer._color}\t {racer._rolls}\t {racer._position}")
        

    def rig_race(self, racers):
        for racer in racers:
            racer.move()

        
            