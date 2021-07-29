import glob
from core import *

if __name__ == '__main__':
    for file in glob.glob("talk_histories/*.txt"):
        process_talk_history.ProcessTalkHistory(file)