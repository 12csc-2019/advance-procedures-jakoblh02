import tkinter as tk
import random
import vlc
import time

# Constants
WIDTH = 1000
HEIGHT = 500
CEN_X = WIDTH / 2
CEN_Y = HEIGHT / 2
# https://www.color-hex.com/color-palette/165
COLOR_1 = "#fffeb3"
COLOR_2 = "#666547"
COLOR_3 = "#ffe28a"
COLOR_4 = "#fb2e01"
COLOR_5 = "#6fcb9f"
SONG_1 = vlc.MediaPlayer("music/song1.mp3")
FONT = "Sans-Serif"

# Variables
songPlaying = False
numAI = 2
drawCard = ''
canPlayCard = False
chosenCard = ''

junoMain = tk.Tk()
junoMain.title("Juno - The Card Game of the Gods")
junoMain.geometry("1000x500")
PIXEL = tk.PhotoImage(width=1, height=1)

window = tk.Frame(
    master=junoMain,
    width=WIDTH,
    height=HEIGHT,
    bg=COLOR_1
)
window.place(
    x=CEN_X,
    y=CEN_Y,
    anchor='center'
)


def button(text, command, x, y):
    btn = tk.Button(
        master=window,
        width=50,
        height=50,
        bg=COLOR_5,
        image=PIXEL,
        compound='c',
        text=text,
        font=(FONT, 40),
        command=command
    )
    btn.place(
        x=x,
        y=y,
        anchor='center'
    )
    return btn


def playMusic():
    global songPlaying
    if not songPlaying:
        SONG_1.play()
        songPlaying = True
    else:
        SONG_1.pause()
        songPlaying = False


def creditsPage():
    print("")


def ruleBook():
    print("")


music = button('♪', playMusic, CEN_X / 6, CEN_Y)
ruleBookMenu = button('?', ruleBook, CEN_X / 6, CEN_Y / 2)
creditMenu = button('Credits', creditsPage, CEN_X / 6, CEN_Y + (CEN_Y / 2))
creditMenu.config(font=(FONT, 12))

startMenu = tk.Frame(
    master=window,
    width=WIDTH / 1.5,
    height=HEIGHT / 1.1,
    bg=COLOR_3
)

startMenu.place(
    x=CEN_X,
    y=CEN_Y,
    anchor='center'
)

title = tk.Label(
    master=window,
    fg=COLOR_4,
    bg=COLOR_3,
    text="JUNO",
    font=(FONT, 100, 'bold'),
    image=PIXEL,
    compound='c'
)

title.place(
    x=CEN_X,
    y=CEN_Y / 2,
    anchor='center'
)


def setAINum2():
    global numAI
    numAI = 2


def setAINum3():
    global numAI
    numAI = 3


def setAINum4():
    global numAI
    numAI = 4


setAINum = [setAINum2, setAINum3, setAINum4]

numAIButtons = ['', '', '']
for i in range(3):
    numAIButtons[i] = button(i + 2, setAINum[i], CEN_X + ((i - 1) * 100), CEN_Y + (CEN_Y / 1.4))


numAILabel = tk.Label(
    master=window,
    image=PIXEL,
    compound='c',
    text='# of AI:',
    font=(FONT, 20),
    bg=COLOR_3
)
numAILabel.place(
    x=CEN_X/1.6,
    y=CEN_Y+(CEN_Y/1.4),
    anchor='center'
)


def game():
    userHand = ['Human']
    robots = []
    players = [userHand]
    gameRunning = True
    class Card:
        def __init__(self):
            i = random.randint(0, 14)
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'R', 'S', 'D', 'W', 'W4']
            self.number = numbers[i]
            if self.number != 'W' and self.number != 'W4':
                j = random.randint(0, 3)
                colors = ['yellow', 'blue', 'red', 'green']
                self.color = colors[j]
                self.text = 'black'
            else:
                self.color = 'black'
                self.text ='white'

    def topCard(card):
        displayCard = tk.Button(
            master=window,
            image=PIXEL,
            compound='c',
            width=130,
            height=200,
            text=card.number,
            bg=card.color,
            fg=card.text,
            font=(FONT, 100)
        )
        displayCard.place(
            x=CEN_X,
            y=CEN_Y,
            anchor='center'
        )
    def playUserCard():
        global canPlayCard
        if canPlayCard:
            topCard(chosenCard)
            canPlayCard = False


    def displayUserCards():
        for i in range(len(userHand)):
            if not userHand[i] == 'Human':
                card = tk.Button(
                    master=window,
                    image=PIXEL,
                    compound='c',
                    height=80,
                    width=50,
                    text=userHand[i].number,
                    bg=userHand[i].color,
                    fg=userHand[i].text,
                    font=(FONT,40),
                    command=playUserCard
                )
                card.place(
                    x=CEN_X + ((i - 4) * 100),
                    y=CEN_Y + (CEN_Y / 2) + 50,
                    anchor='center'
                )
            chosenCard = userHand[i]

    def gameStart():
        topCard(Card())
        for i in range(7):
            userHand.append(Card())
        for j in range(numAI):
            robots.append([])
            for k in range(7):
                robots[j].append(Card())
        for l in range(numAI):
            players.append(robots[l])
        displayUserCards()

    def playCard():
        canPlayCard = True
        displayUserCards()
        time.sleep(30)


    def robotPickCard(robot):
        r = random.randint(0, len(robot)-1)
        topCard(robot[r])
        print(robot[r].color, robot[r].number)

    def gameLoop():
        r = random.randint(0, numAI)
        while True:
            junoMain.update()
            player = players[r]
            print(player[0]=='Human')
            if player[0] == 'Human':
                playCard()
            else:
                time.sleep(2)
                robotPickCard(player)
            if r == numAI:
                r = 0
            else:
                r += 1


    gameStart()
    gameLoop()

def changeScreen():
    for child in window.winfo_children():
        if child != music and child != ruleBookMenu:
            child.destroy()
    music.place(
        x=CEN_X / 14,
        y=CEN_Y / 7,
        anchor='center'
    )
    ruleBookMenu.place(
        x=CEN_X / 14,
        y=CEN_Y / 2.5,
        anchor='center'
    )
    game()


start = button('START', changeScreen, CEN_X, CEN_Y + (CEN_Y / 2) / 2)
start.config(width=250, height=100, font=(FONT, 50, 'bold'))

junoMain.mainloop()
