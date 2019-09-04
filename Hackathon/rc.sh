#!/bin/bash

if [[ -z $1 ]]; then
  sudo python robocmd.py
elif [[ -z $2 ]]; then
  sudo python robocmd.py $1
else
  sudo python robocmd.py $1 $2
fi
