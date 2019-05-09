#!/bin/bash

# train a bigram hmm tagger
perl ./train_hmm.pl jv.train.tgs jv.train.txt > my-jv-bigram.hmm

# run the Viterbi algorithm to tag some data
python2 ./viterbi.py my-jv-bigram.hmm jv.test.txt > my-jv-bigram.out

# evaluate
perl ./tag_acc.pl jv.test.tgs my-jv-bigram.out
