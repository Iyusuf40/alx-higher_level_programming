#!/bin/bash
# sccript prints the size of the body oa http response
curl -Is "$1" | grep "Content-Length*" | cut -d " " -f 2
