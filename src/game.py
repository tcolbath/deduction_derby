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
        self.rig_race(racers)


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
            print(f"{racer._color}\t {racer._rolls}")
        
    def rig_race(self, racers):
        # for all horses move 1-6 spaces in order of leader ->
        # track horse order and location of each turn

        crossed_the_line = []
        self.rig_race_r(racers, crossed_the_line)
        self.get_results(crossed_the_line)

    def rig_race_r(self, racers, crossed_the_line):
        for racer in racers:
            if range(len(racers)) == 0:
                return
            num = racer.move()
            racer._rolls.append(num)
            if racer._position > self._num_spaces:
                racer._position = self._num_spaces + 1
                crossed_the_line.append(racer)
                racers.remove(racer)
        if len(racers) > 0:
            self.get_roll_order(racers)
            self.rig_race_r(racers, crossed_the_line)

    def get_roll_order(self, racers):
        leader = 0
        leader_last_roll = 0
        leader_index = 0

        for i in range(len(racers)):
            racer = racers[i] 
            if racer._position > leader:
                leader = racer._position
                leader_last_roll = racer._last_roll
                leader_index = i
            if racer._position == leader:
                if racer._last_roll > leader_last_roll:
                    leader_last_roll = racer._last_roll
                    leader_index = i

        roll_order = []
        roll_order.extend(racers[leader_index:])
        roll_order.extend(racers[0:leader_index])
        return roll_order