# pseudo-chat

**pseudo-chat** offers unreal & likely chat with your friends

By reading your talk history, the new phony messages would be fabricated

* Message is generated by simple markov chain algorithm

* At this time, only adapt to [*Line*](https://en.wikipedia.org/wiki/Line_(software) app

![sample_image](docs/sample1.png)

## Requirements
* Python 3.6+
(In latest ver., lib *thread* might not work well)

* Ubuntu 18.04 LTS on **WSL**

## Setup
1. create & activate virtualenv by e.g.
```
virtualenv env1 && source env1/bin/activate
```
    default env name is *env1*

    (you can change in *config.txt*)

2. install python lib by
```
pip install -r requirements.txt
```

3. make *talk_histories* directory at root

## Usage
1. export talk history from *Line* app

2. put the .txt in *talk_histories/*

3. put icon file in *templates/* as you like

    default icon filename is *icon.png*

    (you can change in *config.txt*)

4. run *run.sh* by e.g.
```
bash run.sh Alice
```
As above, *Alice* corresponds to opponent's name in chat

5. push *receive* & *send* button

## Config

Param | Desc
----|----
HOST | hosting
PORT | port number
ICON_FILENAME | filename for icon
VENV_DIR | name of virtualenv


## Acknowledgement

My .html & .css heavily refer to the following

https://github.com/nakox0706/3owebcreate/tree/chat_line_css/chat_line_css