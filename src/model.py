from __future__ import division

from sklearn.neural_network import MLPClassifier

def NN_model(X):
	'''A perceptron classifier for classifying whether a route should be made
	one-way or not for a particular time-period. 
	
	Parameters
	==========
	X : int, array
	    An integer column matrix    
	The default algorithm ‘adam’ works pretty well on relatively large datasets
	(with thousands of training samples or more) in terms of both training time and validation score. For small datasets, however, ‘l-bfgs’ can converge faster and perform better.

    activation: logistic, the logistic sigmoid function, returns f(x) = 1 / (1 + exp(-x)).
    alpha: 0.0001 default
    learning_rate: 'constant'
    max_iter : int, optional, default 200
    tol : float, optional, default 1e-4
	
	'''
	clf = MLPClassifier(hidden_layer_sizes=(0, 0), activation='logistic', algorithm='l-bfgs',
		                early_stopping=True)
	return clf.predict(X)
