from graphics import Window, Point, Line

class Game:
    def __init__(self, number_of_horses, num_spaces, window="None"):
        self.__number_of_horses = number_of_horses
        self.__num_spaces = num_spaces
        self.__win = window
        self.draw_track(num_spaces)

    def new_game(self):
        # place all horses on start

        # next hint = free

        # calculate all turns of game
            # for all horses move 1-6 spaces in order of leader ->
            # track horse order and location of each turn
            # if a horse crosses finish line, end game and snapshot order
        
        pass

    def draw_track(self, num_spaces, spaces_x=50):
        # draw a line for the track with ticks at space
        if self.__win == None:
            return
        side_margin = 100
        top_margin = 200
        start = Point(side_margin, top_margin)
        end = Point(self.__win.width - side_margin, top_margin)
        track = Line(start, end)
        self.__win.draw_line(track, "black", 5)
