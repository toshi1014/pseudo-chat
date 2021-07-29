import re, glob, os
import pandas as pd
from meta_characters import *


class ProcessTalkHistory():
    def __init__(self, filepath_):
        self.filepath = filepath_
        if not self.is_cached():
            # self.make_df()
            pass
        self.make_df()      # TEMP:

    def is_cached(self):
        with open(self.filepath, "r", encoding="UTF-8") as f:
            row1, row2 = f.readlines()[:2]

        self.opponent_name = row1.strip(HEADER_PREFIX).strip(HEADER_SUFFIX)
        saved_date = re.sub("\\D", "", row2)         ## remove un-number => saved_date == yyyymmdd

        self.cache_filename = "../cache/" + self.opponent_name + "_" + saved_date + ".pickle"
        return os.path.exists(self.cache_filename)

    def remove_non_string(self, message):
        if message in [STAMP_EMOTICON, IMAGE, VIDEO]:
            return "NONE"
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

                # TODO: add validation for name
                message_list.append(self.remove_non_string(message))

        data_dict = {
            "date": date_list, "time": time_list,
            "name": name_list, "message": message_list,
        }

        df = pd.DataFrame(data_dict, columns=data_dict.keys())

        df.to_csv(self.cache_filename[:-7] + ".csv")      # DEBUG:
        df.to_pickle(self.cache_filename)


make_df = ProcessTalkHistory(glob.glob("../talk_history/*.txt")[0])