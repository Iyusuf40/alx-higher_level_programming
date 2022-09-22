#!/bin/bash
# sccript sends an options request to 1st parameter
curl -sX OPTIONS $1 | grep Allow | cut -d " " -f 2-
