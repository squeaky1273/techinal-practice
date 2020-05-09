# An anagram is a rearrangement of letters to form a new word. 
# Given a word and a list of candidates, select the sublist of 
# anagrams of the given word.

# good inputs: a = [listen, uns], b = ['olep', 'urn']
# bad inputs: a = [1, 5, 10, 25], b = [10, 11, 12, 13]
# edge cases: a = ['listen', 'google'], b = ['oogle', 'oocl']

# pseudocode:
# function init():
    # create empty dictionary
# function create dict():
    # populate dictionary with a word list
# function anagram():
    # for loop with if there are words
        #if statement: if inputs are in the dictioary
            # unscramble them to match sictionary words
 
class Anagram(object):
    def __init__(self):
        self.dict = self.build_dict()

    def build_dict(self):
        """"Build a dictionary to hold all of the words/letters"""
        dic = {}
        word_list = open("/usr/share/dict/words", "r").readlines()
        for word in word_list:
            word = word.strip().lower()
            words = ''.join(sorted(word))
            dic[words] = word
        return dic

    def unscramble(self, words):
        """Build a function to unscramble the letters"""
        for word in words:
            word_sorted = ''.join(sorted(word))
            if word_sorted in self.dict:
                print(self.dict[word_sorted])

if __name__ == '__main__':
# good:
    words = ['listen', 'uns']
    jumble = Anagram()
    jumble.unscramble(words)

    words = ['olep', 'urn']
    jumble = Anagram()
    jumble.unscramble(words)

# edge:
    words = ['listen', 'google']
    jumble = Anagram()
    jumble.unscramble(words)

    words = ['oogle', 'oocl']
    jumble = Anagram()
    jumble.unscramble(words)

# bad:
    words = [10, 11, 12, 13]
    jumble = Anagram()
    jumble.unscramble(words)

    words = [1, 5, 10, 25]
    jumble = Anagram()
    jumble.unscramble(words)