# Author: Laura Lund
# Project: Poetry-Machine
import nltk
import os.path
import random

class Poems:
    # Grammar line patterns
    line_patterns = []

    # Learn pattern of one line of input
    def pattern_extractor(self, sentence):
        # Tokenize and tag with parts of speech
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        pattern = ""

        # Extract the pattern
        for i in tagged:
            if len(pattern) == 0:
                pattern += str(i[1])
            else:
                pattern += " " + str(i[1])

        # Add this pattern to the list of known patterns
        self.line_patterns.append(pattern)

    # Read patterns from a file
    def read_pattern(self, file_name):
        if os.path.isfile(file_name):
            read_file = open(file_name, "r")
            for line in read_file:
                # Store the pattern of this line
                self.pattern_extractor(line)


    # Write a line using a known pattern
    def generate_line(self, file_builder_obj):
        # If it knows at least one pattern
        if len(self.line_patterns) != 0:
            # Choose a random pattern
            rand_max = len(self.line_patterns) - 1
            rand_index = random.randrange(0, rand_max)

            # Tokenize this pattern
            tokens = nltk.word_tokenize(self.line_patterns[rand_index])

            # Write a line
            new_line = ""
            bad_pos = ""
            for pos in tokens:
                # Convert to string
                i = str(pos)

                # Choose word
                new_word = file_builder_obj.choose_random_word(pos)
                new_line += new_word + " "
                #print("line so far: " + new_line + ", added: " + i)
            if new_line == "":
                new_line = "EMPTY LINE"
            return new_line
        else:
            print("Error: No line patterns known.")

    # Write a poem
    def generate_poem(self, file_builder_obj):
        # Random number of lines
        rand_lines = random.randrange(2, 14)
        count = 0
        while count < rand_lines:
            print(self.generate_line(file_builder_obj))
            count += 1


    # Poem Builder: uses patterns, arg is a FileBuilder object?

    # Learn patterns/update patterns