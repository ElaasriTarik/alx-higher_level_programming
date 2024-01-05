#!/bin/bash
# all allowed methods
curl -s -I "$1" | grep 'Allow:' | sed -n -e 's/^Allow: //p'
