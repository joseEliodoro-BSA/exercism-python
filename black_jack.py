# Instructions
# In this exercise you are going to implement some rules of Blackjack, such as the way the game is played and scored.

# Note : In this exercise, A means ace, J means jack, Q means queen, and K means king. Jokers are discarded. A standard French-suited 52-card deck is assumed, but in most versions, several decks are shuffled together for play.

# In Blackjack, it is up to each individual player if an ace is worth 1 or 11 points (more on that later). Face cards (J, Q, K) are scored at 10 points and any other card is worth its "pip" (numerical) value.

# Define the value_of_card(<card>) function with parameter card. The function should return the numerical value of the passed-in card string. Since an ace can take on multiple values (1 or 11), this function should fix the value of an ace card at 1 for the time being. Later on, you will implement a function to determine the value of an ace card, given an existing hand.

# >>> value_of_card('K')
# 10

# >>> value_of_card('4')
# 4

# >>> value_of_card('A')
# 1

# Stuck? Reveal Hints
# Opens in a modal
# Define the higher_card(<card_one>, <card_two>) function having parameters card_one and card_two. For scoring purposes, the value of J, Q or K is 10. The function should return which card has the higher value for scoring. If both cards have an equal value, return both. Returning both cards can be done by using a comma in the return statement:

# # Using a comma in a return creates a Tuple.  Tuples will be covered in a later exercise.
# >>> def returning_two_values(value_one, value_two):
#         return value_one, value_two

# >>> returning_two_values('K', '3')
# ('K', '3')
# An ace can take on multiple values, so we will fix A cards to a value of 1 for this task.

# >>> higher_card('K', '10')
# ('K', '10')

# >>> higher_card('4', '6')
# '6'

# >>> higher_card('K', 'A')
# 'K'

# Stuck? Reveal Hints
# Opens in a modal
# As mentioned before, an ace can be worth either 1 or 11 points. Players try to get as close as possible to a score of 21, without going over 21 (going "bust").

# Define the value_of_ace(<card_one>, <card_two>) function with parameters card_one and card_two, which are a pair of cards already in the hand before getting an ace card. Your function will have to decide if the upcoming ace will get a value of 1 or a value of 11, and return that value. Remember: the value of the hand with the ace needs to be as high as possible without going over 21.

# Hint: if we already have an ace in hand, then the value for the upcoming ace would be 1.

# >>> value_of_ace('6', 'K')
# 1

# >>> value_of_ace('7', '3')
# 11

# Stuck? Reveal Hints
# Opens in a modal
# If a player is dealt an ace (A) and a ten-card (10, K, Q, or J) as their first two cards, then the player has a score of 21. This is known as a blackjack hand.

# Define the is_blackjack(<card_one>, <card_two>) function with parameters card_one and card_two, which are a pair of cards. Determine if the two-card hand is a blackjack, and return the boolean True if it is, False otherwise.

# Note : The score calculation can be done in many ways. But if possible, we'd like you to check if there is an ace and a ten-card in the hand (or at a certain position), as opposed to summing the hand values.

# >>> is_blackjack('A', 'K')
# True

# >>> is_blackjack('10', '9')
# False

# Stuck? Reveal Hints
# Opens in a modal
# If the players first two cards are of the same value, such as two sixes, or a Q and K a player may choose to treat them as two separate hands. This is known as "splitting pairs".

# Define the can_split_pairs(<card_one>, <card_two>) function with parameters card_one and card_two, which are a pair of cards. Determine if this two-card hand can be split into two pairs. If the hand can be split, return the boolean True otherwise, return False

# >>> can_split_pairs('Q', 'K')
# True

# >>> can_split_pairs('10', 'A')
# False

# Stuck? Reveal Hints
# Opens in a modal
# When the original two cards dealt total 9, 10, or 11 points, a player can place an additional bet equal to their original bet. This is known as "doubling down".

# Define the can_double_down(<card_one>, <card_two>) function with parameters card_one and card_two, which are a pair of cards. Determine if the two-card hand can be "doubled down", and return the boolean True if it can, False otherwise.

# >>> can_double_down('A', '9')
# True

# >>> can_double_down('10', '2')
# False


"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if(card.upper() in ['J', 'Q', 'K']): 
        return 10
    if(card.upper() == "A"): 
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    score_one = value_of_card(card_one)
    score_two = value_of_card(card_two)
    if(score_one > score_two): return card_one
    if(score_two > score_one): return card_two
    return (card_one, card_two)
    
    


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if(card_one == "A" or card_two == "A"): return 1
    soma = value_of_card(card_one) + value_of_card(card_two)
    if(soma > 10): return 1
    return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if(card_one == "A" and card_two in ["J", "Q", "K", "10"]):
        return True
    if(card_two == "A" and card_one in ["J", "Q", "K", "10"]):
        return True
        
    soma = value_of_card(str(card_one)) + value_of_card(str(card_two)) 
    return soma == 21



def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two) 


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    return value_of_card(card_one) + value_of_card(card_two) in [9, 10, 11]
