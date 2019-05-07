#!/bin/bash

subsetMaker=./make-subsets.sh

sourceFile=$1
sourceFileMainName="${sourceFile%.*}"
tagsFile=${sourceFileMainName}.tgs

subsetsDir=$2

testFile=$3
testFileMainName="${testFile%.*}"
testTagsFile=${testFileMainName}.tgs


outputFile=$4

trainingScript=./train_hmm.py
hmm=./my.hmm
out=./my.out
evaluate=./tag_acc.pl
viterbiScript=./viterbi.pl


if [ "$1" = "" ] || [ "$2" = "" ] || [ "$3" = "" ] || [ "$4" = "" ]
then
	echo "Usage: ./get-subsets-training-data.sh <source file> <subsets directory (end with \"/\")> <tagging test file> <output file>"
	exit -1
fi

rm -f $outputFile

$subsetMaker $sourceFile $subsetsDir

for i in ${subsetsDir}*
do

	echo $i | tee -a $outputFile
	echo $testTagsFile | tee -a $outputFile
	
	# 1. training
	$trainingScript $tagsFile $i > $hmm
	# 2. tag some data using Viterbi
	$viterbiScript $hmm < $testFile > $out
	# 3. evaluate
	$evaluate $testTagsFile $out | tee -a $outputFile

	echo -e "\n" | tee -a $outputFile
	
done


