# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = "Score: 0";
result = '';
msg1_cl = 'Black'
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print
            "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)

    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0],
                    CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE,
                          [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.card_list = []

    def __str__(self):
        s = 'Hand contains: '
        for x in self.card_list:
            s += str(x) + ' '
        return s.rstrip()

    def add_card(self, card):
        self.card_list.append(card)

    def get_value(self):
        v = 0;
        f = False
        for x in self.card_list:
            if x.get_rank() != 'A':
                v += VALUES[x.get_rank()]
            else:
                v += 1;
                f = True
        if not (v + 10 > 21) and f is True:
            v += 10
        return v

    def draw(self, canvas, pos):
        for c in self.card_list:
            c.draw(canvas, pos)
            pos[0] += CARD_SIZE[0]


# define deck class
class Deck:
    def __init__(self):
        self.deck_list = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck_list.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck_list)

    def deal_card(self):
        return self.deck_list.pop()

    def __str__(self):
        s = 'Deck contains: '
        for x in self.deck_list:
            s += str(x) + ' '
        return s.rstrip()


# define event handlers for buttons
def deal():
    global outcome, in_play, score, msg0, msg1, result
    global game_deck, player, dealer

    if in_play:
        in_play = False;
        score -= 1;
        outcome = 'Score: ' + str(score)
        result = 'You have busted!';
        msg1_cl = 'Yellow'
    else:
        game_deck = Deck();
        game_deck.shuffle();
        player = Hand();
        dealer = Hand()
        player.add_card(game_deck.deal_card());
        player.add_card(game_deck.deal_card())
        dealer.add_card(game_deck.deal_card());
        dealer.add_card(game_deck.deal_card())
        in_play = True;
        msg0 = 'Hit or stand?';
        msg1 = '';
        result = ''
    # print 'Player: ' + str(player)
    # print 'Dealer: ' + str(dealer)


def hit():
    global outcome, in_play, score, msg1, result, msg1_cl
    global game_deck, player, dealer

    if in_play:
        if player.get_value() <= 21:
            player.add_card(game_deck.deal_card())
            msg1 = 'New deal?';
            msg1_cl = 'Black'
        else:
            in_play = False;
            score -= 1;
            outcome = 'Score: ' + str(score)
            result = 'You have busted!';
            msg1_cl = 'Yellow'


def stand():
    global outcome, in_play, score, result, msg1_cl
    global game_deck, player, dealer

    if player.get_value() > 21:
        hit()
        # print 'You have already busted.'; msg1_cl = 'Yellow'

    elif in_play:
        while dealer.get_value() < 17:
            dealer.add_card(game_deck.deal_card())

        if dealer.get_value() > 21:
            in_play = False;
            score += 1;
            outcome = 'Score: ' + str(score)
            result = 'Dealer has busted.';
            msg1_cl = 'Yellow'
        else:
            if player.get_value() < dealer.get_value():
                in_play = False;
                score -= 1;
                outcome = 'Score: ' + str(score)
                result = 'You lose! Dealer has greater number.';
                msg1_cl = 'Yellow'
            elif player.get_value() == dealer.get_value():
                in_play = False;
                score -= 1;
                outcome = 'Score: ' + str(score)
                result = 'You lose! Dealer wins ties :)';
                msg1_cl = 'Yellow'
            else:
                in_play = False;
                score += 1;
                outcome = 'Score: ' + str(score)
                result = 'You have won! Dealer has smaller number.';
                msg1_cl = 'Yellow'


# draw handler
def draw(canvas):
    global player, dealer, in_play, outcome, msg0, msg1, result, msg1_cl

    canvas.draw_text('Blackjack', [20, 50], 35, 'Black', 'sans-serif')
    canvas.draw_text(outcome, [480, 50], 25, 'Black', 'sans-serif')
    canvas.draw_text(result, [200 - len(result) * 3, 290], 35 - len(result) / 2.6, 'Red', 'monospace')

    msg0_cl = 'Yellow'
    if msg1_cl == 'Yellow' and not in_play: msg0_cl = 'Black'
    canvas.draw_text(msg0, [100, 380], 20, msg0_cl, 'sans-serif')
    canvas.draw_text(msg1, [340, 380], 20, msg1_cl, 'sans-serif')

    player.draw(canvas, [100, 400])
    if in_play:
        f = True
        pos = [100, 100]
        for c in dealer.card_list:
            if f:
                c.draw_back(canvas, pos);
                f = False
            else:
                c.draw(canvas, pos)
            pos[0] += CARD_SIZE[0]
    else:
        dealer.draw(canvas, [100, 100])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
