#!/bin/bash

# train a bigram hmm tagger
perl ./train_hmm.pl jv.train.tgs jv.train.txt > my-jv-bigram-given.hmm

# run the Viterbi algorithm to tag some data
perl ./viterbi.pl my-jv-bigram-given.hmm jv.test.txt > my-jv-bigram-given.out

# evaluate
perl ./tag_acc.pl jv.test.tgs my-jv-bigram-given.out
