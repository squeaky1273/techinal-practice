# Given a phrase, count the occurrences of 
# each word in that phrase.

# good inputs = ['he does not like cherries, but he likes grapes'], ['I like this and I like that']
# bad inputs = [1234], [3456]
# edge cases = ['I don't like that.'], ['Ha ha ha!]

# pseudocode:
# function name(string):
    # Have a diction of words
    # Split them so they don't end up as separate letters

    # for loop to go through str
        # if thw word is in the dictionary,
            # add a plus 1 to increse the count
        # else
            # equal the count to 1
    # return the words in the dictionary

def counter(str):
    count = dict()
    words = str.split()

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

# good:
print(counter("he does not like cherries, but he does like grapes"))
print(counter("I like this and I like that"))

# edge:
print(counter("I don't like that."))
print(counter("Ha ha ha!"))

# bad:
print(counter(1234))
print(counter(3456))


