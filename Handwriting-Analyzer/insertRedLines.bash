#!/bin/bash

# Substitutes lines of red pixels into a grid of letters at 100-pixel intervals

#Usage: cat <ifile> | insertRedLines.bash > <ofile>

sed '263s/[A-Z][A-Z]/OP/g;
363s/[A-Z][A-Z]/OP/g;
463s/[A-Z][A-Z]/OP/g;
563s/[A-Z][A-Z]/OP/g;
663s/[A-Z][A-Z]/OP/g;
763s/[A-Z][A-Z]/OP/g;
863s/[A-Z][A-Z]/OP/g;
963s/[A-Z][A-Z]/OP/g;
1063s/[A-Z][A-Z]/OP/g;
1163s/[A-Z][A-Z]/OP/g;
1263s/[A-Z][A-Z]/OP/g'
