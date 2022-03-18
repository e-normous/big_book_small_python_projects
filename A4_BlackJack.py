#A. 4 Blackjack
#https://inventwithpython.com/bigbookpython/project4.html


"""Blackjack, also known as 21, is a card game where players try to get as close to 21 points as possible without going over.
This program uses images drawn with text characters, called ASCII art. American Standard Code for Information
Interchange (ASCII) is a mapping of text characters to numeric codes that computers used before Unicode replaced it.
The playing cards in this program are an example of ASCII art:

 ___   ___
|A  | |10 |
| ♣ | | ♦ |
|__A| |_10|
"""



"""Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17."""

import random, sys

#set up the constants:
hearts = chr(9829) #this one is the heart
diamonds = chr(9830)
spades = chr(9824)
clubs = chr(9827)
#find a list of chr codes at https://inventwithpython.com/chractermap
backside = "backside"



def main():
    print('''Blackjack Game
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')

    money = 3000

    while True:
        #check whether players have run out of money:
        if money <= 0:
            print("You are broke!")
            print("Good thing you didn't play real money")
            print("Thank you for playing.")
            sys.exit()
    
        #Let the player enter their bet for this round:
        print(f"Your balance: CHF {money}")
        bet = get_bet(money)

        #give the dealer and player two cards from the deck each:
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        #handle the player's actions:
        print(f"Bet: {bet} CHF")
        
        #looping until player stands or busts:
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()

            #check whether the player has bust:
            if get_hand_value(player_hand) > 21:
                break

            #get the player's move, either H, S, or D:
            move = get_move(player_hand, money - bet)

            #handle the player actions now:
            if move == "D":
                #player is doubling, increasing their bet:
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print(f"Bet increased to {bet} CHF")
                print(f"Bet: {bet} CHF")

            if move in ("H", "D"):
                #Hit/Doubling down takes another card:
                new_card = deck.pop()
                rank, suit = new_card
                print(f"You drew a {rank} of {suit}.")
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    #the player has busted:
                    continue

            if move in ("S", "D"):
                #Stand/Doubling down stops the players turn:
                break

        #handle the dealers actions:
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                #dealer's hitting 'till he reaches 17:
                print("Dealer hits.")
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break #dealer busted
                input("Press Enter to continue...")
                print("\n\n")


        #Show the final hands:
        display_hands(player_hand, dealer_hand, True)

        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        #handle whether the player won, lost or tied:
        if dealer_value > 21:
            print(f"Dealer busts, you win {bet}. Congrats!")
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print("You lost, too bad!")
            money -= bet
        elif player_value > dealer_value:
            print(f"You won {bet}! Congrats.")
            money += bet
        elif player_value == dealer_value:
            print("It is in fact a tie. Your bet is returned to you.")

        input ("Press enter to continue...")
        print("\n\n")



def get_bet(max_bet):
    #ask the player how much they'd like to bet for this round:
    
    #keep asking until they enter a valid value:
    while True:
        print(f"How much would you like to bet? (1-{max_bet}, or QUIT)")
        bet = input("> ").upper().strip()
        if bet.upper() == "QUIT":
            print(f"You go home with CHF {max_bet}.")
            print("Thank you for playing.")
            sys.exit()
        
        if not bet.isdecimal():
            continue #if the player didn't enter a number, ask again

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet 


def get_deck():
    #return a list of (rank, suit) tuples for all 52 cards
    deck = []
    for suit in (hearts, diamonds, spades, clubs):
        for rank in range(2, 11):
            deck.append((str(rank), suit))#add the numbered cards
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit)) #add the face and ace cards
    random.shuffle(deck)
    return deck

def display_hands(player_hand, dealer_hand, showDealerHand):
    #show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is false
    print()
    if showDealerHand:
        print(f"DEALER: {get_hand_value(dealer_hand)}")
        display_cards(dealer_hand)
    else:
        print("DEALER: ???")
        #Hide the dealer's first card:
        display_cards([backside] + dealer_hand[1:])

    #show the player's cards:
    print(f"PLAYER: {get_hand_value(player_hand)}")
    display_cards(player_hand)


def get_hand_value(cards):
    #Returning the value of the cards. Face cards are worth 10, aces are 
    #worth 11 or 1 (this function picks the most suitable ace value):
    value = 0
    number_of_aces = 0

    #Add the value for the non-ace cards:
    for card in cards:
        rank = card[0] #card is a tuple like (rank, suit)
        if rank == "A":
            number_of_aces += 1
        elif rank in ("K", "Q", "J"):
            value += 10
        else:
            value += int(rank) #numbered cards are worth their number

        #Now add the value for the aces:
    value += number_of_aces
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10
        
    return value

def display_cards(cards):
    #Display all the cards in the cards list:
    rows = ["", "", "", "", ""] #text to display on each row.

    for i, card in enumerate(cards):
        rows[0] += " ___ "
        if card == backside:
            #print the card's back side
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "|_##| "

        else:
            #print the card's front
            rank, suit = card #card is a tuple data structure
            rows[1] += "|{} | ".format(rank.ljust(2))
            rows[2] += "| {} | ".format(suit)
            rows[3] += "|_{}|".format(rank.rjust(2, "_"))

    #print each row on the screen:
    for row in rows:
        print(row)



def get_move(player_hand, money):
    #Asking the player ofor their move, returning "H" for hit, "S" for stand and "D" for double down
    while True: #Keep looping until the player enters a correct move.
        #Determine what moves the player can make:
        moves = ["(H)it", "(S)tand"]

        #The player can only double down on their first move, which we can tell because they'll have exactly two cards:
        if len(player_hand) == 2 and money > 0:
            moves.append("(D)ouble down")

        #Get the player's move:
        move_prompt = ", ".join(moves) + "> "
        move = input(move_prompt).upper()
        if move in ("H", "S"):
            return move #player has entered a valid move
        if move == "D" and "(D)ouble down" in moves:
            return move #Doubling down is possible and the user choses to double down
        
#If the program is run (instead of being imported), run the game:
if __name__ == "__main__":
    main()

