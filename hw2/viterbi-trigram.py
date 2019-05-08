#!/usr/bin/python

import sys
import re
import math
import itertools

# Task 3: trigram Viterbi algorithm

# Usage: python2 ./viterbi-trigram.py <hmmFile> <inputFile> > <outputFile>

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
		trans VBP NNP MD 0.0409090909091
		emit VBD assumed 0.000401485496336 

		Regex, see: https://docs.python.org/2.7/library/re.html?highlight=regular%20expression
		\s: whitespace
		\S: non-whitespace
		'''
		transDataReg = "\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)"
		transReg = "trans" + transDataReg
		emitDataReg = "\s+(\S+)\s+(\S+)\s+(\S+)"
		emitReg = "emit" + emitDataReg;

		transMatch = re.match(transReg, line)
		emitMatch = re.match(emitReg, line)

		if transMatch:
			''' "trans" line structure:
				trans VBP NNP MD 0.0409090909091
			'''
			prevPrevTag, prevTag, currentTag, transProb = transMatch.groups()
			transProbs[(prevPrevTag, prevTag, currentTag)] = math.log(float(transProb))
			tags[prevPrevTag] = 1
			tags[prevTag] = 1
			tags[currentTag] = 1

		elif emitMatch:
			''' "emit" line structure:
				emit VBD assumed 0.000401485496336
			'''
			currentTag, word, emitProb = emitMatch.groups()
			emitProbs[(currentTag, word)] = math.log(float(emitProb))
			tags[currentTag] = 1
			vocab[word] = 1

		else:
			pass

with open(inputFile) as inputFile:
	for line in inputFile.read().splitlines():
		currentLineList = line.split(" ");
		currentLineLen = len(currentLineList);
		
		backtrace = dict()
		initProbs = {(0, INIT_STATE, INIT_STATE): 0.0} # math.log(1) = 0
		# pi_1, ..., pi_n: an initial probability distribution over tags 1, ..., n

		# for each word in the line represented by the list, with their indices starting at 1
		for index, word in enumerate(currentLineList, 1):
			
			# if a word isn't in the vocabulary, rename it with the OOV symbol
			if word not in vocab:
				word = OOV_SYMBOL # since an OOV_SYMBOL is assigned a score during training
			
			for prevPrevTag, prevTag, currentTag in itertools.product(tags, tags, tags):
				
				if ((prevPrevTag, prevTag, currentTag) in transProbs) and ((currentTag, word) in emitProbs) and ((index - 1, prevPrevTag, prevTag) in initProbs):
					viterbiProb = initProbs[(index - 1, prevPrevTag, prevTag)] + transProbs[(prevPrevTag, prevTag, currentTag)] + emitProbs[(currentTag, word)] # log of product

					# if we found a better previous state, take note!
					if ((index, prevTag, currentTag) not in initProbs) or (viterbiProb > initProbs[(index, prevTag, currentTag)]):
						# note that the indices here are at least 1
						initProbs[(index, prevTag, currentTag)] = viterbiProb
						backtrace[(index, prevTag, currentTag)] = prevPrevTag

		# Now handle the last of the Viterbi equations
		foundGoal = False
		goal = float("-inf");
		foundTag = INIT_STATE
		foundPrevTag = INIT_STATE

		for prevTag, currentTag in itertools.product(tags, tags):
			
			if ((prevTag, currentTag, FINAL_STATE) in transProbs) and ((currentLineLen, prevTag, currentTag) in initProbs):
				viterbiProb = initProbs[(currentLineLen, prevTag, currentTag)] + transProbs[(prevTag, currentTag, FINAL_STATE)]
				# if we found a better path
				if (not foundGoal) or (viterbiProb > goal):
					goal = transProbs
					foundGoal = True
					foundTag = currentTag
					foundPrevTag = prevTag
		
		if foundGoal:
			finalTags = [foundPrevTag]
			
			for i in xrange(currentLineLen, 2, -1):
				finalTags.append(backtrace[(i, foundPrevTag, foundTag)])
				temp = foundPrevTag
				foundPrevTag = backtrace[(i, foundPrevTag, foundTag)]
				foundTag = temp
				
			finalTags.reverse()
			print " ".join(finalTags)

		else:
			print "".join([])
