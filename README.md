# NLP-OT

This repository contains the work done during a research project with Paul Mortamet and guided by Dr. François Yvon.

The Notebook contains the final report and the code that we used to get our results and the changes that we tested.

## Abstract

There are few specific studies on
the use of Optimal Transport in
word alignment problems between
sentences in different languages (Word
Alignment). Our study follows the work of
Our study follows the work of Zi-Yi Dou and Gra-
ham Neubig [7] who introduced this method lightly into the
the method into the problems of Word Alignment.
of Word Alignment. We have
studied the implications of Sinkhorn's algorithm
algorithm and the construction of the
the cost matrix in the approximation of the
of the Optimal Transport Plan. By
observing the different successive steps of the
of the method of Dou and Neubig
[7], we propose an optimisation of the Sinkhron
the Sinkhron algorithm through a
the entropy regularisation parameter.
entropy regularisation parameter. Then, we propose a
the construction of the cost ma-
the construction of the cost model, by defining two new distances.
distances. We conclude our study by
study by proposing a new and more flexible method
method for extracting alignments, which is more flexible
and adapted to different distributions.


## Content

- Introduction
    - Embedding spaces
    - Multilingual embedding spaces
    - Earth mover's distance
- Word Alignment
- Optimal transport
- Our research
    - Entropic regularization
    - A deeper analysis of the cost matrix
- Conclusion