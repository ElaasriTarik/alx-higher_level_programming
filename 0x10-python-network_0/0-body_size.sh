#!/bin/bash
# URL body size

curl -s -I "$1" | grep 'Content-Lenght:' | cut -d ' ' -f2
