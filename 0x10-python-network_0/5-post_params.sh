#!/bin/bash
# sends a post request
curl $1 -sX POST -d "email=test@gmail.com&subject=I will always\
be here for PLD"
