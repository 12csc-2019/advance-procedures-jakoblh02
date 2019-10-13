import tkinter as tk
import random
import vlc
import time
from functools import partial

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
chosenCard = ' '

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
    rules = tk.Toplevel()
    rules.title("Rule Book")
    rules.geometry("771x301")
    PX = tk.PhotoImage(width=1, height=1)
    rulesbg = tk.Frame(
        master=rules,
        width=WIDTH / 1.3,
        height=300,
        bg=COLOR_4
    )
    rulesbg.place(
        x=WIDTH/1.3/2,
        y=300/2,
        anchor='center'
    )
    rulesfg = tk.Frame(
        master=rules,
        width=WIDTH / 1.3 - 10,
        height=HEIGHT / 2 + 40,
        bg=COLOR_1
    )
    rulesfg.place(
        x=WIDTH / 1.3 / 2,
        y=300/2,
        anchor='center'
    )
    rulesTitle = tk.Label(
        master=rules,
        text='Rules of Juno',
        font=(FONT, 20),
        bg=COLOR_1
    )
    rulesTitle.place(
        x=WIDTH/1.3/2,
        y=300/2-100,
        anchor='center'
    )
    rulesText = tk.Label(
        master=rules,
        text=("""
        To play a card, it must either match the colour or number of the card on the top of the deck, unless its a wild card which can be placed on any card.
        If a card is not played, you must draw a new card from the deck.
        The player can only play one card at a time.
        The player must click the JUNO button when they have one card left otherwise they must pick up 2 more cards.
        The winner of the game is the first person to play all their cards.

        Action Cards:

        Reverse: Changes direction of play. 
        Skip: Skips the next player's turn.
        Draw Two: Next player draws two cards into their deck, and forfeits their turn.
        Wild: Allows the player to change the colour of the deck.
        Wild Draw Four: Next player draws four cards into their deck, and forfeits their turn. The current player picks a new colour for the deck as well.
        """),
        font=(FONT, 8),
        bg=COLOR_1
    )

    rulesText.place(
        x=WIDTH/1.3/2,
        y=300/2+20,
        anchor='center'
    )


def endProgram():
    junoMain.destroy()

music = button('♪', playMusic, CEN_X / 6, CEN_Y)
ruleBookMenu = button('?', ruleBook, CEN_X / 6, CEN_Y / 2)
creditMenu = button('Credits', creditsPage, CEN_X / 6, CEN_Y + (CEN_Y / 2))
stopButton = button('X', endProgram, 2*CEN_X-50, 50)
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
    numRobotCards = []
    playerCards = []
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

    currentTopCard = Card()

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
        global currentTopCard
        currentTopCard = card

    def chooseChosenCard(card, i):
        global chosenCard
        chosenCard = card
        playerCards[i].destroy()
        userHand.pop(i-1)


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
                    command=partial(chooseChosenCard, userHand[i], i)
                )
                card.place(
                    x=CEN_X + ((i - 4) * 100),
                    y=CEN_Y + (CEN_Y / 2) + 50,
                    anchor='center'
                )
                playerCards.append(card)

    def doesntDoAnything():
        print("Doesn't Do Anything")

    def drawACard(player):
        player.append(Card())

    def gameStart():
        topCard(currentTopCard)
        for i in range(7):
            userHand.append(Card())
        for j in range(numAI):
            robots.append([])
            for k in range(7):
                robots[j].append(Card())
        for l in range(numAI):
            players.append(robots[l])
        displayUserCards()
        for m in range(len(robots)):
            numRobotCards.append(button(len(robots[m]), doesntDoAnything, CEN_X+(m*60)+200, CEN_Y))
        drawButton = button("DRAW",partial(drawACard, userHand), CEN_X/2, CEN_Y)
        drawButton.config(
            width=170
        )

    def playCard():
        displayUserCards()
        global chosenCard
        global currentTopCard
        continueWaiting = True
        oldtime = time.time()
        timeLeft = (30 - (time.time() - oldtime))
        countdownText = str(timeLeft)
        countdown = tk.Label(
            master=junoMain,
            text=countdownText,
            font=(FONT,20)
        )
        countdown.place(
            x=CEN_X,
            y=CEN_Y/2,
            anchor='center'
        )

        while continueWaiting:
            junoMain.update()
            timeLeft = (30 - round((time.time() - oldtime)))
            countdown.config(
                text=str(timeLeft)
            )
            if chosenCard != ' ':
                topCard(chosenCard)
                currentTopCard = chosenCard
                chosenCard = ' '
                continueWaiting = False
                countdown.destroy()
                displayUserCards()
            if (time.time() - oldtime) > 29:
                continueWaiting = False
                r = random.randint(1, len(userHand)-1)
                topCard(userHand[r])
                countdown.destroy()
                displayUserCards()

    def robotPickCard(robot):
        global currentTopCard
        i = 0
        for c in range(len(robot)-1):
            if robot[c].color == currentTopCard.color or robot[c].number == currentTopCard.number or robot[c].color == 'black':
                topCard(robot[c])
                robot.pop(c)
                break
            elif i > len(robot):
                robot.append(Card())
            i = i+1

    def gameLoop():
        global currentTopCard
        r = random.randint(0, numAI)
        noWinner = True
        while noWinner:
            junoMain.update()
            player = players[r]
            if player[0] == 'Human':
                yourTurn = tk.Label(
                    master=junoMain,
                    text="Your Turn!",
                    font=(FONT, 30)
                )
                yourTurn.place(
                    x=CEN_X,
                    y=CEN_Y / 4,
                    anchor='center'
                )
                playCard()
                yourTurn.destroy()
            else:
                randomTime = random.randint(2,5)
                time.sleep(randomTime)
                robotPickCard(player)
                for q in range(len(players)):
                    numRobotCards[q-1].config(
                        text=len(players[q])
                    )
            for t in range(len(players)):
                if players[0] != "Human":
                    if len(players[t]) == 0:
                        noWinner = False
                        junoMain.destroy()
                elif len(players[t]) == 1:
                    noWinner = False
                    junoMain.destroy()
            if r == numAI:
                r = 0
            else:
                r += 1


    gameStart()
    gameLoop()

def changeScreen():
    for child in window.winfo_children():
        if child != music and child != ruleBookMenu and child != stopButton:
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
