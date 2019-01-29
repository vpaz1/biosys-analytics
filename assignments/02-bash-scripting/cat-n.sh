#!/bin/bash

#set -u # output warning for misspells

FILE=$1 # first argument

if [[ $# -ne 1 ]]; then # if the num of args is equal to 1
	echo "Usage: cat-n.sh FILE"
	exit 1
elif [[ $# -eq 1 ]] && [[ -f "$FILE" ]]; then
i=0
while read -r LINE; do
	i=$((i+1))
	echo $i $LINE
done < "$FILE"
	exit 1
else
	echo "$FILE is not a file"
        exit 1
fi
