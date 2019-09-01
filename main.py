import tkinter as tk
import random
import vlc

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
hand = []
playersHand = []
player = []

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
creditMenu = button('☀', creditsPage, CEN_X / 6, CEN_Y + (CEN_Y / 2))

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
    global playersHand

    class Card:
        def __init__(self):
            i = random.randint(0, 14)
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'R', 'S', 'D', 'W', 'W4']
            self.number = numbers[i]
            if self.number != 'W' and self.number != 'W4':
                i = random.randint(0, 3)
                colors = ['yellow', 'blue', 'red', 'green']
                self.color = colors[i]
            else:
                self.color = 'black'
    # Give all the players there cards
    for i in range(numAI+1):
        player.append([])
        hand.append([])
        for j in range(7):
            hand[i].append(Card)
    r = random.randint(0,6)
    playersHand = hand[r]
    # Pick a random person to start
    s = random.randint(0,numAI)
    startingPlayer = player[s]
    # Random Card pulled from deck put to top of deck
    topCard = Card
    # Player can pick from playable cards in their hand
    # Any Action associated with that card happens
    # Move to next player
    # Repeat


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
