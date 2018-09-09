# Author: Laura Lund
# Project: Poetry-Machine
import nltk
import os.path
import random

class Poems:
    # Grammar line patterns
    line_patterns = []

    # Extract words and patterns
    def knowledge_extractor(self, file_builder_obj, sentence):
        # Tokenize and tag with parts of speech
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)

        # Save the word in a file
        file_builder_obj.build_files(tagged)

        # Save the pos pattern
        self.pattern_extractor(tagged)

    # Learn pattern of one line of input
    def pattern_extractor(self, tagged):
        pattern = ""

        # Extract the pattern
        for i in tagged:
            if str(i[1]) not in '.,!? _:;':
                if len(pattern) == 0:
                    pattern += str(i[1])
                else:
                    pattern += " " + str(i[1])


        # Check if we have this pattern
        new_pattern = True
        if len(self.line_patterns) > 0:
            for ptrn in self.line_patterns:
                if pattern == ptrn:
                    new_pattern = False
        if new_pattern:
            # Add this pattern to the list of known patterns
            self.line_patterns.append(pattern)
        print("Patterns known:")
        print(self.line_patterns)

    # Read patterns from a file
    def read_knowledge(self, file_name, file_builder_obj):
        if os.path.isfile(file_name):
            read_file = open(file_name, "r")
            for line in read_file:
                # Store the pattern of this line, but skip lines with just newline char
                if len(line) > 1:
                    self.knowledge_extractor(file_builder_obj, line)


    # Write a line using a known pattern
    def generate_line(self, file_builder_obj):
        # If it knows at least one pattern
        if len(self.line_patterns) != 0:
            # Choose a random pattern
            rand_max = len(self.line_patterns) - 1
            rand_index = random.randrange(0, rand_max)

            # Write a line
            new_line = ""
            for pos in self.line_patterns[rand_index].split():
                # Choose word
                new_word = file_builder_obj.choose_random_word(pos)
                new_line += new_word + " "
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