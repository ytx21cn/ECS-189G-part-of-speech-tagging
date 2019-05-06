subsetMaker=./make-subsets.sh
sourceFile=$1
sourceFileMainName="${sourceFile%.*}"
tagsFile=${sourceFileMainName}.tgs
subsetsDir=$2
outputFile=$3

trainingScript=./train_hmm.py
hmm=./my.hmm
out=./my.out
evaluate=./tag_acc.pl
viterbiScript=./viterbi.pl


if [ "$1" = "" ] || [ "$2" = "" ] || [ "$3" = "" ]
then
	echo "Usage: ./get-subsets-training-data.sh <source file> <subsets directory (end with \"/\")> <output file>"
	exit -1
fi

rm -f $outputFile

$subsetMaker $sourceFile $subsetsDir

for i in ${subsetsDir}*
do

	echo $i | tee -a $outputFile
	
	# 1. training
	$trainingScript $tagsFile $i > $hmm
	# 2. tag some data using Viterbi
	$viterbiScript $hmm < $i > $out
	# 3. evaluate
	$evaluate $tagsFile $out | tee -a $outputFile

	echo -e "\n" | tee -a $outputFile
	
done


