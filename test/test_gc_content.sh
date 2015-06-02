# Trivial test of gc_content.py

INPUT=test/sample1.fasta
OUTPUT=`src/gc_content.py $INPUT`
EXPECTED="GC content: 0.4"

if [[ $OUTPUT != $EXPECTED ]]
then
	echo "test failed."
	echo "Actual: $OUTPUT"
	echo "Expected: $EXPECTED"
else
	echo "test passed."
fi
