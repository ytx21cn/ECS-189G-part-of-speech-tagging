#!/bin/bash

# train a trigram hmm tagger
python2 ./train_hmm_trigram.py ptb.2-21.tgs ptb.2-21.txt > my-trigram.hmm

# run the Viterbi algorithm to tag some data
python2 ./viterbi-trigram.py my-trigram.hmm ptb.22.txt > my-trigram.out

# evaluate
perl ./tag_acc.pl ptb.22.tgs my-trigram.out
