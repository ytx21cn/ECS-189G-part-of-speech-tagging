#!/bin/bash

# train a bigram hmm tagger
perl ./train_hmm.pl ptb.2-21.tgs ptb.2-21.txt > my-bigram-given.hmm

# run the Viterbi algorithm to tag some data
perl ./viterbi.pl my-bigram-given.hmm ptb.22.txt > my-bigram-given.out

# evaluate
perl ./tag_acc.pl ptb.22.tgs my-bigram-given.out
