# Author: Laura Lund
# Project: Poetry-Machine

import nltk
import file_build
import poem_builder
import linecache
from nltk.tokenize import word_tokenize
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
def get_line_poetry(nf, vf, adjf, advbf):
    line = choose_random_word(adjf).capitalize() + " " + choose_random_word(nf) + " " + choose_random_word(vf) + " " + choose_random_word(advbf)
    return line

# Generate a poem
def get_poem(nf, vf, adjf, advbf, num_lines):
    count = 0
    while count < num_lines:
        print(get_line_poetry(nf, vf, adjf, advbf))
        count += 1


# Main Program
# Words from corpora
#brown_tagged = brown.tagged_words()
#gutenberg_words = gutenberg.words()
#gutenberg_tagged = nltk.pos_tag(gutenberg_words)

# Build files of sorted words
my_files = file_build.FileBuilder()
#my_files.build_files(brown_tagged)
#my_files.build_files(gutenberg_tagged)
print(my_files.file_dictionary['Noun']['sing_comm']['file_name'])
print(my_files.file_dictionary['Noun']['sing_comm']['tag'])
print()
print("Choosing random common noun:")
print(my_files.choose_random_word('NN'))

# Extract pattern from sample line
my_poem_pattern = poem_builder.Poems()

line0 = """The yellow sun is really bright"""
my_poem_pattern.pattern_extractor(line0)
print("After extraction: " + str(my_poem_pattern.line_patterns))
line1 = """Very merry people run fast"""
my_poem_pattern.pattern_extractor(line1)
print("After extraction: " + str(my_poem_pattern.line_patterns))
print()
print("Generated line 0: ")
print(my_poem_pattern.generate_line(0, my_files))
print()
print("Generated line 1: ")
print(my_poem_pattern.generate_line(1, my_files))



# Write a poem
#get_poem(my_files.scn_file, my_files.st_verbs_file, my_files.adjs_file, my_files.advbs_file, 5)
