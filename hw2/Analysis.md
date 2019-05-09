# ECS 189G Part of speech tagging

## Task 1

In this task, the file I used to train ([ptb.2-21.txt](./ptb.2-21.txt)) contains 39832 lines. Hence I chose breakpoints to be 500, 1000, 2000, 5000, 10000, 20000, 40000. I stored the results in [task1-results.txt](./task1-results.txt). The plot of errors vs. training size is seen as follows:

![](./task1.svg)

The results are not very surprising. The assumption is that the larger the corpus is used for training, the less percent error will be occuring; it is verified by the plot.

## Task 3

For this task, I chose to implement the trigram viterbi algorithm, as suggested in the discussion slides. For this task, there is a noticeable change in data structure, in order to accomodate the data for each of three consecutive states. I also need to have the previous two states of the first word to be set to the initial state.

I have trained my models using [ptb.2-21.txt](ptb.2-21.txt) and tested my models using [ptb.22.txt](ptb.22.txt), and stored the bigram viterbi results (from **Task 2**) and trigram viterbi results in separate text files for comparison.

My results for [bigram](my-bigram-results-backup.txt):
```
error rate by word:      0.0539920731859312 (2166 errors out of 40117)
error rate by sentence:  0.654705882352941 (1113 errors out of 1700)
```

My results for [trigram](my-trigram-results-backup.txt):
```
error rate by word:      0.085101079342922 (3414 errors out of 40117)
error rate by sentence:  0.634705882352941 (1079 errors out of 1700)
```

I observed a 0.02 improvement for the error rate by sentence. However, the error rate by word is back off by 0.03. I also wanted to try deleted interpolation and add-k smoothing techniques, but due to time constraints (the midterm was just one day before this project's deadline) I was unable to succeed in doing it.

I then tagged the data for [ptb.23.txt](ptb.23.txt). The output tags are stored in [my-23-bigram.out](my-23-bigram.out) and [my-23-trigram.out](my-23-trigram.out).

## Task 4

I used my own viterbi algorithm to run the tests for Bulgarian and Japanese. The results are as follows:

### Bulgarian

[Bigram](my-btb-bigram-results.txt):
```
error rate by word:      0.116616110549376 (692 errors out of 5934)
error rate by sentence:  0.756281407035176 (301 errors out of 398)
```

[Trigram](my-btb-trigram-results.txt):
```
error rate by word:      0.211156049882036 (1253 errors out of 5934)
error rate by sentence:  0.778894472361809 (310 errors out of 398)
```

### Japanese

[Bigram](my-jv-bigram-results.txt):
```
error rate by word:      0.0628611451584661 (359 errors out of 5711)
error rate by sentence:  0.136812411847673 (97 errors out of 709)
```

[Trigram](my-jv-trigram-results.txt):
```
error rate by word:      0.326037471546139 (1862 errors out of 5711)
error rate by sentence:  0.293370944992948 (208 errors out of 709)
```

**Note:** For Japanese, I encountered some problem with producing the outputs due to some formatting issues (period "." at the end of each line of the tags). I had to do a minor modification to my code, and the modified viterby codes are [viterbi-jv.py](viterbi-jv.py) and [viterbi-trigram-jv.py](viterbi-trigram-jv.py).

### Observations

For these two languages, I have found that the bigram viterbi model performs better than the trigram viterbi model on both languages. From these observations, I think that these two languages would have less long-term dependences of words within a sentence, but each two adjacent words could play more important roles in POS tagging.

## Task 5
I was unable to do this part due to time constraints.
