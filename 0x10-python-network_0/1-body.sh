#!/bin/bash
# sccript prints a sites body if status code is 200
code=$(curl -Is "$1" | grep "HTTP*" | cut -d " " -f 2)
if [ $code -eq 200 ]; then
	curl -X GET "$1"
fi
