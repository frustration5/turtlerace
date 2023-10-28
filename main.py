import turtle
from random import randint


scrn = turtle.Screen()
scrn.setup(width=700, height=400)
# names = ["Turtle_1", "Turtle_2", "Turtle_3", "Turtle_4", "Turtle_5", "Turtle_6"]
racer_c = {"red": None, "blue": None, "green": None, "pink": None, "yellow": None, "orange": None}
names_i = []
winner = ""
u_bet = ""


def get_input():  # Run initially to set names and amount of racers
    """Lets you define names for the amount of turtle racers you chose"""
    global names_i
    global names
    how_many = scrn.textinput(title="Racer Amount", prompt="How many turtles will race? (2-6): ")
    names_i = [*range(0, int(how_many))]
    if len(names_i) > 6:  # Creates the range of ints for name index and if it's greater than 6, then 6
        names_i = [*range(0, 6)]
        scrn.textinput(title="Max Racers", prompt="Max is 6.")
    if len(names_i) < 2:  # Creates the range of ints for name index and if it's greater less than 2, then 2
        names_i = [*range(0, 2)]
        scrn.textinput(title="Dumb?", prompt="There's no point in racing less than 2 racers, are you dumb?")
    create_turtles()
    start_race()



def create_turtles():
    """Creates turtles depending on the names_i length. Must be run after get_names function."""
    global names_i
    global racer_c
    if len(names_i) == 1:
        turtle_1 = turtle.Turtle()
        racer_c["red"] = turtle_1
    elif len(names_i) == 2:
        turtle_1 = turtle.Turtle()
        racer_c["red"] = turtle_1
        turtle_2 = turtle.Turtle()
        racer_c["blue"] = turtle_2
    elif len(names_i) == 3:
        turtle_1 = turtle.Turtle()
        racer_c["red"] = turtle_1
        turtle_2 = turtle.Turtle()
        racer_c["blue"] = turtle_2
        turtle_3 = turtle.Turtle()
        racer_c["green"] = turtle_3
    elif len(names_i) == 4:
        turtle_1 = turtle.Turtle()
        racer_c["red"] = turtle_1
        turtle_2 = turtle.Turtle()
        racer_c["blue"] = turtle_2
        turtle_3 = turtle.Turtle()
        racer_c["green"] = turtle_3
        turtle_4 = turtle.Turtle()
        racer_c["violet"] = turtle_4
    elif len(names_i) == 5:
        turtle_1 = turtle.Turtle()
        racer_c["red"] = turtle_1
        turtle_2 = turtle.Turtle()
        racer_c["blue"] = turtle_2
        turtle_3 = turtle.Turtle()
        racer_c["green"] = turtle_3
        turtle_4 = turtle.Turtle()
        racer_c["pink"] = turtle_4
        turtle_5 = turtle.Turtle()
        racer_c["yellow"] = turtle_5
    elif len(names_i) == 6:
        turtle_1 = turtle.Turtle()
        racer_c["red"] = turtle_1
        turtle_2 = turtle.Turtle()
        racer_c["blue"] = turtle_2
        turtle_3 = turtle.Turtle()
        racer_c["green"] = turtle_3
        turtle_4 = turtle.Turtle()
        racer_c["pink"] = turtle_4
        turtle_5 = turtle.Turtle()
        racer_c["yellow"] = turtle_5
        turtle_6 = turtle.Turtle()
        racer_c["orange"] = turtle_6


def start_race():
    global racer_c
    global winner
    global u_bet
    offset = 0
    first_turtle_pos = {"x": -340, "y": 140}
    turt = list(racer_c.keys())
    for t in names_i:
        racer_c[turt[t]].color(turt[t])
        racer_c[turt[t]].penup()
        racer_c[turt[t]].goto(first_turtle_pos["x"], first_turtle_pos["y"] + offset)
        offset -= 50
    u_bet = scrn.textinput(title="Make your bet", prompt="Which turtle will win, enter a color: ")

    while True:
        xpos = ()
        for t in names_i:
            mv = randint(5, 15)
            racer_c[turt[t]].forward(mv)
            xpos = racer_c[turt[t]].pos()  # The x coordinate of the current turtle of the for loop
            if xpos[0] >= 330:  # Check if the x coord is at or past the finish line (x = 300) and break loop if so
                break
        if xpos[0] >= 330:
            for i in names_i:
                xpos = racer_c[turt[i]].pos()
                if xpos[0] >= 330:
                    winner = turt[i]
                    print(f"The winner is {winner}!")
                    if winner == u_bet.lower():
                        print("You Win!")
                    else:
                        print("You lose!")
            break


get_input()


scrn.exitonclick()