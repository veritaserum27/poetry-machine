# Author: Laura Lund
# Project: Poetry-Machine
import os
import linecache
import random

class FileBuilder:
    # Dictionary of files containing word banks for each part of speech
    # Categorized by POS tag > file name
    # Dictionary is built from text the machine reads
    file_dir = './word_files/'
    file_dictionary = {
        # 'Noun': {
        #     'sing_comm': {
        #         'file_name': file_dir + 'sc_noun.txt',
        #         'tag': 'NN'
        #     },
        #     'poss_sing_comm': {
        #         'file_name': file_dir + 'poss_sc_noun.txt',
        #         'tag': 'NN$'
        #     },
        #     'plural_comm': {
        #         'file_name': file_dir + 'plc_noun.txt',
        #         'tag': 'NNS'
        #     },
        #     'poss_plural_comm': {
        #         'file_name': file_dir + 'poss_plc_noun.txt',
        #         'tag': 'NNS$'
        #     },
        # },
        # 'Pronoun': {
        #     'pers_pro': {
        #         'file_name': file_dir + 'per_pronoun.txt',
        #         'tag': 'PRP'
        #     },
        #     'poss_pro': {
        #         'file_name': file_dir + 'poss_pronoun.txt',
        #         'tag': 'PRP$'
        #     }
        # },
        # 'Verb': {
        #     'third_person_sing_pres_verb': {
        #         'file_name': file_dir + 'tpsp_verb.txt',
        #         'tag': 'VBZ'
        #     },
        #     'not_third_person_sing_pres_verb': {
        #         'file_name': file_dir + 'not_tpsp_verb.txt',
        #         'tag': 'VBP'
        #     }
        # },
        # 'Adverb': {
        #     'adverb': {
        #         'file_name': file_dir + 'adverb.txt',
        #         'tag': 'RB'
        #     },
        #     'comp_adverb': {
        #         'file_name': file_dir + 'comp_adverb.txt',
        #         'tag': 'RBR'
        #     },
        #     'sup_adverb': {
        #         'file_name': file_dir + 'sup_adverb.txt',
        #         'tag': 'RBS'
        #     }
        # },
        # 'Adjective': {
        #     'adjective': {
        #         'file_name': file_dir + 'adjective.txt',
        #         'tag': 'JJ'
        #     },
        #     'comp_adj': {
        #         'file_name': file_dir + 'comp_adj.txt',
        #         'tag': 'JJR'
        #     },
        #     'sup_adverb': {
        #       build  'file_name': file_dir + 'sup_adj.txt',
        #         'tag': 'JJS'
        #     }
        # },
        # 'Prepositions_Sub_Conj': {
        #     'prep_sub_conj': {
        #         'file_name': file_dir + 'prep_sub_conj.txt',
        #         'tag': 'IN'
        #     }
        # },
        # 'Determiner': {
        #     'determiner': {][j]['file_name'
        #         'file_name': file_dir + 'determiner.txt',
        #         'tag': 'DT'
        #     }
        # },
        # 'To': {
        #     'to': {
        #       build  'file_name': file_dir + 'to.txt',
        #         'tag': 'TO'
        #     }
        # },
        # 'Interjection': {
        #     'inter': {
        #         'file_name': file_dir + 'interjection.txt',
        #         'tag': 'UH'
        #     }
        # },
        # 'Wh_words': {
        #     'wh_det': {
        #         'file_name': file_dir + 'wh_det.txt',
        #         'tag': 'WDT'
        #     },
        #     'wh_pro': {
        #         'file_name': file_dir + 'who_pro.txt',
        #         'tag': 'WP'
        #     },
        #     'wh_poss_pro': {
        #         'file_name': file_dir + 'wh_poss_pro.txt',
        #         'tag': 'WP$'
        #     },
        #     'wh_advb': {
        #         'file_name': file_dir + 'wh_advb.txt',
        #         'tag': 'WRB'
        #     }
        # },
        # 'Coor_conjunction': {
        #     'coor_conj': {
        #         'file_name': file_dir + 'coor_conj.txt',
        #         'tag': 'CC'
        #     }
        # }
    }

    # Updates a dictionary of items stored as POS-tag: word file pairs
    def update_dictionary(self, pos_tag):
        new_file_name = self.file_dir + pos_tag + '_file.txt'
        self.file_dictionary[pos_tag] = new_file_name

    # Adds a word not in the dictionary
    def add_word(self, pos_tag, new_word):
        # Locate the correct file for reading
        # Check if this word is in file
        # If not, open for writing
        word_file = open(self.file_dictionary[pos_tag], 'a+')
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

        # This function should really just be about adding the file if it doesn't exist
        # for pair in tagged:
        #     for key in self.file_dictionary.items():
        #         if pair[1] == key:
        #             key_found = True
        #             self.add_word(pair[1], pair[0])
        #     if key_found == False:
        #         # add key
        #         self.build_dictionary(pair[1])
        #         #Add word
        #         self.add_word(pair[1], pair[0])

    # Build files using a collection of tagged words
    def build_files(self, tagged):
        # Create directory if it doesn't exist
        if not os.path.exists(self.file_dir):
            os.makedirs(self.file_dir)

        # Go through tagged words
        for pair in tagged:
            # Get the file
            self.get_file(pair[1])

            # Add the word
            self.add_word(pair[1], pair[0])

        # Build files for all categories in the dictionary
        # for i in self.file_dictionary:
        #     self.build_file(i, tagged)


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
                    if line_count > 0:
                        # Get a random word from this file
                        rand_number = random.randrange(0, line_count - 1)
                        word = linecache.getline(self.file_dictionary[pos_tag], rand_number)
                        return word[:len(word) - 1]
                    else:
                        return 'ERROR: NO ' + pos_tag + ' WORDS STORED'
