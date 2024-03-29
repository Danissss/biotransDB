################################################################################
# Copyright (C) <date> X Consortium
#
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the Software 
# is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#################################################################################


#
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split


from sklearn import linear_model
from sklearn import svm
from sklearn import naive_bayes
from sklearn import tree
from sklearn import ensemble 
from sklearn import neural_network 

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

from sklearn.externals import joblib

import pickle 
# import cPickle
import datetime
import os
import sys


# default classes is 2 (binary)
def create_model_for_brutal(X,y,algorithm,classes=2):
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=0)
	if algorithm == "SVC":
		model = svm.SVC(gamma="auto")
	elif algorithm == "NuSVC":
		model = svm.NuSVC()
	elif algorithm == "LinearSVC":
		model = svm.LinearSVC(random_state=0)
	elif algorithm == "GaussianNB":
		model = naive_bayes.GaussianNB()
	elif algorithm == "BernoulliNB":
		model = naive_bayes.BernoulliNB()
	elif algorithm == "MultinomialNB":
		model = naive_bayes.MultinomialNB()
	elif algorithm == "DecisionTreeClassifier":
		model = tree.DecisionTreeClassifier()
	elif algorithm == "RandomForestClassifier":
		model = ensemble.RandomForestClassifier(n_estimators=10)
	elif algorithm == "MLPClassifier":
		model = neural_network.MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
	else:
		print("more algorithm please select by coding")
		sys.exit(0)
	# elif algorithm == "ExtraTreesClassifier":
	# 	model = ensemble.ExtraTreesClassifier()


	model.fit(X,y)
	return model
# 
## return1: information for single algorithm
## return2: the absolute path for the model
def train(X,y,external_X,external_y,algorithm,classes):
	"""
	train:
		train every possible popular machine learning algorithm with given data
		measurement/evaluation are cross-validation 5, 10, 15 and 0.8:0.2 split test
	Args:
		param1 (str): training X
		param2 (str): training y
		param3 (str): external testing X
		param4 (str): external testing y
		param5 (str): the algorithm to run 
		param6 (num): the number of classes/labels ==TODO
	limiation:
		only works for classification 
		regression: ==TODO
	return:
		list of string that each element describe a score
	"""
	#
	c_time = datetime.datetime.now()
	times  = c_time.strftime('%S_%M_%H_%m_%d_%Y')
	cwd = os.getcwd()
	model_name = algorithm+"_"+times
	model_ = cwd + "/" + model_name+".pkl"
	model_file = open(model_, 'wb')

	# report_path = cwd+"/report.txt"
	# report = open(report_path,"w")

	#

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=0)
	if algorithm == "SVC":
		model = svm.SVC(gamma="auto")
	elif algorithm == "NuSVC":
		model = svm.NuSVC()
	elif algorithm == "LinearSVC":
		model = svm.LinearSVC(random_state=0)
	elif algorithm == "GaussianNB":
		model = naive_bayes.GaussianNB()
	elif algorithm == "BernoulliNB":
		model = naive_bayes.BernoulliNB()
	elif algorithm == "MultinomialNB":
		model = naive_bayes.MultinomialNB()
	elif algorithm == "DecisionTreeClassifier":
		model = tree.DecisionTreeClassifier()
	elif algorithm == "RandomForestClassifier":
		model = ensemble.RandomForestClassifier(n_estimators=10)
	elif algorithm == "MLPClassifier":
		model = neural_network.MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
	else:
		print("more algorithm please select by coding")
		sys.exit(0)
	# elif algorithm == "ExtraTreesClassifier":
	# 	model = ensemble.ExtraTreesClassifier()


	model.fit(X,y)
	#cv
	cv = [5,10,15]
	score_result = []
	for i in cv:
		mean_score = cross_val_score(model, X,y, cv=i).mean()
		mean_score_2_decimal = "{0:.2f}".format(mean_score)
		score_result.append("score for cv-"+str(i)+"= "+str(mean_score_2_decimal)+";")

	# test split (tp = test split) 0.8:0.2:
	model.fit(X_train,y_train)
	test_score = model.score(X_test,y_test)
	score_result.append("score for 0.8 split ="+str(test_score)+";")
	# external on full dataset
	if external_X != None and external_y != None:
		external_test_score = model.score(external_X,external_y)
		score_result.append("score for external test data ="+str(external_test_score)+";")



	report = algorithm+" result: "+str(score_result)
	# print(algorithm+" result: "+str(score_result))
	pickle.dump(model, model_file) 
	# load the model
	# https://stackoverflow.com/questions/10592605/save-classifier-to-disk-in-scikit-learn
	# load it again
	# with open('my_dumped_classifier.pkl', 'rb') as fid:
 #    	gnb_loaded = pickle.load(fid)
	return report, model_


def brutal(X,y,model,algorithm):
	'''
	This function will try the scklearn grid search (brutal force)
	to find the best parameters
	1. RandomizedSearchCV
	2. GridSearchCV
	3. given the best estimates 
	Args:
		param1 (str): X (training data)
		param2 (str): y (label)
		param3 (str): fitted model
		param4 (str): name of the alogrithm
	Note:
		some ML algorithm is not tuneable such as NB;
	'''
	# Because couldn't pickle.load(model) (error: TypeError: a bytes-like object is required, not '_io.BufferedReader')
	# Has to create the model here 
	# default is binary classification
	# model = create_model_for_brutal(X,y,algorithm);

	# use a full grid over all parameters
	if algorithm == "RandomForestClassifier":
		param_grid = {"max_depth": [3, None],
			"max_features": [1, 3, 10],
			"min_samples_split": [2, 3, 10],
			"min_samples_leaf": [1, 3, 10],
			"bootstrap": [True, False],
			"criterion": ["gini", "entropy"]}
	elif algorithm == "SVC":
		param_grid = {'kernel':('rbf','poly','sigmoid','precomputed'),'degree':list(range(1, 5)),
           'coef0':[1.0,2.0,3.0,4.0,5.0],'probability':(False,True)}
		# gamma,class_weight is not in this grid
	elif algorithm == "NuSVC":
		SVC_grid = {'nu':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],'kernel':('rbf','poly','sigmoid','precomputed'),'degree':[1,10],
           'coef0':[1.0,10.0],'probability':(False,True)}
	elif algorithm == "LinearSVC":
		param_grid = {"C":list(range(1,10)),"loss":("hinge","squared_hinge"),'dual':(True,False)}
	else:

		print("Wrong/unsupported alogrithm name")



	grid_search = GridSearchCV(model, param_grid=param_grid)       

	grid_search.fit(X, y) # ValueError: X should be a square kernel matrix
	print(grid_search.best_params_)
	return grid_search.best_params_



