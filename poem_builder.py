# Author: Laura Lund
# Project: Poetry-Machine
import nltk
import os.path

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
        print("Just added pattern: " + pattern)
        self.line_patterns.append(pattern)


    #  Choose a word of the selected part of speech


    # Write a line using a known pattern at the specified index
    def generate_line(self, pattern_index, file_builder_obj):
        # If it knows at least one pattern
        if len(self.line_patterns) != 0:
            # Tokenize this pattern
            tokens = nltk.word_tokenize(self.line_patterns[pattern_index])

            # Write a line
            new_line = ""
            for pos in tokens:
                # Convert to string
                i = str(pos)

                # Choose word
                new_word = file_builder_obj.choose_random_word(pos)
                new_line += new_word + " "
            return new_line
        else:
            print("Error: No line patterns known.")

    # Read patterns from a file
    def read_pattern(self, file_name):
        if os.path.isfile(file_name):
            read_file = open(file_name, "r")
            for line in read_file:
                print("Just read: " + line)
                # Store the pattern of this line
                self.pattern_extractor(line)



    # Poem Builder: uses patterns, arg is a FileBuilder object?

    # Learn patterns/update patterns