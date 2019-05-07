#!/bin/bash

file=$1
numLines=$2
startingLine=1

sed -n "${startingLine},${numLines}p" $file
