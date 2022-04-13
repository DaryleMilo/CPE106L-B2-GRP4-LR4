import os, random
import oxo_data

class game():
    def __init__(game):
        game.board = list (" " * 9)

    def save(game, player):
        oxo_data.saveGame(game.board)

    def restore(game):
        try:
            game.board = oxo_data.restoreGame()
            if len(game.board) != 9:
                game.board = list (" " * 9)
            return game.board
        except IOError:
            game.board = list(" " * 9)
            return game.board

    def _generateMove(game):
        options = [i for i in range(len(game.board)) if game.board[i] == " "]
        if options:
            return random.choice(options)
        else: return -1

    def _isWinningMove(game):
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))
        game = game.board
        for a,b,c in wins:
            chars = game[a] + game[b] + game[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False
    
    def userMove(game,cell):
        if game.board[cell] != ' ':
            raise ValueError('Invalid Cell')
        else:
            game.board[cell] = 'X'
        if game._isWinningMove():
            return 'X'
        else:
            return ""

    def computerMove(game):
        cell = game._generateMove()
        if cell == -1:
            return 'D'
        game.board[cell] = 'O'
        if game._isWinningMove():
            return 'O'
        else:
            return ""

def test():
    result = ""
    game = game()
    while not result:
        print(game.board)
        try:
            result = game.userMove( game._generateMove())
        except ValueError:
                print("Oops, that shouldn't happen")
        if not result:
                result = game.computerMove()

        if not result: continue
        elif result == 'D':
            print("Its a draw")
        else:
            print("Winner is:", result)
        print(game.board)

if __name__ == "__main__":
    test()