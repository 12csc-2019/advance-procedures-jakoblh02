# Importing libraries
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
# Music Player
songPlaying = False
# Special Card Abilities
skipTurn = False
reverse = False
pickUpTwo = False
pickUpFour = False
# Number of Robots
numAI = 2
# Related to the user being able to play cards
drawCard = ''
drawButtonNotPressed = True
canPlayCard = False
chosenCard = ' '
# Colors
colors = ['red', 'blue', 'green', 'yellow']


# Creates button object
def button(text, command, x, y):
    btn = tk.Button(
        master=window,
        width=50,
        height=50,
        bg=COLOR_5,
        image=PIXEL,
        compound='c',
        text=text,
        font=("Sans-Serif", 40),
        command=command
    )
    btn.place(
        x=x,
        y=y,
        anchor='center'
    )
    return btn


# Creates frame object
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


# Creates label object
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


# Music Player
def playMusic():
    global songPlaying
    if not songPlaying:
        SONG_1.play()
        songPlaying = True
    else:
        SONG_1.pause()
        songPlaying = False


# Creates credits window
def creditsPage():
    credits = tk.Toplevel()
    credits.title("Credits")
    credits.geometry("771x301")
    # Background, Foreground colors
    creditsBg = frame(credits, WIDTH / 1.3, 300, COLOR_4, WIDTH / 1.3 / 2, 150)
    creditsFg = frame(credits, WIDTH / 1.3 - 10, HEIGHT / 2 + 40, COLOR_1, WIDTH / 1.3 / 2, 150)

    # Creating text to display
    titleText = "Credits:"
    creditTxtFile = open('credits.txt', 'r')
    bodyText = creditTxtFile.read()
    creditTxtFile.close()

    # Displaying text
    creditsTitle = label(credits, titleText, 20, COLOR_1, WIDTH / 1.3 / 2, 50)
    creditsText = label(credits, bodyText, 8, COLOR_1, WIDTH / 1.3 / 2, 170)

# Creates rule book window
def ruleBook():
    rules = tk.Toplevel()
    rules.title("Rule Book")
    rules.geometry("771x301")
    # Background, Foreground colors
    rulesBg = frame(rules, WIDTH/1.3, 300, COLOR_4, WIDTH/1.3/2, 150)
    rulesFg = frame(rules, WIDTH/1.3-10,HEIGHT/2+40, COLOR_1, WIDTH/1.3/2, 150)

    # Creating text to display
    titleText = "Rules of Juno"
    ruleTxtFile = open('rules.txt', 'r')
    bodyText = ruleTxtFile.read()
    ruleTxtFile.close()

    # Displaying text
    rulesTitle = label(rules, titleText, 20, COLOR_1, WIDTH/1.3/2, 50)
    rulesText = label(rules, bodyText, 8, COLOR_1, WIDTH/1.3/2, 170)


# Ends Program
def endProgram():
    junoMain.destroy()


# Creating main window
junoMain = tk.Tk()
junoMain.title("Juno - The Card Game of the Gods")
junoMain.geometry("1000x500")
PIXEL = tk.PhotoImage(width=1, height=1)
window = frame(junoMain, WIDTH, HEIGHT, COLOR_1, CEN_X, CEN_Y)

# Various home screen buttons
music = button('♪', playMusic, CEN_X / 6, CEN_Y)
ruleBookMenu = button('?', ruleBook, CEN_X / 6, CEN_Y / 2)
creditMenu = button('Credits', creditsPage, CEN_X / 6, CEN_Y + (CEN_Y / 2))
stopButton = button('X', endProgram, 2 * CEN_X - 50, 50)
creditMenu.config(font=("Sans-Serif", 12))

# Home Screen design
startMenu = frame(window, WIDTH/1.5, HEIGHT/1.1, COLOR_3, CEN_X, CEN_Y)
title = label(window, "JUNO",  100, COLOR_3, CEN_X, CEN_Y/2)
title.config(
    font=("Sans-Serif", 100, 'bold'),
    fg = COLOR_4
)


# Setting the number of AI to i
def setAINum(i):
    global numAI
    numAI = i + 2
    # Highlighting selected button
    for j in range(3):
        if j == i:
            numAIButtons[j].config(
                bg=COLOR_1
            )
        else:
            numAIButtons[j].config(
                bg=COLOR_5
            )

