#!/bin/bash

# Format a LinkedIn course transcript

# Locate text beginning
#selectTextLineNum=$(( `pbpaste | sed -En '/ *\- \[/='` ))
selectTextLineNum=$(( `pbpaste | sed -En '/^( *\- )?[\[\(]/=' | tail -n 1` ))
echo $selectTextLineNum

pbpaste | 
sed "1,$(( selectTextLineNum - 3 ))d"  | # cut lines up to 2 before selectTextLineNum
fold -sw80  | \
sed '/Enable interactive transcripts/d; /Selecting transcript lines/d' |
sed '/^video/d' | 
sed '/^$/d' | # delete any blank lines (may be >1 at end)
sed '/Find in transcript/d; /Filter results/d; /Chat with Coach/d' |
pbcopy; pbpaste
