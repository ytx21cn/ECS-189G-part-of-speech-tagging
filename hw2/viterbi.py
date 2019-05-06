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
transProbs = dict()
emitProbs = dict()
vocab = dict()

# Read the hmm file and store the log of the probabilities
# The hmm has "trans" lines and "emit" lines

with open(hmmFile) as hmmFile:
	# use splitlines() to exclude "\n"s at the end of each line
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
			transProbs[(prevState, currentState)] = math.log(float(transProb))
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
			emitProbs[(currentState, word)] = math.log(float(emitProb))
			states[currentState] = 1
			vocab[word] = 1

		else:
			pass

with open(inputFile) as inputFile:
	for line in inputFile.read().splitlines():
		currentLineList = line.split(" ");
		backtrace = dict()
		initProbs = {(0, INIT_STATE, INIT_STATE): 0.0} # math.log(1) = 0
		# pi_1, ..., pi_n: an initial probability distribution over states 1, ..., n
		
		for index, word in enumerate(currentLineList, 1): # index start from 1
			# if a word isn't in the vocabulary, rename it with the OOV symbol
			
		