# Creating numAI buttons
numAIButtons = ['', '', '']
for i in range(3):
    numAIButtons[i] = button(i + 2, partial(setAINum, i), CEN_X + ((i - 1) * 100), CEN_Y + (CEN_Y / 1.4))

# Label telling user what the numAI buttons do
numAILabelText = '# of AI:'
numAILabel = label(window, numAILabelText, 20, COLOR_3, CEN_X/1.6, CEN_Y+(CEN_Y/1.4))


# Main game function
def game():
    # Globals
    global colors

    # Variables
    userHand = ['Human']
    robots = []
    players = [userHand]
    playerCards = []

    # Card Object
    class Card:
        def __init__(self):
            global colors
            # Randomizing the card
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

    # Creates the initial top card
    currentTopCard = Card()
    # If the color is black it changes it to something random
    if currentTopCard.color == 'black':
        r = random.randint(0, 3)
        currentTopCard.color = colors[r]

    # Function for displaying top card
    def topCard(card):
        # Default fontSize
        fontSize = 100
        # Characters to change the text for
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
        # Displaying the card, doesn't work with the button() function I created for some reason
        displayCard = tk.Button(
            master=window,
            image=PIXEL,
            compound='c',
            width=130,
            height=200,
            text=cardText,
            bg=card.color,
            fg=card.text,
            font=("Sans-Serif", fontSize)
        )
        displayCard.place(
            x=CEN_X,
            y=CEN_Y,
            anchor='center'
        )
        # Setting the current top card to whatever card
        global currentTopCard
        currentTopCard = card

    # Function for the card buttons in the user hand
    # Sets chosenCard to the chosen card if it follows the card rules.
    def chooseChosenCard(card, i):
        global currentTopCard
        global chosenCard
        # Checks if the card is any of these and allows you to play a card onto the same action card.
        skip = True
        draw2 = True
        draw4 = True
        if currentTopCard.number == 'Z':
            if currentTopCard.number == 'S':
                skip = False
        if currentTopCard.number == '+2':
            if currentTopCard.number == 'D':
                draw2 = False
        if currentTopCard.number == '+4':
            if currentTopCard.number == 'W4':
                draw4 = False

        # If the card fails this you can't play it
        if card.color != currentTopCard.color and card.number != currentTopCard.number and card.color != 'black' and skip and draw2 and draw4:
            chosenCard = ' '
        else:
            chosenCard = card
            for c in playerCards:
                c.destroy()
            userHand.pop(i)

    # Function that displays the users cards
    def displayUserCards():
        for i in range(len(userHand)):
            if userHand[i] != 'Human':
                # Default font
                fontSize = 40
                # For changing the displayed characters
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
                # Displays the cards
                card = tk.Button(
                    master=window,
                    image=PIXEL,
                    compound='c',
                    height=80,
                    width=50,
                    text=cardText,
                    bg=userHand[i].color,
                    fg=userHand[i].text,
                    font=("Sans-Serif", fontSize),
                    command=partial(chooseChosenCard, userHand[i], i)
                )
                card.place(
                    x=(CEN_X - 500) + (i * 70),
                    y=CEN_Y + (CEN_Y / 2) + 50,
                    anchor='center'
                )
                playerCards.append(card)

    # doesn't do anything, needed cause tkinter buttons need to be provided a command.
    def doesntDoAnything():
        print("Doesn't Do Anything")

    # Adds a card to user hand when you click the draw button
    def drawACard():
        global drawButtonNotPressed
        drawButtonNotPressed = False
        userHand.append(Card())
        junoMain.update()
        displayUserCards()

    # Initializes the game
    def gameStart():
        # sets top card to currentTopCard
        topCard(currentTopCard)
        # Gives player cards
        for i in range(7):
            userHand.append(Card())
        # Gives robots cards
        for j in range(numAI):
            robots.append([])
            for k in range(7):
                robots[j].append(Card())
        # appends both to the list of players
        for l in range(numAI):
            players.append(robots[l])
        # displays the users cards
        displayUserCards()
        # Text telling the user what the AI Card numbers do
        numAICardsLabelText = "AI Card #:"
        numAICardsLabel = label(junoMain, numAICardsLabelText, 20, COLOR_1, CEN_X+200, CEN_Y-50)

    # Allows the user to play a card
    def playCard():
        displayUserCards()
        global drawButtonNotPressed
        global chosenCard
        global currentTopCard

        continueWaiting = True

        # Countdown label
        oldtime = time.time()
        timeLeft = (30 - (time.time() - oldtime))
        countdownText = "Time Left: " + str(timeLeft)
        countdown = label(junoMain, countdownText, 20, COLOR_1, CEN_X, CEN_Y/2)

        # list that will contain buttons
        colorButtons = []

        # sets the color if the card's color is black to whatever the user wants it to be
        def colorButtonHandler(color):
            global colorButtons
            global continueWaiting
            global chosenCard
            global currentTopCard
            global drawButtonNotPressed
            continueWaiting = False
            if chosenCard.color == 'black':
                chosenCard.color = color

        # Label for the wild card color selector
        global colors
        colorButtonsLabelText = "Wild Card Color:"
        colorButtonsLabel = label(window, colorButtonsLabelText, 20, COLOR_1, CEN_X-250, CEN_Y-100)
        colorButtonsLabel.config(
            font=("Sans-Serif", 20, 'bold')
        )

        # Creates color buttons
        for b in range(4):
            colorButtons.append(
                button('', partial(colorButtonHandler, colors[b]), (CEN_X - 400) + (b * 100), CEN_Y - 50))
            colorButtons[b].config(
                bg=colors[b]
            )

        # While loop that waits for user to play card and if they don't it times out
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

    # Allows the robots to play a card
    # For sections that are the same as above you can read the playCard() function comments
    def robotPickCard(robot):
        global colors
        global currentTopCard
        dontPickUpCard = False
        skip = False
        draw2 = False
        draw4 = False
        for c in range(len(robot)):
            if robot[c].number == 'Z':
                if currentTopCard.number == 'S':
                    skip = True
            if robot[c].number == '+2':
                if currentTopCard.number == 'D':
                    draw2 = True
            if robot[c].number == '+4':
                if currentTopCard.number == 'W4':
                    draw4 = True

            if robot[c].color == currentTopCard.color or robot[c].number == currentTopCard.number or robot[c].color == 'black' or skip or draw2 or draw4:
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

    # Main game loop that allows the players to play in turns
    def gameLoop():
        global skipTurn
        global reverse
        global pickUpTwo
        global pickUpFour
        global drawButton
        global currentTopCard
        global chosenCard
        # selects random player to play first
        r = random.randint(0, numAI)

        # Creates variable for the while loop checking if someone isn't winner
        noWinner = True
        # while loop checking if no one has one and continuing play
        while noWinner:
            # displays users cards
            displayUserCards()
            # destroys the ai card numbers if they exist
            try:
                numberOfCards.destroy()
            except:
                pass
            # creates the number ai card buttons
            for p in range(len(players)):
                if players[p][0] != 'Human':
                    numberOfCards = button(str(len(players[p])), doesntDoAnything, CEN_X + 80 + (p * 80), CEN_Y)
            # if statements checking if either of these cards have been played
            if currentTopCard.number == 'S':
                skipTurn = True
            if currentTopCard.number == 'D':
                pickUpTwo = True
            if currentTopCard.number == 'W4':
                pickUpFour = True
            # updates the screen
            junoMain.update()
            # sets the current player
            player = players[r]
            # if current player is the user
            if player[0] == 'Human':
                chosenCard = ' '
                # skips turn
                if skipTurn:
                    skipTurn = False
                    currentTopCard.number = 'Z'
                # adds two cards to user hand
                elif pickUpTwo:
                    userHand.append(Card())
                    userHand.append(Card())
                    pickUpTwo = False
                    currentTopCard.number = '+2'
                # adds four cards to user hand
                elif pickUpFour:
                    for a in range(4):
                        userHand.append(Card())
                    pickUpFour = False
                    currentTopCard.number = '+4'
                    displayUserCards()
                # if none of the above is true
                else:
                    # creates draw button
                    drawButton = button("DRAW", drawACard, CEN_X / 2, CEN_Y + 20)
                    drawButton.config(
                        width=170
                    )
                    # tells user its their turn
                    yourTurn = label(junoMain, "Your Turn!", 30, COLOR_1, CEN_X, CEN_Y/4)

                    playCard()
                    yourTurn.destroy()
                    # if the user has played a reverse card it reverses
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
start.config(width=250, height=100, font=("Sans-Serif", 50, 'bold'))

junoMain.mainloop()
