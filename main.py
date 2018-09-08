import nltk
import linecache
porter = nltk.PorterStemmer()
from nltk.corpus import words
from nltk.corpus import stopwords
from nltk.corpus import cmudict
from nltk.corpus import gutenberg
from nltk.corpus import brown
import random


# Find file line count
def file_line_count(file_name):
    return len(open(file_name).readlines())


# Sort words into files by part of speech
def get_part_of_speech(tagged, file_name, pos):
    word_file = open(file_name, "w")
    for pair in tagged:
        if pair[1] == pos:
            if pair[0].islower():
                word_file.write(pair[0] + '\n')
    word_file.close()


# Choose a random word from the file
def choose_random_word(file_name):
    line_count = file_line_count(file_name)
    rand_number = random.randrange(0, line_count - 1)
    word = linecache.getline(file_name, rand_number)
    return word[:len(word)-1]


# Generate a line of poetry
def get_line_poetry(nf, vf, adjf):
    line = choose_random_word(adjf).capitalize() + " " + choose_random_word(nf) + " " + choose_random_word(vf)
    return line

# Generate a poem
def get_poem(nf, vf, adjf, num_lines):
    count = 0
    while count < num_lines:
        print(get_line_poetry(nf, vf, adjf))
        count += 1


# Main Program

# Build files of sorted words
nouns_file = "noun_file.txt"
poss_nouns_file = "possessive_noun_file.txt"
plural_nouns_file = "plural_noun_file.txt"
poss_pl_nouns_file = "possessive_plural_noun_file.txt"
sing_non_third_verbs_file = "sing_non_third_verb_file.txt"
sing_third_verbs_file = "sing_third_verbs_file.txt"
adjs_file = "adj_file.txt"
brown_tagged = brown.tagged_words()
get_part_of_speech(brown_tagged, poss_nouns_file, "NN$")
get_part_of_speech(brown_tagged, plural_nouns_file, "NNS")
get_part_of_speech(brown_tagged, poss_pl_nouns_file, "NNS$")
get_part_of_speech(brown_tagged, nouns_file, "NN")
get_part_of_speech(brown_tagged, sing_non_third_verbs_file, "VBP")
get_part_of_speech(brown_tagged, sing_third_verbs_file, "VBZ")
get_part_of_speech(brown_tagged, adjs_file, "JJ")

# Write a poem
get_poem(nouns_file, sing_third_verbs_file, adjs_file, 5)