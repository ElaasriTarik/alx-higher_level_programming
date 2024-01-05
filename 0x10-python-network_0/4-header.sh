#!/bin/bash
# send a get request with a header
curl -sL -H "X-School-User-Id: 98" -X GET "$1"
