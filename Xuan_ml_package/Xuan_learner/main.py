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
	# new_learner = learner(sys.argv[1])
	# new_learner.get_training_data()
	# new_learner.learn_all()
	# new_learner.brutal_force_("SVC") # grid search the hyperparameter for SVC model


	## generate molecular descriptors from csv file
	## csv file: row[0]:name row[1]:smiles string

	sample_file = "/Users/xuan/Desktop/biotransDB/Xuan_ml_package/Xuan_learner/Sample_data.csv"
	
	
	print("___________Done@")




if __name__ == '__main__':
	main()