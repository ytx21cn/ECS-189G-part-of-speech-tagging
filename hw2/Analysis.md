# ECS 189G Part of speech tagging

## Task 1

In this task, the file I used to train ([ptb.2-21.txt](./ptb.2-21.txt)) contains 39832 lines. Hence I chose breakpoints to be 500, 1000, 2000, 5000, 10000, 20000, 40000. I stored the results in [task1-results.txt](./task1-results.txt). The plot of errors vs. training size is seen as follows:

![](./task1.svg)

The results are not very surprising. The assumption is that the larger the corpus is used for training, the less percent error will be occuring; it is verified by the plot.

