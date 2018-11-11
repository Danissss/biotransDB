# biotransDB

## Create_dataset_from_DB
1. Parse all available dataset from online, lab, etc. of compound into standard form 
2. Combine all dataset into one big dataset by eliminating the duplicate compounds via check molecular similary using RDKit module
3. Get the combined dataset, however, some of the compound data is not completed; hence it needs human to curate further
4. (Later on, will do machine-curateable paper reader)

## Xuan_ml_package
1. Contain most of state of art machine learning algorithm obtained from sklearn
2. There is one module in this folder that will generate the descriptor for compounds via using RDKit
3. Using various ML algorithm and various setting for training the models; for each setting, it will print the total result report for user to review
4. (Later on, will implement and add new machine learning algorithm and tricks (such as PGM) for other purpose)


# other file are not important
