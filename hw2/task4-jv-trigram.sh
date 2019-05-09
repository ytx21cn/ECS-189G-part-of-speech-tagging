#!/bin/bash

# train a trigram hmm tagger
python2 ./train_hmm_trigram.py jv.train.tgs jv.train.txt > my-jv-trigram.hmm

# run the Viterbi algorithm to tag some data
python2 ./viterbi-trigram-jv.py my-jv-trigram.hmm jv.test.txt > my-jv-trigram.out

# evaluate
perl ./tag_acc.pl jv.test.tgs my-jv-trigram.out
