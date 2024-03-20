from graphics import Window, Point, Line
from horse import Horse
from player import bid_log, clear_bid_log

class Game:
    def __init__(self, number_of_horses, num_spaces, window="None", game_logs="False"):
        self._number_of_horses = number_of_horses
        self._num_spaces = num_spaces
        self._win = window
        self.draw_track()
        self.game_logs = game_logs
        
    def new_game(self, horses):
        if self.game_logs == True:
            clear_race_log()
            clear_bid_log()
        self._num_turns = 0
        colors = list(horses.keys())
        racers = []

        # Creates the horses, draws them at start and starts a list for each horse
        for i in range(self._number_of_horses):
            horse = Horse(colors[i], horses[colors[i]])
            if self._win is not None:
                offset = Point(self.start.x, self.start.y - (25 * (self._number_of_horses - i)) + 15)
                horse.draw_horse(offset, self._win)
            racers.append(horse)
          
        # next hint = free

        # calculate all turns of game
        results = self.rig_race(racers)
        results_to_console(results)

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
     

    def rig_race(self, racers):
        # for all horses move 1-6 spaces in order of leader ->
        # track horse order and location of each turn
        crossed_the_line = []
        self.rig_race_r(racers, crossed_the_line)
        return crossed_the_line


    def rig_race_r(self, racers, crossed_the_line):
        self._num_turns += 1
        racers_to_remove = []
        for racer in racers:
            if range(len(racers)) == 0:
                return
            num = racer.move()
            if racer.position > self._num_spaces:
                racer.position = self._num_spaces + 1
                crossed_the_line.append(racer)
                racers_to_remove.append(racer)
            racer._rolls.append(num)
            racer._positions.append(racer.position)
        racers = list(filter(lambda racer: racer not in racers_to_remove, racers))
        if self.game_logs == True:
            race_log(self._num_turns, racers, crossed_the_line)
        # play another turn if active racers left
        if len(racers) > 0:
            racers = self.get_roll_order(racers)
            self.rig_race_r(racers, crossed_the_line)


    def get_roll_order(self, racers):
        leader = 0
        leader_last_roll = 0
        leader_index = 0

        for i in range(len(racers)):
            racer = racers[i] 
            if racer.position > leader:
                leader = racer.position
                leader_last_roll = racer._last_roll
                leader_index = i
            if racer.position == leader:
                if racer._last_roll > leader_last_roll:
                    leader_last_roll = racer._last_roll
                    leader_index = i

        roll_order = []
        roll_order.extend(racers[leader_index:])
        roll_order.extend(racers[0:leader_index])
        return roll_order
    

def race_log(turn, racers, crossed_the_line):
    with open("./data/race_log.txt", "a") as race_log:
        race_log.write(f"\nTurn {turn}:\n")
        for racer in racers:
            if racer._last_roll == 0:
                race_log.write(f"{racer._color} stumbled! Still at {racer.position}\n")
            else:
                race_log.write(f"{racer._color} rolled a {racer._last_roll}.  Now at {racer.position}\n")
        if len(crossed_the_line) > 0:
            place = 1
            for racer in crossed_the_line:
                race_log.write(f"{place}. {racer._color}, ") 
                place += 1
            race_log.write("have crossed the finish line!\n")

def clear_race_log():
    with open("./data/race_log.txt", "w") as race_log:
        race_log.write("Deduction Derby -- Race Log\n")


def results_to_console(results):
    for racer in results:
        print(f"{racer._color}\t {racer._rolls}\t\t {racer._positions}")


