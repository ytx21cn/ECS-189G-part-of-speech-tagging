#!/bin/bash

# train a bigram hmm tagger
perl ./train_hmm.pl ptb.2-21.tgs ptb.2-21.txt > my-bigram.hmm

# run the Viterbi algorithm to tag some data
python2 ./viterbi.py my-bigram.hmm ptb.22.txt > my-bigram.out

# evaluate
perl ./tag_acc.pl ptb.22.tgs my-bigram.out
