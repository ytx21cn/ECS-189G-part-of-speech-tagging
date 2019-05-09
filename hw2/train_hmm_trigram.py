#!/usr/bin/python

# David Bamman
# 2/14/14
#
# Python port of train_hmm.pl:

# Noah A. Smith
# 2/21/08
# Code for maximum likelihood estimation of a bigram HMM from 
# column-formatted training data.

# Usage:  python2 train_hmm_trigram.py tags text > hmm-file

# The training data should consist of one line per sequence, with
# states or symbols separated by whitespace and no trailing whitespace.
# The initial and final states should not be mentioned; they are 
# implied.  
# The output format is the HMM file format as described in viterbi.pl.

import sys,re
from itertools import izip
from collections import defaultdict

TAG_FILE=sys.argv[1]
TOKEN_FILE=sys.argv[2]

vocab={}
OOV_WORD="OOV"
INIT_STATE="init"
FINAL_STATE="final"

# This training script is a slight modification of train_hmm.py, with some changes to data structures to accommodate data for the trigram model

emissions=defaultdict(lambda: defaultdict(int))
emissionsTotal=defaultdict(int)

transitions=defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
transitionsTotal=defaultdict(lambda: defaultdict(int))


with open(TAG_FILE) as tagFile, open(TOKEN_FILE) as tokenFile:
	for tagString, tokenString in izip(tagFile, tokenFile):

		tags=re.split("\s+", tagString.rstrip())
		tokens=re.split("\s+", tokenString.rstrip())
		pairs=zip(tags, tokens)

		prevprevtag=INIT_STATE
		prevtag=INIT_STATE

		for (tag, token) in pairs:

			# this block is a little trick to help with out-of-vocabulary (OOV)
			# words.  the first time we see *any* word token, we pretend it
			# is an OOV.  this lets our model decide the rate at which new
			# words of each POS-type should be expected (e.g., high for nouns,
			# low for determiners).

			if token not in vocab:
				vocab[token]=1
				token=OOV_WORD

			# increment the emission/transition observation
			emissions[tag][token]+=1
			emissionsTotal[tag]+=1
			
			transitions[prevprevtag][prevtag][tag]+=1
			transitionsTotal[prevprevtag][prevtag]+=1

			prevprevtag=prevtag
			prevtag=tag

		# don't forget the stop probability for each sentence
		transitions[prevprevtag][prevtag][FINAL_STATE]+=1
		transitionsTotal[prevprevtag][prevtag]+=1

for prevprevtag in transitions:
	for prevtag in transitions[prevprevtag]:
		for tag in transitions[prevprevtag][prevtag]:
			probability = float(transitions[prevprevtag][prevtag][tag]) / transitionsTotal[prevprevtag][prevtag]
			print "trans %s %s %s %s" % (prevprevtag, prevtag, tag, probability)

for tag in emissions:
	for token in emissions[tag]:
		probability = float(emissions[tag][token]) / emissionsTotal[tag]
		print "emit %s %s %s " % (tag, token, probability)



