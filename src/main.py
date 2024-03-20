from graphics import Window
from game import Game, results_to_console
import random

def main():
    print("Loading game...")
    # Window Parameters (16:9)
    width = 1280
    height = 720
    win = None
    
    # Game Parameters
    number_of_horses = 6 # 1 - 6. Default = 6
    spaces = 20 # Tested with 20
    game_logs = True
    game = Game(number_of_horses, spaces, win, game_logs)
    
    # Name Your Horses! color : horse, in order of their rendering. 
    horses = {
        "red" : "Firestorm",
        "orange" : "Golden Gallop",
        "yellow" : "Thunderhoof",
        "green" : "Whispering Meadow",
        "blue" : "Stormy Symphony",
        "purple" : "Mystic Dreamer",
    }
    
    game.new_game(horses)
    game.real_time_race()

    results_to_console(game._results)
    
    if win is not None:
        win.wait_for_close()


main()
