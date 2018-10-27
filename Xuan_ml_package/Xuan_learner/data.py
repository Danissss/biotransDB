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


from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import arff, sys



def load_data(absolute_path,file_type,training_data):
	"""
	load the data as csv format from absolute path
	notes: 
	1. normalize, scalize and regularize data could be done 
	outside of this function
	2. for NaN value; remove them outside the function
	3. therefore, this function assume that the dataset is well-prepared and raw

	Args:
		param1 (str): absolute directory path of the file
		param2 (str): file type: csv, tsv, arff 
		param3 (str): data type: True or False 
	Returns:
		X: attribute value
		y: labeled value for X
		if it is not training_data, then only return X
	"""
	# load file
	if file_type == "csv":
		data = pd.read_csv(absolute_path)
		dataset = data.values
	elif file_type == "tsv":
		data = pd.read_csv(absolute_path,sep="\t")
		dataset = data.values
	elif file_type == "arff":
		dataset	= arff.load(open(absolute_path, 'rb'))
	else:
		print("Wrong data file type")
		sys.exit(0)

	# prepare the training set
	instance_num = dataset.shape[0]
	attribute_num = dataset.shape[1]
	X = dataset[:,0:attribute_num-1]
	y = dataset[:,attribute_num-1]

	if training_data == True:
		return X,y 
	else:
		return X



