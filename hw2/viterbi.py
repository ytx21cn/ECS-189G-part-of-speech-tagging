#!/usr/bin/python

import sys
import re
import math
import itertools

# Task 2: bigram Viterbi algorithm

# Usage: python2 ./viterbi.py <hmmFile> <inputFile> > <outputFile>

INIT_STATE = "init"
FINAL_STATE = "final"
OOV_SYMBOL = "OOV"

hmmFile = sys.argv[1]
inputFile = sys.argv[2]

tags = dict()
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
				qq = previous tag
				q = current tag
				p = transition probability
			'''
			prevTag, currentTag, transProb = transMatch.groups()
			transProbs[(prevTag, currentTag)] = math.log(float(transProb))
			tags[prevTag] = 1
			tags[currentTag] = 1

		elif emitMatch:
			''' "emit" line structure:
				emit PRP$ OOV 0.666666666667

			In viterbi.pl:
				B = emission probability collection
				q = current tag
				w = word
			'''
			currentTag, word, emitProb = emitMatch.groups()
			emitProbs[(currentTag, word)] = math.log(float(emitProb))
			tags[currentTag] = 1
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
		currentLineList.insert(0, "")
		
		backtrace = dict()
		
		initProbs = {(0, INIT_STATE): 0.0} # math.log(1) = 0
		# pi_1, ..., pi_n: an initial probability distribution over tags 1, ..., n
		''' In viterbi.pl:
			V = initial probability distribution
		'''

		# for each word in the line represented by the list, with their indices starting at 1
		for i in xrange(1, currentLineLen + 1):

			word = currentLineList[i]
			
			# if a word isn't in the vocabulary, rename it with the OOV symbol
			if word not in vocab:
				word = OOV_SYMBOL # since an OOV_SYMBOL is assigned a score during training
			
			for prevTag, currentTag in itertools.product(tags, tags):
				if ((prevTag, currentTag) in transProbs) and ((currentTag, word) in emitProbs) and ((i - 1, prevTag) in initProbs):
					'''
					In viterbi.pl:
						$v = viterbi probability
					'''
					viterbiProb = initProbs[(i - 1, prevTag)] + transProbs[(prevTag, currentTag)] + emitProbs[(currentTag, word)] # log of product

					# if we found a better previous state, take note!
					if ((i, currentTag) not in initProbs) or (viterbiProb > initProbs[(i, currentTag)]):
						# note that the indices here are at least 1
						initProbs[(i, currentTag)] = viterbiProb
						backtrace[(i, currentTag)] = prevTag # best previous state

		# Now handle the last of the Viterbi equations
		foundGoal = False
		goal = float("-inf");
		foundTag = INIT_STATE

		for tag in tags:
			if ((tag, FINAL_STATE) in transProbs) and ((currentLineLen, tag) in initProbs):
				viterbiProb = initProbs[(currentLineLen, tag)] + transProbs[(tag, FINAL_STATE)]
				# if we found a better path
				if (not foundGoal) or (viterbiProb > goal):
					goal = transProbs
					foundGoal = True
					foundTag = tag

		if foundGoal:
			finalTags = []
			for i in xrange(currentLineLen, 1, -1):
				finalTags.append(backtrace[i, foundTag])
				foundTag = backtrace[i, foundTag]
			finalTags.reverse()
			print " ".join(finalTags)

		else:
			print " ".join([])
