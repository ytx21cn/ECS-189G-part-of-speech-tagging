#!/bin/bash

# train a bigram hmm tagger
python2 ./train_hmm.py btb.train.tgs btb.train.txt > my-btb-bigram.hmm

# run the Viterbi algorithm to tag some data
python2 ./viterbi.py my-btb-bigram.hmm btb.test.txt > my-btb-bigram.out

# evaluate
perl ./tag_acc.pl btb.test.tgs my-btb-bigram.out
