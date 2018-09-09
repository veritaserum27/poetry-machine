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
print("I just read some bad poetry. Here's a new poem: \n")
my_poem.generate_poem(my_files)

# Read good poetry
