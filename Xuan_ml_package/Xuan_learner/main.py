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

# local file import 
import learner
import generate_mol_descriptor
import sys



def main():

	## define the object; sys.argv[1] is the absolute_path 
	sample_file = "/Users/xuan/Desktop/biotransDB/Xuan_ml_package/Xuan_learner/TrainingDataMF.csv"
	new_learner = learner.learner(sample_file)
	training_X, training_y = new_learner.get_training_data()  # TESTED:PASS
	new_learner.learn_all()
	sys.exit(0)
	new_learner.brutal_force_("SVC") # grid search the hyperparameter for SVC model


	## generate molecular descriptors from csv file
	## csv file: row[0]:name row[1]:smiles string	
	
	print("___________Done@")




if __name__ == '__main__':
	main()