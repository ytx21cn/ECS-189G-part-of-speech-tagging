import sys
import re
import math

# Task 2: bigram Viterbi algorithm

# Usage: python2 viterbi.py hmmFile < inputFile > tagsFile

INIT_STATE = "init"
FINAL_STATE = "final"
OOV_SYMBOL = "OOV"

hmmFile = sys.argv[1]
inputFile = sys.argv[2]

states = dict()
transitionProbs = dict()
emissionProbs = dict()
vocabulary = dict()

# Read the hmm file and store the log of the probabilities
# The hmm has "trans" lines and "emit" lines

with open(hmmFile) as hmmFile:
	for line in hmmFile.read().splitlines():
		'''
		Line structures in a hmm file:
		trans PRP$ NNS 0.166666666667
		emit PRP$ OOV 0.666666666667

		Existing regex in viterbi.pl:
		m/trans\s+(\S+)\s+(\S+)\s+(\S+)/
		m/emit\s+(\S+)\s+(\S+)\s+(\S+)/
		See: https://docs.python.org/2.7/library/re.html?highlight=regular%20expression
		\s: whitespace
		\S: non-whitespace
		'''
		dataReg = "\s+(\S+)\s+(\S+)\s+(\S+)"
		transReg = "trans" + dataReg;
		emitReg = "emit" + dataReg;

		transMatch = re.match(transReg, line)
		emitMatch = re.match(emitReg, line)

		if transMatch:
			''' "trans" line structure:
				trans PRP$ NNS 0.166666666667

			In viterbi.pl:
				qq = previous
				q = current
				p = transition probability
			'''
			prevState, currentState, transProb = transMatch.groups()
			trans[[prevState, currentState]] = math.log(float(transProb))
			states[prevState] = 1
			states[currState] = 1

		elif emitMatch:
			''' "emit" line structure:
				emit PRP$ OOV 0.666666666667

			In viterbi.pl:
				q = current state
				w = word
			'''
			currentState, word, emitProb = emitMatch.groups()
			emit[[currentState, word]] = math.log(float(emitProb))
			states[currentState] = 1
			vocabulary[word] = 1

		else:
			pass







