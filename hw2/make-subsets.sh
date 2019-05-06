filter=./filter-lines.sh
sourceFile=$1
sourceFileMainName="${sourceFile%.*}"
subsetsDir=$2

if [ "$1" = "" ] || [ "$2" = "" ]
then
	echo "Usage: ./make-subsets.sh <file> <subsets directory>"
	exit -1
fi

mkdir -p $subsetsDir
rm -f $subsetsDir/*
chmod +x $filter

for i in 500 1000 2000 5000 10000 20000 40000
do
	$filter $sourceFile $i > $subsetsDir/$sourceFileMainName-$i.txt
done
