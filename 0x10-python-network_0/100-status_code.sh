#!/bin/bash
# sends a get request
curl -w %{http_code} $1 -so /dev/null
