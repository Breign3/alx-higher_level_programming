#!/bin/bash
# display all HTTP methods the server will accept using curl.
curl -sI ALLOW "$1" -L | grep "Allow"  | cut -d " " -f2-
