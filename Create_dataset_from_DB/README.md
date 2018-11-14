## Collecting data from online database;
1. Find the online database that contain rich experimental data (non-predicted data) with reference.
2. Find the download options
3. If datafile is in rational database, then use sql; If datafile is plain text file (e.g. csv, tsv, etc.); either directly parsing into desired csv file or meanwhile, setup sqlite database. (Note: keep the parsing file for newly updated database)
4. Follow the most intution way to combine the dataset into one dataset (i.e. save them as one big csv file for training set purpose)
5. Validate each training instance (if have time or find mistake in the original online dataset)



# ChEMBL
1. Download the whole db(.sqlite3) file from download page to parse (note: the relation between protein and compound are not clear)
2. Go to each protein section, and download the bioactivity data for parsing



# Drugbank
1. Drugbank has the data file in xml format; easy to parse and get desired information
2. large xml file is not easy to parse, see "how to parse large xml file"



# BindingDB
1. download the data file in tsv format and parse
2. most of data from BindingDB are from CHEMBL



# HMDB
1. We have access to the HMDB mysql database; so it is easy to read the data from query
2. HMDB has data in xml file but it is very large


# Other less important database
1. ChEBI
2. KEGG Drug




# TODO
1. combine data via chemblID and chemical similiarty remain test 
2. List of transporters (Drugbank)
3. List of transporters (ChEMBL)
4. List of transporters ()



# Note
1. bindingDB doesn't provide a lot of information about compound, plus it use a lot of data from chembl; hence exclude the bindingDB data
2. Drugbank and ChEMBL data are enough for the prediction model building for now; run similiarty test on it