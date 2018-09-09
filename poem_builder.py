# Author: Laura Lund
# Project: Poetry-Machine
# OSU Hackathon Fall 2018

import nltk
import os.path
import random

class Poems:
    # Grammar, line patterns
    grammar = ""
    line_patterns = []
    pattern_dictionary = {

    }

    # Add new pattern to dictionary
    def add_pattern_dictionary(self, pattern):
        self.pattern_dictionary[pattern] = 1
        #print("Added pattern '" + pattern + "' with count: " + str(self.pattern_dictionary[pattern]))


    # Update pattern frequency count in dictionary
    def update_pattern_dictionary(self, pattern):
        self.pattern_dictionary[pattern] += 1
        #print("New count for pattern '" + pattern + "': " + str(self.pattern_dictionary[pattern]))

    # Extract words and patterns
    def knowledge_extractor(self, file_builder_obj, sentence):
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
                    # Update count in dictionary
                    self.update_pattern_dictionary(pattern)
        if new_pattern:
            # Add this pattern to the list of known patterns
            self.line_patterns.append(pattern)
            self.add_pattern_dictionary(pattern)


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
            index = 0
            split_pattern = self.line_patterns[rand_index].split()
            for pos in split_pattern:
                # Check for det, noun agreement
                if 'DT' in pos:
                    # Find its noun
                    itr = index + 1
                    found = False
                    while itr < len(split_pattern) and not found:
                        #print(pos, split_pattern[itr])
                        if 'NN' in split_pattern[itr]:
                            found = True
                            # If this is a singular noun
                            if 'NNS' == split_pattern[itr]:
                                pos = 'DT'
                            elif split_pattern[itr] == 'NN':
                                # Make DT singular
                                pos = 'DT_Sing'
                        #print(pos, split_pattern[itr])
                        itr += 1
                index += 1

                #print("Choosing a " + pos)
                # Choose word
                new_word = file_builder_obj.choose_random_word(pos)
                new_line += new_word + " "

            new_line = new_line.capitalize()
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


