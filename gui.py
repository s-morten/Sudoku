from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

game = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

class SudokuGUI(Frame):
    def __init__(self, parent, game):
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)

        self.row, self.col = 0, 0

        self.__initUI()

    def __initUI(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=WIDTH,
                             height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self,
                              text="Clear answers",
                              command=self.__clear_answers)
        clear_button.pack(fill=BOTH, side=BOTTOM)
        new_soduko_button = Button(self,
                              text="New Sudoku",
                              command=self.__get_new_sudoku)
        new_soduko_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle()

        #self.canvas.bind("<Button-1>", self.__cell_clicked)
        #self.canvas.bind("<Key>", self.__key_pressed)

    def __draw_grid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __draw_puzzle(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game[i][j]
                if answer != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    #original = self.game.start_puzzle[i][j]
                    #color = "black" if answer == original else "sea green"
                    self.canvas.create_text(
                        #x, y, text=answer, tags="numbers", fill=color
                        x, y, text=answer, tags="numbers", fill="black"
                    )

    def __clear_answers(self):
        for i in range(9):
            for j in range(9):
                self.game[i][j] = 0
        self.__draw_puzzle()

    def __get_new_sudoku:
        sudoku.get_new_sudoku

root = Tk()
SudokuGUI(root, game)
root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
root.mainloop()
