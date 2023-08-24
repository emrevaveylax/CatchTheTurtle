import turtle
import random

#SCREEN
screen = turtle.Screen()
screen.title("Catch The Turtle")
screen.bgcolor("Pink")
screen.setup(width=600, height=600)

#SKOR
score = 0

#KAPLUMBAĞ
player_turtle = turtle.Turtle()
player_turtle.shape("turtle")
player_turtle.color("blue")
player_turtle.shapesize(2, 2)
player_turtle.penup()

#SKOR Yazısı
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.color("black")
score_turtle.penup()
score_turtle.goto(0, 240)
score_turtle.write("Skor: 0", align="center", font=("Arial", 24, "normal"))


#GERİ SAYIM
countdown_turtle = turtle.Turtle()
countdown_turtle.hideturtle()
countdown_turtle.color("black")
countdown_turtle.penup()
countdown_turtle.goto(0, 200)

click_allowed = True

#Skoru Yükseltme
def increase_score(x, y):
    global score, click_allowed
    if click_allowed:
        score +=1
        score_turtle.clear()
        score_turtle.write(f"Skor: {score}", align="center", font=("Arial", 24, "normal"))
        click_allowed = False
        screen.ontimer(reset_click, 1000)

#Tıklamayı Sıfırlama
def reset_click():
    global click_allowed
    click_allowed = True

#Skor Yükseltme
player_turtle.onclick(increase_score)

#Işınlanma
def teleport_turtle():
    player_turtle.hideturtle()
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    player_turtle.goto(x, y)
    player_turtle.showturtle()
    screen.ontimer(teleport_turtle, 500)

#Geri Sayım
def countdown__timer(count, stop_game=None):
    countdown_turtle.clear()
    if count > 0:
        countdown_turtle.write(f"Kalan Süre: {count} saniye", align="center", font=("Arial", 24, "normal"))
        screen.ontimer(lambda: countdown__timer(count - 1), 1000)
    else:
        countdown_turtle.clear()
        countdown_turtle.write("Süre Doldu!", align="center", font=("Arial", 24, "normal"))
        screen.ontimer(stop_game, 2000)  # Oyunu 2 saniye sonra kapat


    def stop_game():
        turtle.done()

countdown__timer(20)

teleport_turtle()

turtle.mainloop()
