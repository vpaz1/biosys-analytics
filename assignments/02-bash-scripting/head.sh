#!/bin/bash

FILE=$1 # first argument
NUM=$2

if [[ $# -lt 1 ]]; then # if the num of args is equal to 1
        echo "Usage: head.sh FILE NUM_LINES"
        exit 1
fi

if [[ $# -eq 1 ]] && [[ -f "$FILE" ]]; then # Only one argument default 3
i=0
while read -r LINE; do
        echo $LINE
        i=$((i+1))
        if [[ $i -eq 3 ]]; then
		break
        fi
done < "$FILE"
	exit 1
fi

if [[ $# -eq 2 ]] && [[ -f "$FILE" ]] ; then # Both arguments
i=0
while read -r LINE; do
	echo $LINE
        i=$((i+1))
        if [[ $i -eq "$NUM" ]] ; then
                        break
        fi
done < "$FILE"
	exit 1
else
	echo "$FILE is not a file"
        exit 1
fi
