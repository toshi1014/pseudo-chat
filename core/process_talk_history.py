import re, glob, os, pickle
import pandas as pd
from numpy import nan as NA
from meta_characters import *
from janome.tokenizer import Tokenizer


class ProcessTalkHistory():
    def __init__(self, filepath_):
        self.filepath = filepath_
        if not self.is_cached():
            # self.make_df()
            # self.get_message_list()
            pass
        self.make_df()      # TEMP:
        self.get_message_list()
        self.run()


    def is_cached(self):
        with open(self.filepath, "r", encoding="UTF-8") as f:
            row1, row2 = f.readlines()[:2]

        self.opponent_name = row1.strip(HEADER_PREFIX).strip(HEADER_SUFFIX)
        saved_date = re.sub("\\D", "", row2)         ## remove un-number => saved_date == yyyymmdd

        self.cache_filename = "../cache/" + self.opponent_name + "_" + saved_date + ".pickle"
        return os.path.exists(self.cache_filename)


    def remove_non_string(self, message):
        if message in [STAMP_EMOTICON, IMAGE, VIDEO]:
            return NA
        return message

    def make_df(self):
        with open(self.filepath, "r", encoding="UTF-8") as f:
            data = f.read()

        date_list = []
        time_list = []
        name_list = []
        message_list = []

        for datum in data.split("\n\n")[1:]:          ## [1:] remove header
            if datum == "":
                continue

            line_list = datum.split("\n")
            if line_list[0] != "":
                date = line_list[0]

            for line in line_list[1:]:              ## [1:] remove date
                try:
                    time, name, message = line.split("\t")
                except:
                    continue

                date_list.append(date)
                time_list.append(time)
                name_list.append(name)

                message_list.append(self.remove_non_string(message))

        data_dict = {
            "date": date_list, "time": time_list,
            "name": name_list, "message": message_list,
        }

        self.df = pd.DataFrame(data_dict, columns=data_dict.keys())

        self.df.to_csv(self.cache_filename[:-7] + ".csv")        # DEBUG:


    def get_message_list(self):
        df = self.df.dropna()

        self.opponent_message_list = []
        self.my_message_list = []

        for name, message in zip(df["name"], df["message"]):
            if name == self.opponent_name:
                self.opponent_message_list.append(message + "^")        ## ^ as end of sentence
            else:
                self.my_message_list.append(message + "^")              ## ^ as end of sentence


    def add_word_chain(self, tmp_list):
        w1, w2, w3 = tmp_list
        if not w1 in self.dict:
            self.dict[w1] = {}
        if not w2 in self.dict[w1]:
            self.dict[w1][w2] = {}
        if not w3 in self.dict[w1][w2]:
            self.dict[w1][w2][w3] = 0
        self.dict[w1][w2][w3] += 1


    def make_markov_chain(self, message_list):
        t = Tokenizer()
        self.dict = {}

        for message in message_list:
            tmp_list = ["@"]                    ## @ as beginning of sentence
            for rword in t.tokenize(message):
                word = rword.surface
                tmp_list.append(word)

                if len(tmp_list) > 3:           ## 3 words dict
                    tmp_list = tmp_list[1:]
                elif len(tmp_list) < 3:
                    continue

                self.add_word_chain(tmp_list)

        return self.dict


    def run(self):
        opponent_markov_chain = self.make_markov_chain(self.opponent_message_list)
        my_markov_chian = self.make_markov_chain(self.my_message_list)

        ## export
        with open(self.cache_filename, "wb") as f:
            pickle.dump([opponent_markov_chain, my_markov_chian], f)


make_df = ProcessTalkHistory(glob.glob("../talk_history/*.txt")[0])