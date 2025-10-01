# Instructions
# Elyse is really looking forward to playing some poker (and other card games) during her upcoming trip to Vegas. Being a big fan of "self-tracking" she wants to put together some small functions that will help her with tracking tasks and has asked for your help thinking them through.

# Elyse is especially fond of poker, and wants to track how many rounds she plays - and which rounds those are. Every round has its own number, and every table shows the round number currently being played. Elyse chooses a table and sits down to play her first round. She plans on playing three rounds.

# Implement a function get_rounds(<round_number>) that takes the current round number and returns a single list with that round and the next two that are coming up:

# >>> get_rounds(27)
# [27, 28, 29]

# Stuck? Reveal Hints
# Opens in a modal
# Elyse played a few rounds at the first table, then took a break and played some more rounds at a second table ... but ended up with a different list for each table! She wants to put the two lists together, so she can track all of the poker rounds in the same place.

# Implement a function concatenate_rounds(<rounds_1>, <rounds_2>) that takes two lists and returns a single list consisting of all the rounds in the first list, followed by all the rounds in the second list:

# >>> concatenate_rounds([27, 28, 29], [35, 36])
# [27, 28, 29, 35, 36]

# Stuck? Reveal Hints
# Opens in a modal
# Talking about some of the prior Poker rounds, another player remarks how similarly two of them played out. Elyse is not sure if she played those rounds or not.

# Implement a function list_contains_round(<rounds>, <round_number>) that takes two arguments, a list of rounds played and a round number. The function will return True if the round is in the list of rounds played, False if not:

# >>> list_contains_round([27, 28, 29, 35, 36], 29)
# True

# >>> list_contains_round([27, 28, 29, 35, 36], 30)
# False

# Stuck? Reveal Hints
# Opens in a modal
# Elyse wants to try out a new game called Black Joe. It's similar to Black Jack - where your goal is to have the cards in your hand add up to a target value - but in Black Joe the goal is to get the average of the card values to be 7. The average can be found by summing up all the card values and then dividing that sum by the number of cards in the hand.

# Implement a function card_average(<hand>) that will return the average value of a hand of Black Joe.

# >>> card_average([5, 6, 7])
# 6.0

# Stuck? Reveal Hints
# Opens in a modal
# In Black Joe, speed is important. Elyse is going to try and find a faster way of finding the average.

# She has thought of two ways of getting an average-like number:

# Take the average of the first and last number in the hand.
# Using the median (middle card) of the hand.
# Implement the function approx_average_is_average(<hand>), given hand, a list containing the values of the cards in your hand.

# Return True if either one or both of the, above named, strategies result in a number equal to the actual average.

# Note: The length of all hands are odd, to make finding a median easier.

# >>> approx_average_is_average([1, 2, 3])
# True

# >>> approx_average_is_average([2, 3, 4, 8, 8])
# True

# >>> approx_average_is_average([1, 2, 3, 5, 9])
# False

# Stuck? Reveal Hints
# Opens in a modal
# Intrigued by the results of her averaging experiment, Elyse is wondering if taking the average of the cards at the even positions versus the average of the cards at the odd positions would give the same results. Time for another test function!

# Implement a function average_even_is_average_odd(<hand>) that returns a Boolean indicating if the average of the cards at even indexes is the same as the average of the cards at odd indexes.

# >>> average_even_is_average_odd([1, 2, 3])
# True

# >>> average_even_is_average_odd([1, 2, 3, 4])
# False

# Stuck? Reveal Hints
# Opens in a modal
# Every 11th hand in Black Joe is a bonus hand with a bonus rule: if the last card you draw is a Jack, you double its value.

# Implement a function maybe_double_last(<hand>) that takes a hand and checks if the last card is a Jack (11). If the last card is a Jack (11), double its value before returning the hand.

# >>> hand = [5, 9, 11]
# >>> maybe_double_last(hand)
# [5, 9, 22]

# >>> hand = [5, 9, 10]
# >>> maybe_double_last(hand)
# [5, 9, 10]

"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return list(range(number, number+3))


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    media = (hand[0] + hand[-1])/2
    media_approx = sum(hand)/len(hand)
    media_real = hand[len(hand)//2]
    return (media_real==media) or (media_approx==media) or (media_real == media_approx)


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    media = sum(hand)/len(hand)
    return media in hand


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if(hand[-1] == 11): 
        return hand[:-1]+[hand[-1]*2]
    return hand
