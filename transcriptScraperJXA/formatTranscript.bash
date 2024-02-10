#!/bin/bash

# Format a LinkedIn course transcript

selectTextLineNum=`pbpaste | sed -n '/Selecting transcript lines/='`

pbpaste | sed "1,$(( selectTextLineNum-2 ))d" | sed '2d' | fold -sw80 | \
sed "$d" | pbcopy
