# turtle_cake.py
import turtle

def draw_rectangle(t, w, h):
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def draw_cake():
    wn = turtle.Screen()
    wn.title("Happy Birthday!")
    wn.setup(600, 500)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # cake base
    t.penup()
    t.goto(-180, -50)
    t.pendown()
    t.fillcolor("#f7c6c7")  # pink-ish
    t.begin_fill()
    draw_rectangle(t, 360, 140)
    t.end_fill()

    # icing layer
    t.penup()
    t.goto(-180, 40)
    t.pendown()
    t.fillcolor("#fff7a6")  # yellow-ish
    t.begin_fill()
    draw_rectangle(t, 360, 40)
    t.end_fill()

    # candles
    candle_x = -100
    for i in range(5):
        t.penup()
        t.goto(candle_x + i * 50, 80)
        t.pendown()
        t.fillcolor("#ffffff")
        t.begin_fill()
        draw_rectangle(t, 8, 40)
        t.end_fill()
        # flame
        t.penup()
        t.goto(candle_x + i * 50 + 4, 120)
        t.pendown()
        t.fillcolor("#ff9900")
        t.begin_fill()
        t.circle(6)
        t.end_fill()

    # message
    t.penup()
    t.goto(0, -120)
    t.color("black")
    t.write("Happy Birthday, my dear sister!", align="center", font=("Arial", 18, "bold"))

    wn.mainloop()

if __name__ == "__main__":
    draw_cake()
