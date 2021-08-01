#!/bin/bash

set -e

usage(){
    echo -e "" >&2
    echo -e "Usage: bash run.sh [options] <opponent's name>" >&2
    echo >&2
    echo "Options: " >&2
    echo -e "\t-r\trefresh all caches" >&2
    echo -e "\t-n\tnot check update in talk_histories/\n" >&2

    exit 1
}

if [ $# -gt 2 ] || [ $# -lt 1  ]; then
    usage
else
    while getopts rn OPT; do
        case $OPT in
            "r" ) REFRESH=True;;
            "n" ) NO_CHECK=True;;
            * ) usage;;
        esac
    done
    shift $(($OPTIND - 1))

    if [ $# -ne 1 ]; then
        usage
    else
        OPPONENT_NAME=$1
    fi
fi

if [ "$REFRESH" = "True" ]; then
    echo -e "refreshing caches\n"
    # if cache/ is not empty
    if ! [ "`ls cache`" = "" ]; then
        for file in cache/*; do
            rm "$file"
        done
    fi
fi


## read & set config
CONFIG=`cat config.txt`
eval $CONFIG
CODE="
;const ICON_FILENAME = '${ICON_FILENAME}';
const url = 'ws://${HOST}:${PORT}';
"

## remove & write config line in index.js
sed -i "$ d" templates/index.js
echo $CODE >> templates/index.js

source $VENV_DIR/bin/activate
if ! [ "$NO_CHECK" = "True" ]; then
    if ! [ "$REFRESH" = "True" ]; then
        echo -e "checking caches\n"
    fi
    python3 src/utils/handle_cache.py
fi

python3 src/main.py $HOST $PORT $OPPONENT_NAME