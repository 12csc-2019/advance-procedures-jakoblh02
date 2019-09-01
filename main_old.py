import tkinter as tK
import random
import vlc

# Colors - Ref: https://www.color-hex.com/
theme1 = "#428bca"
theme2 = "#5bc0de"
theme3 = "#5cb85c"
theme4 = "#d9534f"
theme5 = "#b3cde0"

# Constants
WIDTH = 1000
HEIGHT = 500

# Variables
p = vlc.MediaPlayer('music\song1.mp3')
playersCards = []
numPlayersCards = 0

junoMain = tK.Tk()
pixel = tK.PhotoImage(width=1, height=1)
junoMain.title("JUNO - The Card Game of the Gods")
junoMain.geometry('1000x500')

window = tK.Frame(master=junoMain, width=WIDTH, height=HEIGHT, bg=theme1)
window.place(x=WIDTH/2, y=HEIGHT/2,anchor='center')


# Function to handle Music Button
def music():
    global musicPlaying
    if not musicPlaying:
        p.play()
        musicButton.config(text='⏸')
        musicPlaying = True
    elif musicPlaying:
        p.pause()
        musicButton.config(text='▷')
        musicPlaying = False


# Music Button
musicPlaying = False
musicButton = tK.Button(
    master=window,
    text="▷",
    command=music,
    font=("Sans-Serif", 50, "bold"),
    image=pixel,
    width=50,
    height=50,
    compound='c',
    background=theme4
)

musicButton.place(x=40, y=40, anchor='center')


# Title
junoTitle = tK.Label(
    master=window,
    text="JUNO",
    font=("Times New Roman", 150, "bold"),
    image=pixel,
    compound="c",
    background=theme1,
    foreground='white'
)
junoTitle.place(x=WIDTH/2, y=HEIGHT/2-100, anchor='center')


# Main Game
def junoGame():
    global numPlayersCards
    def displayPlayersCards(currentCard, i):
        card = tK.Button(
            master=window,
            width=50,
            height=80,
            image=pixel,
            text=currentCard.cardText,
            font=("Times New Roman", currentCard.fontSize, 'bold'),
            compound='c',
            background=currentCard.color,
            foreground=currentCard.cardTextColor
        )
        card.place(x=(i*80)+50,y=HEIGHT-70, anchor='center')

    for i in range(7):
        playersCards.append('')
        playersCards[i] = Card()
        displayPlayersCards(playersCards[i], i)

    numPlayersCards = 7
    topCard = Card()
    displayTopCard = tK.Button(
        master=window,
        width=100,
        height=160,
        image=pixel,
        text=topCard.cardText,
        font=("Times New Roman", topCard.fontSize, 'bold'),
        compound='c',
        background=topCard.color,
        foreground=topCard.cardTextColor
    )
    displayTopCard.place(x=WIDTH/4, y=HEIGHT/3, anchor='center')
    topCardLabel = tK.Label(
        master=window,
        text='Top Card:',
        image=pixel,
        font=("Times New Roman", 30, 'bold'),
        compound='c',
        background=theme1,
        foreground='black'
    )
    topCardLabel.place(x=WIDTH/4, y=HEIGHT/3-110, anchor='center')



# Start Button
def startButtonPressed():
    startButton.destroy()
    junoTitle.destroy()
    junoGame()


startButton = tK.Button(
    master=window,
    text="START",
    font=("Sans-Serif", 50, "bold"),
    image=pixel,
    compound="c",
    width=300,
    height=100,
    background=theme4,
    command=startButtonPressed
)
startButton.place(x=WIDTH/2,y=HEIGHT/2+100, anchor='center')



class Card():
    def __init__(self):
        j = random.randint(0,14)
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "R", "S", "DT", "W", "WF"]
        self.number = numbers[j]

        if type(self.number) == int:
            i = random.randint(0,3)
            color = ['red', 'blue', 'green', 'yellow']
            self.color = color[i]
        else:
            self.color = 'black'

        self.fontSize = 40
        if type(self.number) == int:
            self.cardText = self.number
        elif self.number == "R":
            self.cardText = "↻"
        elif self.number == "S":
            self.cardText = '⍉'
        elif self.number == "DT":
            self.cardText = "+2"
        elif self.number == "WF":
            self.cardText = "+4"
        elif self.number == "W":
            self.cardText = "WILD"
            self.fontSize = 15

        if type(self.number) == int:
            self.cardTextColor = 'black'
        else:
            self.cardTextColor = 'white'



# Create Deck
def drawNewCard():
    card = Card()
    return card




junoMain.mainloop()
