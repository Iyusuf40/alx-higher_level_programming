#!/bin/bash
# sends a post request
curl -sX POST -d @$2 $1 -H "Content-type: application/json"
