from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    word_list = list()
    with open(DICTIONARY, 'r') as f:
        for line in f.readlines():
        	word_list.append(line.strip())
    return word_list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum( [ LETTER_SCORES[c] for c in word.upper() if c in LETTER_SCORES ] )

def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if word_list is None:
        word_list = load_words()
    m=0
    mw=None
    for w in word_list:
        tm = calc_word_value(w)
        if tm > m:
            m = tm
            mw = w
    return mw

if __name__ == "__main__":
    pass # run unittests to validate
