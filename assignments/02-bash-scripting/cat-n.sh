#!/bin/bash

#set -u # output warning for misspells

FILE=$1 # first argument

if [[ $# -eq 0 ]]; then # if the num of args is equal to 1
	echo "Usage: cat-n.sh FILE"
	exit 1
fi

if [[ ! -f "$FILE" ]]; then
	echo "$FILE is not a file"
        exit 1 
fi

i=0
while read -r LINE; do
        i=$((i+1))
        echo "$i $LINE"
done < "$FILE"
