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
				A = transition probability collection
				qq = previous state
				q = current state
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
				B = emission probability collection
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
		''' In viterbi.pl:
			@w: current line as a list
			$n: length of current line
		'''
		currentLineList = line.split(" ");
		currentLineLen = len(currentLineList);
		backtrace = dict()
		initProbs = {(0, INIT_STATE): 0.0} # math.log(1) = 0
		# pi_1, ..., pi_n: an initial probability distribution over states 1, ..., n
		''' In viterbi.pl:
			V = initial probability distribution
		'''

		# for each word in the line represented by the list, with their indices starting at 1
		for index, word in enumerate(currentLineList, 1):
			
			# if a word isn't in the vocabulary, rename it with the OOV symbol
			if word not in vocab:
				word = OOV_SYMBOL # since an OOV_SYMBOL is assigned a score during training
			
			for prevState, currentState in itertools.product(states, states):
				if ((prevState, currentState) in transProbs) and ((currentState, word) in emitProbs) and ((index - 1, prevState) in initProbs):
					'''
					In viterbi.pl:
						$v = viterbi probability
					'''
					viterbiProb = initProbs[(index - 1, prevState)] + transProbs[(prevState, currentState)] + emitProbs[(currentState, word)] # log of product

					# if we found a better previous state, take note!
					if ((index, currentState) not in initProbs) or (viterbiProb > initProbs[(index, currentState)]):
						initProbs[(index, currentState)] = viterbiProb
						backtrace[(index, currentState)] = prevState # best previous state

		# Now handle the last of the Viterbi equations
		foundGoal = False
		goal = float("-inf");
		foundState = INIT_STATE

		for state in states:
			if ((state, FINAL_STATE) in transProbs) and ((currentLineLen, state) in initProbs)
				viterbiProb = initProbs[(currentLineLen, state)] + transProbs[(state, FINAL_STATE)]
				# if we found a better path
				if (not foundGoal) or (viterbiProb > goal):
					goal = transProbs
					foundGoal = True
					foundState = state
					
