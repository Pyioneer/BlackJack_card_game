# lets create black jack game
import random
#creating a global list for card game
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

playing = True


# making a Card class where each Card object has a suit and a rank,
class card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


# a Deck class to hold all 52 Card objects, and can be shuffled
class deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "the deck has:" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


'''
try_deck=deck()
print(try_deck)
'''

#making a hand class( the Hand class may be used to calculate the value of those
# cards using the values dictionary defined above)
class hand():
    def __init__(self):
        self.cards = []  # as similar to deck class to hold the cards
        self.value = 0  # start with zero value
        self.aces = 0  # start with attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        while self.value>21 and self.aces:
            self.value -=10
            self.aces -=1

'''
#TRIAL
try_deck = deck()
try_deck.shuffle()
test_player = hand()

test_player.add_card(try_deck.deal())

print(test_player.value)
'''
#creating a chips class(In addition to decks of cards and hands, we need to
# keep track of a Player's starting chips, bets, and ongoing winnings)
#now create a chips class to get the bet
class chips():
    def __init__(self):
        self.total=100 #this is default value of chips at the start of the game
        self.bet=0 #initial noone has made for bet

    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet

#AS MANY METHODS ARE GOING TO BE REPETITIVE lets make function for them
#creating a function for taking bet from a player
def take_bet(chips):
    while True:
        try:
            chips.bet=int(input('how many chips would you like to bet ?'))
        except ValueError:
            print("sorry bet must be a integer")
        else :
            if chips.bet>chips.total:
                print("you di=ont have enough chips !!")
            else:
                break
#creating a hit function
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
#Function prompting the Player to Hit or Stand
def hit_or_stand(deck,hand):
    global playing
    while True:
        x=input("would yuo like to do hits or stand ?"
                "enter 'h' or 's' ")
        if x[0].lower()=='h':
            hit(deck, hand) #it hits the hit function
        elif x[0].lower()=='s':
            print("player stands dealer is playing")
            playing=False
        else:
            print("SORRY YOUR INPUT IS INVALID")
            continue
        break

#Write functions to display cards
#when the game starts dealer first card is hidden
def show_some(player,dealer):
    print("'\nDealer's hand")
    print("<card hidden>")
    print('',dealer.cards[1])
    #here '*' is used to print every item and "sep" is used to separate each item
    print("\n player's hand:", *player.cards, sep="\n")

#at the end of the hand all cards are shown
def show_all(player,dealer):
    print("\n dealer's hand",*dealer.cards,sep='\n')
    print("dealer's hand=",dealer.value)
    print("\n player's hand:", *player.cards, sep="\n")
    print("player's hand=", player.value)


#functions for handling the game scenarios
def player_busts(player,dealer,chips):
    print("player busts !")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print("player wins")
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print("dealer busts")
def dealer_wins(player,dealer,chips):
    print("dealer wins!!")
    chips.lose_bet()
#as a dealer nad player got 21 same time
def push(player,dealer):
    print("dealer and player tie  it is a push.")


     #HERE THE GAMES BEGINS
while True:
    print("welcome to the BLACKJACK !!")
    print("get as close as 21 as you can without going over")
    print("Dealer hits until she reaches 17.Aces count as 1 or 11")
    #creating a deck and dealing cards to each player
    deck = deck()
    deck.shuffle()

    #for players
    player_hand=hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    #for dealer
    dealer_hand = hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #give chips to players

    player_chips=chips()

    #prompt player for the bet
    take_bet(player_chips)

    #show some cards
    show_some(player_hand,dealer_hand)

    while playing:
        # prompting hit or stand
        hit_or_stand(deck,player_hand)
        #show_some :one card of dealer are hidden
        show_some(player_hand,dealer_hand)
        #as per the condition if player hand exceeds 21,
        #player busts
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    #if player is not busted ,we have to play dealer hand to make it to 17
    if player_hand.value <=21:
        while dealer_hand.value<17:
            hit(deck,dealer_hand)
        #show all cards
        show_all(player_hand,dealer_hand)
        #running different winning scnarios
        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(layer_hand,dealer_hand,player_chips)
        elif  dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print("\m players winning stand at ",player_chips.total)

    #ask to play again
    new_game=input("would you like to play another game ?")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("thanks for playing")
        break
