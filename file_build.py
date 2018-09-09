# Author: Laura Lund
# Project: Poetry-Machine
# OSU Hackathon Fall 2018

import os
import linecache
import random

class FileBuilder:
    # Dictionary of files containing word banks for each part of speech
    # Categorized by POS tag > file name
    # Dictionary is built from text the machine reads
    file_dir = './word_files/'
    file_dictionary = {

    }

    # Updates a dictionary of items stored as POS-tag: word file pairs
    def update_dictionary(self, pos_tag):
        new_file_name = self.file_dir + pos_tag + '_file.txt'
        self.file_dictionary[pos_tag] = new_file_name

        # If the file doesn't exist, create it
        if not os.path.exists(new_file_name):
            new_file = open(new_file_name, 'w')
            new_file.close()

    # Adds a word not in the dictionary
    def add_word(self, pos_tag, new_word):
        found_word = False

        # Locate the correct file for reading
        # If file not empty, check its contents
        if self.file_line_count(self.file_dictionary[pos_tag]) != 0:
            read_file = open(self.file_dictionary[pos_tag], 'r')

            # Check if this word is in file
            for line in read_file:
                if new_word in line:
                    found_word = True
                    continue
            read_file.close()

        # If word not found, open file for writing
        if not found_word:
            word_file = open(self.file_dictionary[pos_tag], 'a')
            word_file.write(new_word + '\n')
            word_file.close()


    def has_key(self, key):
        for k in self.file_dictionary.items():
            if key == k:
                return True
        else:
            return False


    # Gets individual files that correspond to each part of speech category
    def get_file(self, pos_tag):
        # Locate the file that matches pos tag
        # Search existing keys
        if self.has_key(pos_tag):
            return self.file_dictionary[pos_tag]
        # Add key if not found
        self.update_dictionary(pos_tag)
        return self.file_dictionary[pos_tag]


    # Build files using a collection of tagged words
    def build_files(self, tagged):
        # Create directory if it doesn't exist
        if not os.path.exists(self.file_dir):
            os.makedirs(self.file_dir)

        # Go through tagged words
        for pair in tagged:
            # Get the file
            # Add the key if it doesn't have these symbols
            if pair[1] not in '.,!? _:;':
                self.get_file(pair[1])

            # Add the word if it doesn't have these symbols
            if pair[0] not in '.,!? _:;':
                word = pair[0]
                # lowercase if not a proper noun
                if word[0].isupper():
                    if 'NNP' not in pair[1]:
                        word = word.lower()
                self.add_word(pair[1], word)


    # Find file line count
    def file_line_count(self, file_name):
        return len(open(file_name).readlines())


    # Choose a random word from the file for specified part of speech
    def choose_random_word(self, pos_tag):
        # Locate the correct file
        for key in self.file_dictionary.keys():
            if key == pos_tag:
                    # Make sure there is content in this file
                    line_count = self.file_line_count(self.file_dictionary[pos_tag])
                    if line_count > 1:
                        # Get a random word from this file
                        rand_number = random.randrange(1, line_count)
                        word = linecache.getline(self.file_dictionary[pos_tag], rand_number)
                        return word[:len(word) - 1]
                    elif line_count == 1:
                        word = linecache.getline(self.file_dictionary[pos_tag], 1)
                        return word[:len(word) - 1]
                    else:
                        return 'ERROR: NO ' + pos_tag + ' WORDS STORED'
