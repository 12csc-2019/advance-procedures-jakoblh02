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


# Variables
songPlaying = False
numAI = 2
drawCard = ''
drawButtonNotPressed = True
canPlayCard = False
chosenCard = ' '
skipTurn = False
reverse = False
pickUpTwo = False
pickUpFour = False
colors = ['red', 'blue', 'green', 'yellow']

junoMain = tk.Tk()
junoMain.title("Juno - The Card Game of the Gods")
junoMain.geometry("1000x500")
PIXEL = tk.PhotoImage(width=1, height=1)



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

def frame(master, width, height, bg, x, y):
    frame = tk.Frame(
        master=master,
        width=width,
        height=height,
        bg=bg
    )
    frame.place(
        x=x,
        y=y,
        anchor='center'
    )
    return frame


def label(master, text, fontSize, bg, x, y):
    FONT = "Sans-Serif"

    label = tk.Label(
        master=master,
        text=text,
        font=(FONT, fontSize),
        bg=bg
    )
    label.place(
        x=x,
        y=y,
        anchor='center'
    )

    return label

window = frame(junoMain, WIDTH, HEIGHT, COLOR_1, CEN_X, CEN_Y)

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
    rulesbg = frame(rules, WIDTH/1.3, 300, COLOR_4, WIDTH/1.3/2, 150)
    rulesfg = frame(rules, WIDTH/1.3-10,HEIGHT/2+40, COLOR_1, WIDTH/1.3/2, 150)

    titleText = "Rules of Juno"
    bodyText = """
        To play a card, it must either match the colour or number of the card on the top of the deck, unless its a wild card which can be placed on any card.
        If a card is not played, you must draw a new card from the deck.
        The player can only play one card at a time.
        The winner of the game is the first person to play all their cards.

        Action Cards:

        Reverse: Changes direction of play. 
        Skip: Skips the next player's turn.
        Draw Two: Next player draws two cards into their deck, and forfeits their turn.
        Wild: Allows the player to change the colour of the deck.
        Wild Draw Four: Next player draws four cards into their deck, and forfeits their turn. The current player picks a new colour for the deck as well.
        """

    rulesTitle = label(rules, titleText, 20, COLOR_1, WIDTH/1.3/2, 50)
    rulesText = label(rules, bodyText, 8, COLOR_1, WIDTH/1.3/2, 170)


def endProgram():
    junoMain.destroy()


music = button('♪', playMusic, CEN_X / 6, CEN_Y)
ruleBookMenu = button('?', ruleBook, CEN_X / 6, CEN_Y / 2)
creditMenu = button('Credits', creditsPage, CEN_X / 6, CEN_Y + (CEN_Y / 2))
stopButton = button('X', endProgram, 2 * CEN_X - 50, 50)
creditMenu.config(font=(FONT, 12))

startMenu = frame(window, WIDTH/1.5, HEIGHT/1.1, COLOR_3, CEN_X, CEN_Y)
title = label(window, COLOR_3, "JUNO", 100, CEN_X, CEN_Y/2)
title.config(
    font=("Sans-Serif", 100, 'bold'),
    fg = COLOR_4
)


def setAINum(i):
    global numAI
    numAI = i + 2
    for j in range(3):
        if j == i:
            numAIButtons[j].config(
                bg=COLOR_1
            )
        else:
            numAIButtons[j].config(
                bg=COLOR_5
            )


numAIButtons = ['', '', '']
for i in range(3):
    numAIButtons[i] = button(i + 2, partial(setAINum, i), CEN_X + ((i - 1) * 100), CEN_Y + (CEN_Y / 1.4))

numAILabelText = '# of AI:'
numAILabel = label(window, numAILabelText, 20, COLOR_3, CEN_X/1.6, CEN_Y+(CEN_Y/1.4))


