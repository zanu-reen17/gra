import turtle
import random
import time

window = turtle.Screen()

BOK = 600
X = -300
Y = 300

window.setup(BOK,BOK)
window.title('Kółko i krzyżyk')
window.bgcolor('black')

xo = turtle.Turtle()
xo.color('white')
xo.speed(0)
xo.pensize(7)
xo.hideturtle()

tablica = [[None,None,None],
            [None,None,None],
            [None,None,None]]

kolej = random.choice(['x','o'])

ODSTĘP = int(BOK / 3)

for a in [1,2]:
    xo.penup()
    xo.goto(X + a*ODSTĘP, Y)
    xo.pendown()
    xo.goto(X + a*ODSTĘP, -Y)

    xo.penup()
    xo.goto(X, Y -a*ODSTĘP)
    xo.pendown()
    xo.goto(-X, Y -a*ODSTĘP)

def sprawdz():

    if tablica[0][0] == tablica[1][1] == tablica[2][2]: return tablica[2][2]
    if tablica[0][2] == tablica[1][1] == tablica[2][0]: return tablica[2][0]

    for w in range(3):
        if tablica[w][0] == tablica[w][1] == tablica[w][2]: return tablica[w][0]

    for k in range(2):
        if tablica[0][k] == tablica[1][k] == tablica[2][k]: return tablica[0][k]

    return None

def click(x,y):

    global kolej

    kolumna = 0
    wiersz = 0

    if x < X + ODSTĘP: kolumna = 0
    elif x > X + 2*ODSTĘP: kolumna = 2
    else: kolumna = 1

    if y < Y - 2*ODSTĘP: wiersz = 2
    elif y > Y - ODSTĘP: wiersz =0
    else: wiersz = 1


    if tablica[wiersz][kolumna] != None: return


    kolumna_środek = (kolumna*ODSTĘP + ODSTĘP/2) - BOK/2
    wiersz_środek = (-wiersz*ODSTĘP - ODSTĘP/2) + BOK/2

    xo.penup()
    xo.goto(kolumna_środek-25, wiersz_środek-25)
    if kolej == 'x': xo.write('X', font=('Arial',50))
    else: xo.write('O', font=('Arial',50))


    tablica[wiersz][kolumna] = kolej

    if kolej == 'o': kolej = 'x'
    else: kolej = 'o'


    if sprawdz() != None:
        xo.penup()
        xo.goto(-150,0)
        time.sleep(1)
        xo.clear()
        xo.write(" Wygrały " + sprawdz(), font=("Arial",50))

window.onclick(click)

window.listen()
window.mainloop()