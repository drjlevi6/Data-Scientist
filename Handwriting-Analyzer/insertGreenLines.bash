#!/bin/bash

# Substitutes lines of green pixels into a grid of letters at 100-pixel intervals

#Usage: cat <ifile> | insertRedLines.bash > <ofile>

sed '264,268s/[A-Z][A-Z]/BA/g;
364,368s/[A-Z][A-Z]/BA/g;
464,468s/[A-Z][A-Z]/BA/g;
564,568s/[A-Z][A-Z]/BA/g;
664,668s/[A-Z][A-Z]/BA/g;
764,768s/[A-Z][A-Z]/BA/g;
864,868s/[A-Z][A-Z]/BA/g;
964,968s/[A-Z][A-Z]/BA/g;
1064,1068s/[A-Z][A-Z]/BA/g;
1164,1168s/[A-Z][A-Z]/BA/g;
358,362s/[A-Z][A-Z]/BA/g;
458,462s/[A-Z][A-Z]/BA/g;
558,562s/[A-Z][A-Z]/BA/g;
658,662s/[A-Z][A-Z]/BA/g;
758,762s/[A-Z][A-Z]/BA/g;
858,862s/[A-Z][A-Z]/BA/g;
958,962s/[A-Z][A-Z]/BA/g;
1058,1062s/[A-Z][A-Z]/BA/g;
1158,1162s/[A-Z][A-Z]/BA/g;
1258,1262s/[A-Z][A-Z]/BA/g'
