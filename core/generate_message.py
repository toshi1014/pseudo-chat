import glob, random, pickle


class GenerateMessage():
    def __init__(self, opponent_name_):
        self.opponent_name = opponent_name_
        self.cache_filename = glob.glob("../cache/" + self.opponent_name + "*.pickle")[0]
        self.load_cache()


    def load_cache(self):
        with open(self.cache_filename, "rb") as f:
            self.opponent_markov_chain, self.my_markov_chian = pickle.load(f)


    def word_choice(self, dict):
        return random.choice(list(dict.keys()))


    def generate_base(self, dict):
        word_out_list = []

        fst = dict["@"]         ## @ as beginning of sentence
        w1 = self.word_choice(fst)
        w2 = self.word_choice(fst[w1])

        word_out_list += [w1, w2]

        while True:
            w3 = self.word_choice(dict[w1][w2])
            word_out_list.append(w3)
            if w3 == "^":           ## if end of sentence
                break
            w1, w2 = w2, w3

        return "".join(word_out_list)

    def get_generated_message(self, sender):
        if sender == self.opponent_name:
            return self.generate_base(self.opponent_markov_chain)
        else:
            return self.generate_base(self.my_markov_chian)

