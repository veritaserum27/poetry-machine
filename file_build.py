# Author: Laura Lund
# Project: Poetry-Machine
import os


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
        }
    }

    # # Singular common nouns
    # scn_file = "sc_noun_file.txt"
    # scn_tag = "NN"            if self.file_dictionary[pos_category][i]['tag'] == pos:
    #
    # # Singular possessive nouns
    # sp_nouns_file = "sp_noun_file.txt"
    # spn_tag = "NN$"
    #
    # # Plural common nouns
    # pl_nouns_file = "pl_noun_file.txt"
    # pln_tag = "NNS"
    #
    # # Possessive plural nouns
    # ppl_nouns_file = "ppl_noun_file.txt"
    # ppln_tag = "NNS$"

    # Singular verbs, not third person
    snt_verbs_file = "snt_verb_file.txt"
    sntv_tag = "VBP"

    # Singular third person verbs
    st_verbs_file = "st_verbs_file.txt"
    stv_tag = "VBZ"

    # Common adjectives
    adjs_file = "adj_file.txt"
    adj_tag = "JJ"

    # Comparative adjectives
    comp_adjs_file = "comp_adj_file.txt"
    compadj_tag = "JJR"

    # Superlative adjectives
    sup_adjs_file = "sup_adj_file.txt"
    supadj_tag = "JJS"

    # Common adverbs
    advbs_file = "advb_file.txt"
    adv_tag = "RB"

    # Comparative adverbs
    comp_advb_file = "comp_advb_file.txt"
    compadvb_tag = "RBR"

    # Superlative adverbs
    sup_advb_file = "sup_advb_file.txt"
    supadvb_tag = "RBS"

    def build_file(self, pos_category, tagged):
        # Locate the file that matches pos tag
        for i in self.file_dictionary[pos_category]:
            word_file = open(self.file_dictionary[pos_category][i]['file_name'], 'w')
            for pair in tagged:
                if pair[1] == self.file_dictionary[pos_category][i]['tag']:
                    if pair[0].islower():
                        word_file.write(pair[0] + '\n')
            word_file.close()

    def build_files(self, tagged):
        # Create directory if it doesn't exist
        if not os.path.exists(self.file_dir):
            os.makedirs(self.file_dir)

        self.build_file('Noun', tagged)

        # self.build_file(self.snt_verbs_file, self.sntv_tag, tagged)
        # self.build_file(self.st_verbs_file, self.stv_tag, tagged)
        # self.build_file(self.adjs_file, self.adj_tag, tagged)
        # self.build_file(self.comp_adjs_file, self.compadj_tag, tagged)
        # self.build_file(self.sup_adjs_file, self.supadj_tag, tagged)
        # self.build_file(self.advbs_file, self.adj_tag, tagged)
        # self.build_file(self.comp_advb_file, self.compadvb_tag, tagged)
        # self.build_file(self.sup_advb_file, self.supadvb_tag, tagged)


    # Find file line count
    def file_line_count(self, fn):
        return len(open(fn).readlines())


    # Choose a random word from the file for specified part of speech
    # def choose_random_word(self, pos):
    #     line_count = file_line_count(file_name)
    #     rand_number = random.randrange(0, line_count - 1)
    #     word = linecache.getline(file_name, rand_number)
    #     return word[:len(word) - 1]