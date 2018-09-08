class FileBuilder:
    # Singular common nouns
    scn_file = "sc_noun_file.txt"
    scn_tag = "NN"

    # Singular possessive nouns
    sp_nouns_file = "sp_noun_file.txt"
    spn_tag = "NN$"

    # Plural common nouns
    pl_nouns_file = "pl_noun_file.txt"
    pln_tag = "NNS"

    # Possessive plural nouns
    ppl_nouns_file = "ppl_noun_file.txt"
    ppln_tag = "NNS$"

    # Singular verbs, not third person
    snt_verbs_file = "snt_verb_file.txt"
    sntv_tag = "VBP"

    # Singular third person verbs
    st_verbs_file = "st_verbs_file.txt"
    stv_tag = "VBZ"

    # Common adjectives
    adjs_file = "adj_file.txt"
    adj_tag = "JJ"

    def build_file(self, file_name, pos, tagged):
        word_file = open(file_name, "w")
        for pair in tagged:
            if pair[1] == pos:
                if pair[0].islower():
                    word_file.write(pair[0] + '\n')
        word_file.close()

    def build_files(self, tagged):
        self.build_file(self.scn_file, self.scn_tag, tagged)
        self.build_file(self.sp_nouns_file, self.spn_tag, tagged)
        self.build_file(self.pl_nouns_file, self.pln_tag, tagged)
        self.build_file(self.ppl_nouns_file, self.ppln_tag, tagged)
        self.build_file(self.snt_verbs_file, self.sntv_tag, tagged)
        self.build_file(self.st_verbs_file, self.stv_tag, tagged)
        self.build_file(self.adjs_file, self.adj_tag, tagged)
