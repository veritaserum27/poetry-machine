# Author: Laura Lund
# Project: Poetry-Machine
# OSU Hackathon Fall 2018

import nltk
import file_build
import poem_builder


# Main Program
# These objects are used
my_files = file_build.FileBuilder()

# Extract pattern from sample poetry files
my_poem = poem_builder.Poems()
my_poem.read_knowledge('./bad_poetry/vogonesque_samples.txt', my_files)

# Write a poem
my_poem.generate_poem(my_files)

#some_words = "A wolves give a good time"
#tokens = nltk.word_tokenize(some_words)
#tagged = nltk.pos_tag(tokens)
#my_poem.check_DT_NN_agreement(tagged, 2)
