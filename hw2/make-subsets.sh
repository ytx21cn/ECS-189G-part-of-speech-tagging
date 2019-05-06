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
chmod +x $filter

for i in 50 100 200 500 1000 1500 2000
do
	$filter $sourceFile $i > $subsetsDir/$sourceFileMainName-$i.txt
done
