class TicTacToe:

    def __init__(self, player_1, player_2):
        self.pos_valid = None
        self.board = []
        self.user1_pos = None
        self.user2_pos = None
        self.turns = 0
        self.user1_s = []
        self.user2_s = []
        self.winning_pos = [[11, 12, 13], [21, 22, 23], [31, 32, 33],
                            [11, 21, 31], [12, 22, 32], [13, 23, 33],
                            [11, 22, 33], [13, 22, 31]]
        self.player1_name = player_1
        self.player2_name = player_2

    def show_board(self):
        print(f"\n     1 | 2 | 3\n\n"
              f"1    {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}\n"
              f"  ----------------\n"
              f"2    {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}\n"
              f"  ----------------\n"
              f"3    {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}\n")

    def new_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append(" ")
            self.board.append(row)
        self.show_board()

    def continue_game(self):
        if self.turns < 9:
            if self.check_win():
                return False
            else:
                return True
        else:
            print("Game Over!\nIt's a draw!")
            return False

    def check_win(self):
        for row in self.winning_pos:
            if all(x in self.user1_s for x in row):
                print(f"Game Over\n{self.player1_name} wins")
                return True
            elif all(x in self.user2_s for x in row):
                print(f"Game Over\n{self.player2_name} wins")
                return True
        return False

    def validate(self, player_pos):
        if len(player_pos) != 2 or (3 < int(player_pos[0]) or int(player_pos[0]) < 1) or \
         (3 < int(player_pos[1]) or int(player_pos[1]) < 1) or \
         (self.board[int(player_pos[0]) - 1][int(player_pos[1]) - 1] == 'O') or \
         (self.board[int(player_pos[0]) - 1][int(player_pos[1]) - 1] == 'X'):
            print('Invalid Position!')
        else:
            self.pos_valid = False
            if player_pos == self.user1_pos:
                self.set_mark(user=self.user1_pos)
            else:
                self.set_mark(user=self.user2_pos)

    def play(self):
        self.new_board()
        while self.continue_game():
            self.pos_valid = True
            while self.pos_valid:
                self.user1_pos = input(f"{self.player1_name} enter a position on the grid: ")
                self.validate(self.user1_pos)
            # for player 2
            if self.continue_game():
                self.pos_valid = True
                while self.pos_valid:
                    self.user2_pos = input(f"{self.player2_name} enter a position on the grid: ")
                    self.validate(self.user2_pos)

    def set_mark(self, user):
        if user == self.user1_pos:
            self.board[int(self.user1_pos[0]) - 1][int(self.user1_pos[1]) - 1] = 'X'
            self.user1_s.append(int(f"{self.user1_pos[0]}{self.user1_pos[1]}"))
            self.show_board()
            self.turns += 1
        else:
            self.board[int(self.user2_pos[0]) - 1][int(self.user2_pos[1]) - 1] = 'O'
            self.user2_s.append(int(f"{self.user2_pos[0]}{self.user2_pos[1]}"))
            self.show_board()
            self.turns += 1


print("Welcome to TIC-TAC-TOE!\n"
      "You play by entering a 2 digit number representing the rows and column of the grid respectively\n")
player1 = input("Enter your name player 1, you will be 'X': ")
player2 = input("Enter your name player2, you will be 'Y': ")

game = TicTacToe(player_1=player1, player_2=player2)
game.play()
