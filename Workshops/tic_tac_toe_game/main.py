from tic_tac_toe_game import setup
from tic_tac_toe_game.play import play

if __name__ == '__main__':
    setup.setup()
    play()
    new_game = input(f"Do you want to play a new game? y/n: ")

    while new_game not in ('y', 'n'):
        input(f'Do you want to play a new game? Please enter "y" or "n": ')

    while new_game == 'y':
        setup.setup()
        play()
        new_game = input(f"Do you want to play a new game? y/n: ")


    for key, value in setup.game_counter.items():
        print(f"Player {key} won {value} game/s")

    print("Bye!")
