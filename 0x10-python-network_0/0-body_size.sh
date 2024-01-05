#!/bin/bash
# URL body size
curl -s -I "$1" | grep 'Content-Length:' | cut -d' ' -f2
