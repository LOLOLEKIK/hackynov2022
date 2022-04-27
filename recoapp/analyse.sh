#!/bin/bash

rand=$(( $RANDOM % 2 ))
if [ $rand -eq 0 ]
then
echo "$1 Bad"
else
echo "$1 Good"
fi
