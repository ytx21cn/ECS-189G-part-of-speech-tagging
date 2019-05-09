#!/bin/bash

# train a bigram hmm tagger
perl ./train_hmm.pl btb.train.tgs btb.train.txt > my-btb-bigram-given.hmm

# run the Viterbi algorithm to tag some data
perl ./viterbi.pl my-btb-bigram-given.hmm btb.test.txt > my-btb-bigram-given.out

# evaluate
perl ./tag_acc.pl btb.test.tgs my-btb-bigram-given.out
