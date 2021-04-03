from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from blocks import Blocks
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout!")
screen.tracer(0)

paddle = Paddle((0, -250))
scoreboard = ScoreBoard()
blocks = Blocks()
ball = Ball()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True
red_contact_first_time = False
orange_contact_first_time = False
red_contact = False
orange_contact = False
hits = 0
lives = 3

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect ball collision with ceiling
    if ball.ycor() > 280:
        ball.bounce_y()
        paddle.shrink()

    # detect ball collision with walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # detect paddle collision
    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_y()
        hits += 1

        if hits == 4 or hits == 12:
            ball.increase_speed()

    # detect paddle miss
    if ball.ycor() < -300:
        lives -= 1
        scoreboard.lost()
        ball.reset()
        hits = 0
        red_contact_first_time = False
        orange_contact_first_time = False

    # detect paddle collision with yellow blocks
    for block in blocks.list_of_yellow_blocks:
        if ball.distance(block) < 40:
            blocks.remove(blocks.list_of_yellow_blocks, block)
            ball.bounce_y()
            scoreboard.yellow_point()

    # detect paddle collision with green blocks
    for block in blocks.list_of_green_blocks:
        if ball.distance(block) < 40:
            blocks.remove(blocks.list_of_green_blocks, block)
            ball.bounce_y()
            scoreboard.green_point()

    # detect paddle collision with orange blocks
    for block in blocks.list_of_orange_blocks:
        if ball.distance(block) < 40:
            blocks.remove(blocks.list_of_orange_blocks, block)
            ball.bounce_y()
            scoreboard.orange_point()
            if not orange_contact_first_time:
                orange_contact_first_time = True
                orange_contact = True

    # detect paddle collision with red blocks
    for block in blocks.list_of_red_blocks:
        if ball.distance(block) < 40:
            blocks.remove(blocks.list_of_red_blocks, block)
            ball.bounce_y()
            scoreboard.red_point()
            if not red_contact_first_time:
                red_contact_first_time = True
                red_contact = True

    # increase speed if both orange and red blocks have been hit
    if red_contact and orange_contact:
        red_contact = False
        orange_contact = False
        ball.increase_speed()

    # out of lives
    if lives == 0:
        scoreboard.gameover()
        game_is_on = False

    # no blocks remaining
    if len(blocks.list_of_yellow_blocks) == 0 and len(blocks.list_of_green_blocks) == 0 \
            and len(blocks.list_of_orange_blocks) == 0 and len(blocks.list_of_red_blocks) == 0:
        scoreboard.win()
        game_is_on = False


screen.exitonclick()
