---
title: "Machine learning algorithms -- step by step"
excerpt: "This is my personal note and code on basic machine learning algorithms -- from regression to neural networks." 
excerpt_separator: "<!--more-->"
image:
    teaser: 2016-08-15-ml-algorithm-stepbystep/teaser.png
categories:
  - Projects
---

## Synopsis

Personally, the best way to learn is to build myself a small prototype based on what I have learn fromthe books/theory. The *tinkering* and *debugging* parts really gave me an intuition that is missing had I just do a proof of concept in paper. 


[Here is the list of jupyter notebooks I created](https://github.com/simpleblob/ml_algorithms_stepbystep), with theory explanation and actual code side-by-side. Hope these will be useful for someone with similar itention.

## Table of Content

1. *[Linear Regression](https://github.com/simpleblob/ml_algorithms_stepbystep/blob/master/algo_example_linear_regression.ipynb)* - the basics of the basics. This notebook illustrates the solution in closed form using matrix in python.
2. *[Logistic Regression](https://github.com/simpleblob/ml_algorithms_stepbystep/blob/master/algo_example_logistic_regression_and_optimization_methods.ipynb)* - another bread and butter algorithm. Mostly useful for probability-type predictions (Churn rate, yes/no, certain classifications). Here I used gradient descent as an optimization method.
3. *[Neural Network: Perceptron](https://github.com/simpleblob/ml_algorithms_stepbystep/blob/master/algo_example_NN_perceptron.ipynb)* - the most simple type of NN. 
4. *[Neural Network: Multi-layer](https://github.com/simpleblob/ml_algorithms_stepbystep/blob/master/algo_example_NN_multilayer_FNN.ipynb)* - a more elaborate type with a hidden layer in the middle. Illustrates backpropagation method with MNIST digit image dataset.

## TODO

More will be updated once finished and cleaned up the code..
