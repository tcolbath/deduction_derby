from graphics import Window, Point, Line

class Game:
    def __init__(self, number_of_horses, num_spaces, window="None"):
        self.__number_of_horses = number_of_horses
        self.__num_spaces = num_spaces
        self.__win = window
        self.draw_track()

    def new_game(self):
        # place all horses on start

        # next hint = free

        # calculate all turns of game
            # for all horses move 1-6 spaces in order of leader ->
            # track horse order and location of each turn
            # if a horse crosses finish line, end game and snapshot order
        
        pass

    def draw_track(self):
        # draw a line for the track
        if self.__win == None:
            return
        side_margin = 100
        top_margin = 200
        start = Point(side_margin, top_margin)
        end = Point(self.__win.width - side_margin, top_margin)
        track = Line(start, end)
        self.__win.draw_line(track, "black", 5)

        # draw a tick marks for each of the spaces
        length_of_track = track.p2.x - track.p1.x
        spaces_x = int(length_of_track / (self.__num_spaces + 2))

        for i in range(0, self.__num_spaces + 3):
            space_tick_y1 = Point(start.x + (i * spaces_x) + 1, start.y - 2)
            space_tick_y2 = Point(start.x + (i * spaces_x) + 1, start.y + 10)
            space_tick = Line(space_tick_y1, space_tick_y2)
            if i == 1:
                self.__win.draw_line(space_tick, "green", 4)
            elif i == self.__num_spaces + 1:
                self.__win.draw_line(space_tick, "red", 4)
            else: 
                self.__win.draw_line(space_tick)

