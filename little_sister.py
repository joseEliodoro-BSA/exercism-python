# Instructions
# In this exercise you are helping your younger sister edit her paper for school. The teacher is looking for correct punctuation, grammar, and excellent word choice.

# You have four tasks to clean up and modify strings.

# Any good paper needs a properly formatted title. Implement the function capitalize_title(<title>) which takes a title str as a parameter and capitalizes the first letter of each word. This function should return a str in title case.

# >>> capitalize_title("my hobbies")
# "My Hobbies"

# Stuck? Reveal Hints
# Opens in a modal
# You want to make sure that the punctuation in the paper is perfect. Implement the function check_sentence_ending() that takes sentence as a parameter. This function should return a bool.

# >>> check_sentence_ending("I like to hike, bake, and read.")
# True

# Stuck? Reveal Hints
# Opens in a modal
# To make the paper look professional, unnecessary spacing needs to be removed. Implement the function clean_up_spacing() that takes sentence as a parameter. The function should remove extra whitespace at both the beginning and the end of the sentence, returning a new, updated sentence str.

# >>> clean_up_spacing(" I like to go on hikes with my dog.  ")
# "I like to go on hikes with my dog."

# Stuck? Reveal Hints
# Opens in a modal
# To make the paper even better, you can replace some of the adjectives with their synonyms. Write the function replace_word_choice() that takes sentence, old_word, and new_word as parameters. This function should replace all instances of the old_word with the new_word, and return a new str with the updated sentence.

# >>> replace_word_choice("I bake good cakes.", "good", "amazing")
# "I bake amazing cakes."

"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """

    return title.title()


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """

    return sentence[-1] == "."


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """

    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    return sentence.replace(old_word, new_word)
