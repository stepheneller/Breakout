from turtle import Turtle


class Blocks():

    def __init__(self):
        self.list_of_red_blocks = []
        self.list_of_orange_blocks = []
        self.list_of_green_blocks = []
        self.list_of_yellow_blocks = []
        self.BLOCK_START_X = -320
        self.BLOCK_START_Y = 250
        self.generator()

    def blocks(self, color, list_name):
        new_block = Turtle("square")
        new_block.penup()
        new_block.color(color)
        new_block.shapesize(stretch_wid=1, stretch_len=3)
        new_block.goto(self.BLOCK_START_X, self.BLOCK_START_Y)
        self.BLOCK_START_X += 70
        list_name.append(new_block)

    def remove(self, list_name, block):
        block.color('black')
        list_name.remove(block)

    def generator(self):
        for num in range(0, 10):
            self.blocks('dark red', self.list_of_red_blocks)

        self.BLOCK_START_X = -320
        self.BLOCK_START_Y = 220
        for num in range(0, 10):
            self.blocks('dark red', self.list_of_red_blocks)

        self.BLOCK_START_X = -320
        self.BLOCK_START_Y = 190
        for num in range(0, 10):
            self.blocks('dark orange', self.list_of_orange_blocks)

        self.BLOCK_START_X = -320
        self.BLOCK_START_Y = 160
        for num in range(0, 10):
            self.blocks('dark orange', self.list_of_orange_blocks)

        self.BLOCK_START_X = -320
        self.BLOCK_START_Y = 130
        for num in range(0, 10):
            self.blocks('dark green', self.list_of_green_blocks)

        self.BLOCK_START_X = -320
        self.BLOCK_START_Y = 100
        for num in range(0, 10):
            self.blocks('dark green', self.list_of_green_blocks)

        self.BLOCK_START_X = -320
        self.BLOCK_START_Y = 70
        for num in range(0, 10):
            self.blocks('gold', self.list_of_yellow_blocks)

        self.BLOCK_START_X = -320
        self.BLOCK_START_Y = 40
        for num in range(0, 10):
            self.blocks('gold', self.list_of_yellow_blocks)

