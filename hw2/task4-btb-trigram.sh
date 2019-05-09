#!/bin/bash

# train a trigram hmm tagger
python2 ./train_hmm_trigram.py btb.train.tgs btb.train.txt > my-btb-trigram.hmm

# run the Viterbi algorithm to tag some data
python2 ./viterbi-trigram.py my-btb-trigram.hmm btb.test.txt > my-btb-trigram.out

# evaluate
perl ./tag_acc.pl btb.test.tgs my-btb-trigram.out
