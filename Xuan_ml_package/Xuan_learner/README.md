# load_data.py 
## load_data
1. can load data from file like csv, tsv, and arff
2. could be both training data and test data
## test_data
1. similar to load_data



# train.py
## _train__
1. train model with selected algorithms
2. example: _train_(X,y,external_X,external_y,algorithm="SVC",classes=2)
3. full list of current support ML algorithm:
	linear_model
	svm
	naive_bayes
	tree
	ensemble 
	neural_network 


# learner.py
## learner (class)
1. this class will store the training data and test data 
2. this class will utilize the concurrent method to train all the possible model
