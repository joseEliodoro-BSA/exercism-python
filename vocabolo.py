# Instructions
# You are helping your younger sister with her English vocabulary homework, which she is finding very tedious. Her class is learning to create new words by adding prefixes and suffixes. Given a set of words, the teacher is looking for correctly transformed words with correct spelling by adding the prefix to the beginning or the suffix to the ending.

# The assignment has four activities, each with a set of text or words to work with.

# One of the most common prefixes in English is un, meaning "not". In this activity, your sister needs to make negative, or "not" words by adding un to them.

# Implement the add_prefix_un(<word>) function that takes word as a parameter and returns a new un prefixed word:

# >>> add_prefix_un("happy")
# 'unhappy'

# >>> add_prefix_un("manageable")
# 'unmanageable'

# Stuck? Reveal Hints
# Opens in a modal
# There are four more common prefixes that your sister's class is studying: en (meaning to 'put into' or 'cover with'), pre (meaning 'before' or 'forward'), auto (meaning 'self' or 'same'), and inter (meaning 'between' or 'among').

# In this exercise, the class is creating groups of vocabulary words using these prefixes, so they can be studied together. Each prefix comes in a list with common words it's used with. The students need to apply the prefix and produce a string that shows the prefix applied to all of the words.

# Implement the make_word_groups(<vocab_words>) function that takes a vocab_words as a parameter in the following form: [<prefix>, <word_1>, <word_2> .... <word_n>], and returns a string with the prefix applied to each word that looks like: '<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'.

# Creating a for or while loop to process the input is not needed here. Think carefully about which string methods (and delimiters) you could use instead.

# >>> make_word_groups(['en', 'close', 'joy', 'lighten'])
# 'en :: enclose :: enjoy :: enlighten'

# >>> make_word_groups(['pre', 'serve', 'dispose', 'position'])
# 'pre :: preserve :: predispose :: preposition'

# >> make_word_groups(['auto', 'didactic', 'graph', 'mate'])
# 'auto :: autodidactic :: autograph :: automate'

# >>> make_word_groups(['inter', 'twine', 'connected', 'dependent'])
# 'inter :: intertwine :: interconnected :: interdependent'

# Stuck? Reveal Hints
# Opens in a modal
# ness is a common suffix that means 'state of being'. In this activity, your sister needs to find the original root word by removing the ness suffix. But of course there are pesky spelling rules: If the root word originally ended in a consonant followed by a 'y', then the 'y' was changed to 'i'. Removing 'ness' needs to restore the 'y' in those root words. e.g. happiness --> happi --> happy.

# Implement the remove_suffix_ness(<word>) function that takes in a word, and returns the root word without the ness suffix.

# >>> remove_suffix_ness("heaviness")
# 'heavy'

# >>> remove_suffix_ness("sadness")
# 'sad'

# Stuck? Reveal Hints
# Opens in a modal
# Suffixes are often used to change the part of speech a word is assigned to. A common practice in English is "verbing" or "verbifying" -- where an adjective becomes a verb by adding an en suffix.

# In this task, your sister is going to practice "verbing" words by extracting an adjective from a sentence and turning it into a verb. Fortunately, all the words that need to be transformed here are "regular" - they don't need spelling changes to add the suffix.

# Implement the adjective_to_verb(<sentence>, <index>) function that takes two parameters. A sentence using the vocabulary word, and the index of the word, once that sentence is split apart. The function should return the extracted adjective as a verb.

# >>> adjective_to_verb('I need to make that bright.', -1 )
# 'brighten'

# >>> adjective_to_verb('It got dark as the sun set.', 2)
# 'darken'

"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return f"un{word}"


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    list_with_prefix = [ vocab_words[0]+prefix for prefix in vocab_words[1:] ]
    return " :: ".join([vocab_words[0]] + list_with_prefix) 


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    new_word = word.replace('ness', "")
    if(new_word[-1] == "i"): 
        return new_word[:len(new_word)-1]+ "y"
    return new_word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    verb = sentence[:-1].split(' ')[index]
    return verb+"en"
