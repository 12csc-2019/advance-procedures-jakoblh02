rulesbg = tk.Frame(
    master=junoMain,
    width=WIDTH / 1.3,
    height=HEIGHT / 2 + 50,
    bg=COLOR_4
)
rulesbg.place(
    x=CEN_X,
    y=CEN_Y,
    anchor='center'
)
rules = tk.Frame(
    master=junoMain,
    width=WIDTH / 1.3 - 10,
    height=HEIGHT / 2 + 40,
    bg=COLOR_1
)
rules.place(
    x=CEN_X,
    y=CEN_Y,
    anchor='center'
)
rulesTitle = tk.Label(
    master=junoMain,
    image=PIXEL,
    compound='c',
    text='Rules of Juno',
    font=(FONT, 20),
    bg=COLOR_1
)
rulesTitle.place(
    x=CEN_X,
    y=CEN_Y - 100,
    anchor='center'
)
rulesText = tk.Label(
    master=junoMain,
    image=PIXEL,
    compound='c',
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
    x=CEN_X,
    y=CEN_Y + 20,
    anchor='center'
)


def closeRules():
    rulesbg.destroy()
    rulesText.destroy()
    rules.destroy()
    rulesTitle.destroy()
    rulesClose.destroy()


rulesClose = button('X', closeRules, CEN_X * 1.85, CEN_Y)
rulesClose.config(
    bg='red'
)
