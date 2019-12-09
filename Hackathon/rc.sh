#!/bin/bash

if [[ -z $1 ]]; then
  sudo python robocmd.py
elif [[ $1 = "aes" && -n $2 ]]; then
  sudo python aescmd.py $2
elif [[ -z $2 ]]; then
  sudo python robocmd.py $1
else
  sudo python robocmd.py $1 $2
fi