def game():
    global colors
    userHand = ['Human']
    robots = []
    players = [userHand]
    playerCards = []

    class Card:
        def __init__(self):
            global colors
            i = random.randint(0, 14)
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'R', 'S', 'D', 'W', 'W4']
            self.number = numbers[i]
            if self.number != 'W' and self.number != 'W4':
                j = random.randint(0, 3)
                self.color = colors[j]
                self.text = 'black'
            else:
                self.color = 'black'
                self.text = 'white'

    currentTopCard = Card()
    if currentTopCard.color == 'black':
        r = random.randint(0, 3)
        currentTopCard.color = colors[r]

    def topCard(card):
        fontSize = 100
        changeDisplayedCharacter = ['R', 'S', 'D', 'W', 'W4']
        if card.number in changeDisplayedCharacter:
            if card.number == 'R':
                cardText = '↻'
            elif card.number == 'S':
                cardText = 'Ø'
            elif card.number == 'D':
                cardText = '+2'
                fontSize = 90
            elif card.number == 'W':
                cardText = 'WILD'
                fontSize = 40
            elif card.number == 'W4':
                cardText = '+4'
                fontSize = 90
        else:
            cardText = card.number
        displayCard = tk.Button(
            master=window,
            image=PIXEL,
            compound='c',
            width=130,
            height=200,
            text=cardText,
            bg=card.color,
            fg=card.text,
            font=(FONT, fontSize)
        )
        displayCard.place(
            x=CEN_X,
            y=CEN_Y,
            anchor='center'
        )
        global currentTopCard
        currentTopCard = card

    def chooseChosenCard(card, i):
        global currentTopCard
        global chosenCard
        if card.color != currentTopCard.color and card.number != currentTopCard.number and card.color != 'black':
            chosenCard = ' '
        else:
            chosenCard = card
            for c in playerCards:
                c.destroy()
            userHand.pop(i)

    def displayUserCards():
        for i in range(len(userHand)):
            if userHand[i] != 'Human':
                fontSize = 40
                changeDisplayedCharacter = ['R', 'S', 'D', 'W', 'W4']
                if userHand[i].number in changeDisplayedCharacter:
                    if userHand[i].number == 'R':
                        cardText = '↻'
                    elif userHand[i].number == 'S':
                        cardText = 'Ø'
                    elif userHand[i].number == 'D':
                        cardText = '+2'
                        fontSize = 35
                    elif userHand[i].number == 'W':
                        cardText = 'WILD'
                        fontSize = 15
                    elif userHand[i].number == 'W4':
                        cardText = '+4'
                        fontSize = 35
                else:
                    cardText = userHand[i].number
                card = tk.Button(
                    master=window,
                    image=PIXEL,
                    compound='c',
                    height=80,
                    width=50,
                    text=cardText,
                    bg=userHand[i].color,
                    fg=userHand[i].text,
                    font=(FONT, fontSize),
                    command=partial(chooseChosenCard, userHand[i], i)
                )
                card.place(
                    x=(CEN_X - 500) + (i * 70),
                    y=CEN_Y + (CEN_Y / 2) + 50,
                    anchor='center'
                )
                playerCards.append(card)

    def doesntDoAnything():
        print("Doesn't Do Anything")

    def drawACard():
        global drawButtonNotPressed
        drawButtonNotPressed = False
        userHand.append(Card())
        junoMain.update()
        displayUserCards()

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
        numAICardsLabelText
        numAICardsLabel = label(junoMain, numAICardsLabelText, 20, COLOR_1, CEN_X+200, CEN_Y-50)

    def playCard():
        displayUserCards()
        notPickedColor = True
        global drawButtonNotPressed
        global chosenCard
        global currentTopCard
        continueWaiting = True
        oldtime = time.time()
        timeLeft = (30 - (time.time() - oldtime))
        countdownText = "Time Left: " + str(timeLeft)

        countdown = label(junoMain, countdownText, 20, COLOR_1, CEN_X, CEN_Y/2)

        colorButtons = []

        def colorButtonHandler(color):
            global colorButtons
            global continueWaiting
            global chosenCard
            global currentTopCard
            global drawButtonNotPressed
            continueWaiting = False
            if chosenCard.color == 'black':
                chosenCard.color = color

        global colors
        colorButtonsLabelText = "Wild Card Color:"
        colorButtonsLabel = label(window, colorButtonsLabelText, 20, COLOR_1, CEN_X-250, CEN_Y-100)
        colorButtonsLabel.config(
            font=("Sans-Serif", 20, 'bold')
        )

        for b in range(4):
            colorButtons.append(
                button('', partial(colorButtonHandler, colors[b]), (CEN_X - 400) + (b * 100), CEN_Y - 50))
            colorButtons[b].config(
                bg=colors[b]
            )

        while continueWaiting and drawButtonNotPressed:
            junoMain.update()
            timeLeft = (30 - round((time.time() - oldtime)))
            countdown.config(
                text="Time Left: " + str(timeLeft)
            )
            if chosenCard != ' ':
                if chosenCard.color != 'black':
                    topCard(chosenCard)
                    currentTopCard = chosenCard
                    chosenCard = ' '
                    continueWaiting = False
                    countdown.destroy()
                    displayUserCards()

            if (time.time() - oldtime) > 29:
                continueWaiting = False
                r = random.randint(1, len(userHand) - 1)
                topCard(userHand[r])
                countdown.destroy()
                displayUserCards()
        drawButtonNotPressed = True

    def robotPickCard(robot):
        global colors
        global currentTopCard
        dontPickUpCard = False
        for c in range(len(robot)):
            if robot[c].color == currentTopCard.color or robot[c].number == currentTopCard.number or robot[c].color == 'black':
                dontPickUpCard = True
                if robot[c].color == 'black':
                    randomColor = random.randint(0, 3)
                    robot[c].color = colors[randomColor]
                    topCard(robot[c])
                    robot.pop(c)
                    junoMain.update()
                    break
                else:
                    topCard(robot[c])
                    robot.pop(c)
                    junoMain.update()
                    break
        if not dontPickUpCard:
            robot.append(Card())

    def gameLoop():
        global skipTurn
        global reverse
        global pickUpTwo
        global pickUpFour
        global drawButton
        global currentTopCard
        global chosenCard
        r = random.randint(0, numAI)
        noWinner = True
        while noWinner:
            try:
                numberOfCards.destroy()
            except:
                pass
            for p in range(len(players)):
                if players[p][0] != 'Human':
                    numberOfCards = button(str(len(players[p])), doesntDoAnything, CEN_X + 80 + (p * 80), CEN_Y)
            if currentTopCard.number == 'S':
                skipTurn = True
            if currentTopCard.number == 'D':
                pickUpTwo = True
            if currentTopCard.number == 'W4':
                pickUpFour = True
            junoMain.update()
            player = players[r]
            if player[0] == 'Human':
                chosenCard = ' '
                if skipTurn:
                    skipTurn = False
                    currentTopCard.number = 'Z'
                elif pickUpTwo:
                    userHand.append(Card())
                    userHand.append(Card())
                    pickUpTwo = False
                    currentTopCard.number = '+2'
                elif pickUpFour:
                    for a in range(4):
                        userHand.append(Card())
                    pickUpFour = False
                    currentTopCard.number = '+4'
                    displayUserCards()
                else:
                    drawButton = button("DRAW", drawACard, CEN_X / 2, CEN_Y + 20)
                    drawButton.config(
                        width=170
                    )
                    yourTurn = label(junoMain, "Your Turn!", 30, COLOR_1, CEN_X, CEN_Y/4)
                    playCard()
                    yourTurn.destroy()
                    if currentTopCard.number == 'R':
                        if reverse:
                            reverse = False
                        else:
                            reverse = True
            else:
                if skipTurn:
                    skipTurn = False
                    currentTopCard.number = 'Z'
                elif pickUpTwo:
                    player.append(Card())
                    player.append(Card())
                    pickUpTwo = False
                    currentTopCard.number = '+2'
                elif pickUpFour:
                    for a in range(4):
                        player.append(Card())
                    pickUpFour = False
                    currentTopCard.number = '+4'
                else:
                    randomTime = 3
                    time.sleep(randomTime)
                    robotPickCard(player)
                    if currentTopCard.number == 'R':
                        if reverse:
                            reverse = False
                        else:
                            reverse = True
            for t in range(len(players)):
                if players[0] != "Human":
                    if len(players[t]) == 0:
                        noWinner = False
                        junoMain.destroy()
                elif len(userHand) == 1:
                    noWinner = False
                    junoMain.destroy()
            if not reverse:
                if r == numAI:
                    r = 0
                else:
                    r += 1
            else:
                if r == 0:
                    r = numAI
                else:
                    r -= 1

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
