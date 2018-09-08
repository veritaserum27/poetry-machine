# Author: Laura Lund
# Project: Poetry-Machine
import os
import linecache
import random

class FileBuilder:
    # Dictionary of files containing word banks for each part of speech
    # Categorized by general POS > specific type > file name, POS tag
    file_dir = './word_files/'
    file_dictionary = {
        'Noun': {
            'sing_comm': {
                'file_name': file_dir + 'sc_noun.txt',
                'tag': 'NN'
            },
            'poss_sing_comm': {
                'file_name': file_dir + 'poss_sc_noun.txt',
                'tag': 'NN$'
            },
            'plural_comm': {
                'file_name': file_dir + 'plc_noun.txt',
                'tag': 'NNS'
            },
            'poss_plural_comm': {
                'file_name': file_dir + 'poss_plc_noun.txt',
                'tag': 'NNS$'
            },
        },
        'Pronoun': {
            'pers_pro': {
                'file_name': file_dir + 'per_pronoun.txt',
                'tag': 'PRP'
            },
            'poss_pro': {
                'file_name': file_dir + 'poss_pronoun.txt',
                'tag': 'PRP$'
            }
        },
        'Verb': {
            'third_person_sing_pres_verb': {
                'file_name': file_dir + 'tpsp_verb.txt',
                'tag': 'VBZ'
            },
            'not_third_person_sing_pres_verb': {
                'file_name': file_dir + 'not_tpsp_verb.txt',
                'tag': 'VBP'
            }
        },
        'Adverb': {
            'adverb': {
                'file_name': file_dir + 'adverb.txt',
                'tag': 'RB'
            },
            'comp_adverb': {
                'file_name': file_dir + 'comp_adverb.txt',
                'tag': 'RBR'
            },
            'sup_adverb': {
                'file_name': file_dir + 'sup_adverb.txt',
                'tag': 'RBS'
            }
        },
        'Adjective': {
            'adjective': {
                'file_name': file_dir + 'adjective.txt',
                'tag': 'JJ'
            },
            'comp_adj': {
                'file_name': file_dir + 'comp_adj.txt',
                'tag': 'JJR'
            },
            'sup_adverb': {
                'file_name': file_dir + 'sup_adj.txt',
                'tag': 'JJS'
            }
        },
        'Prepositions_Sub_Conj': {
            'prep_sub_conj': {
                'file_name': file_dir + 'prep_sub_conj.txt',
                'tag': 'IN'
            }
        },
        'Determiner': {
            'determiner': {
                'file_name': file_dir + 'determiner.txt',
                'tag': 'DT'
            }
        },
        'To': {
            'to': {
                'file_name': file_dir + 'to.txt',
                'tag': 'TO'
            }
        },
        'Interjection': {
            'inter': {
                'file_name': file_dir + 'interjection.txt',
                'tag': 'UH'
            }
        },
        'Wh_words': {
            'wh_det': {
                'file_name': file_dir + 'wh_det.txt',
                'tag': 'WDT'
            },
            'wh_pro': {
                'file_name': file_dir + 'who_pro.txt',
                'tag': 'WP'
            },
            'wh_poss_pro': {
                'file_name': file_dir + 'wh_poss_pro.txt',
                'tag': 'WP$'
            },
            'wh_advb': {
                'file_name': file_dir + 'wh_advb.txt',
                'tag': 'WRB'
            }
        },
        'Coor_conjunction': {
            'coor_conj': {
                'file_name': file_dir + 'coor_conj.txt',
                'tag': 'CC'
            }
        }
    }

    # Builds individual files in each part of speech category
    def build_file(self, pos_category, tagged):
        # Locate the file t hat matches pos tag
        for i in self.file_dictionary[pos_category]:
            word_file = open(self.file_dictionary[pos_category][i]['file_name'], 'w')
            for pair in tagged:
                if pair[1] == self.file_dictionary[pos_category][i]['tag']:
                    # Only save common
                    if pair[0].islower():
                        # This allows for duplicates, may change in future version
                        word_file.write(pair[0] + '\n')
            word_file.close()

    def build_files(self, tagged):
        # Create directory if it doesn't exist
        if not os.path.exists(self.file_dir):
            os.makedirs(self.file_dir)

        # Build files for all categories in the dictionary
        for i in self.file_dictionary:
            self.build_file(i, tagged)


    # Find file line count
    def file_line_count(self, fn):
        return len(open(fn).readlines())


    # Choose a random word from the file for specified part of speech
    def choose_random_word(self, pos):
        # Locate the correct file
        for i in self.file_dictionary:
            for j in self.file_dictionary[i]:
                if self.file_dictionary[i][j]['tag'] == pos:
                    # Make sure there is content in this file
                    line_count = self.file_line_count(self.file_dictionary[i][j]['file_name'])
                    if line_count > 0:
                        # Get a random word from this file
                        rand_number = random.randrange(0, line_count - 1)
                        word = linecache.getline(self.file_dictionary[i][j]['file_name'], rand_number)
                        return word[:len(word) - 1]
                    else:
                        return 'ERROR: NO ' + pos + ' WORDS STORED'
