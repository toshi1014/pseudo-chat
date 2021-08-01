import glob, sys, os
sys.path.append(os.path.realpath('./src'))
from core import *

if __name__ == '__main__':
    for file in glob.glob("talk_histories/*.txt"):
        process_talk_history.ProcessTalkHistory(file)