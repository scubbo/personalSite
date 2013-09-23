#!/bin/zsh
ssh pi 'df' 2&>/dev/null | grep '/var/media' | perl -pe 's/.*\s([0-9]+)%.*/$1/'
