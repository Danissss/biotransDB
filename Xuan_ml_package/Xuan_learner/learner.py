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

import data
import sys
from train import train
from train import brutal
import multiprocessing
import pickle 
from concurrent.futures import ProcessPoolExecutor

class learner:
	"""
	TODO:
		visualziation task

	learner class:
		store the training data, testing data
		perform data visualization task
	
	"""

	def __init__(self,absolute_path):
		self.training_X = None
		self.training_y = None
		self.external_testing_X = None
		self.external_testing_y = None
		self.absolute_path = absolute_path
		self.worker_n = multiprocessing.cpu_count()


	def get_training_data(self):
		path_as_list = self.absolute_path.split(".")
		length_path_as_list = len(path_as_list)
		file_type = path_as_list[length_path_as_list-1]
		self.training_X,self.training_y = data.load_data(self.absolute_path,file_type,training_data=True)
		# print(self.training_X)
		# print(self.training_y)
		return self.training_X, self.training_y


	def get_external_testing_data(self,absolute_path):
		path_as_list = absolute_path.split(".")
		length_path_as_list = len(path_as_list)
		file_type = path_as_list[length_path_as_list-1]
		self.external_testing_X,self.external_testing_y = data.load_data(absolute_path,file_type,training_data=True)


	def undersampling(self):
		return None

	def oversampling(self):
		return None

	def learn_all(self):
		'''
		Concurrent python will utilize all thread 
		'''
		algorithms = ["SVC","NuSVC","LinearSVC","GaussianNB",
		"BernoulliNB","MultinomialNB","DecisionTreeClassifier",
		"RandomForestClassifier","MLPClassifier"]
		with ProcessPoolExecutor(max_workers=self.worker_n) as executor:
			for ML_ in algorithms:
				# print(self.training_y)
				# print(self.worker_n)
				future = executor.submit(train,self.training_X,self.training_y,
					self.external_testing_X,self.external_testing_y,
					algorithm=ML_,classes=2)
				val_1 = future.result()
				print(val_1)
				sys.exit(0)

	def brutal_force_(self,algorithms):
		'''
		Using brutal force to find the best parameter for selected models
		
		'''
		model_directory = train(self.training_X,self.training_y,
					self.external_testing_X,self.external_testing_y,
					algorithm=algorithms,classes=2)
		model = pickle.loads(model_directory)
		# return and print the best parameter 
		brutal(self.training_X,self.training_y,model,algorithms)

		return None
	

















