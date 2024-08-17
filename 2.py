import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.begin_fill()
        for _ in range(4):
            t.forward(length)
            t.left(180)
        t.end_fill()
    else:
        t.forward(length)
        t.left(45)
        draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
        
        t.right(90)
        draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
        t.left(45)
        t.backward(length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    level = int(input("Введіть рівень рекурсії: "))

    t = turtle.Turtle()
    t.color("green")
    t.speed("fastest")
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    draw_pythagoras_tree(t, 100, level)

    turtle.done()

if __name__ == "__main__":
    main()
