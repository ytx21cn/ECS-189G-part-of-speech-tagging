#!/bin/bash

# train a bigram hmm tagger
perl ./train_hmm.pl ptb.2-21.tgs ptb.2-21.txt > my-bigram.hmm

# run the Viterbi algorithm to tag some data
python2 ./viterbi.py my-bigram.hmm ptb.23.txt > my-23-bigram.out

