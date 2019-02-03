############
# Given two datasets with simles
# using Tc to determine the similarity and remove the same compound
# using chemical similarity to determine (RDK)
# put chembl ID at first
# put SMILES at second
# put InChIKEY at third
# put all other info at fourth

import csv
import sys
import os
from rdkit import DataStructs
from rdkit import Chem
from rdkit.Chem.Fingerprints import FingerprintMols
# this use Topological Fingerprints to determine the similarity


# this function is trying to combine the new dataset
# to ensure that there is no redundent molecules;
def combined_new_dataset():
	file_name = walk()

	
	checked_file = open("final_with_other_dataset.csv","w",newline='')
	csv_writer_checked = csv.writer(checked_file,quoting=csv.QUOTE_ALL)

	final_csv = open("final_.csv", newline='')
	final_csvreader = csv.reader(final_csv, delimiter=',')
	Original = []
	# append instance from final_.csv
	for row in final_csvreader:
		Original.append(row)
	final_csv.close()
	
	# ignore drugbank and chembl two backbone database
	drugbank = "DRUGBANK"
	CHEMBL   = "CHEMBL"
	for i in file_name:
		if drugbank in i.upper() or ChEMBL in i.upper():
			file_name.remove(i)
		

	# check for other dataset:
	# later for speeding up: store the Chem.MolFromSmiles and fingerprint in dictionary as key: iteration; value: fingerprint obj
	# due to lack of evidence, combined dataset needs to be manually curated;
	# with standard and advanced ml procedure, it should be easy to process the data
	for file in file_name:
		ab_csv = open(file,'r',newline='')
		ab_csvreader = csv.reader(ab_csv, delimiter=',')
		tmp_list   = []
		for row in ab_csvreader:
			tmp_list.append(row)						# assume the smiles string is in row[1]
		for cl in Original:
			for db in tmp_list:
				mol_object_c = Chem.MolFromSmiles(cl[1])
				mol_object_d = Chem.MolFromSmiles(db[1])

				fps_c = FingerprintMols.FingerprintMol(mol_object_c)
				fps_d = FingerprintMols.FingerprintMol(mol_object_d)
				similiarty  = DataStructs.FingerprintSimilarity(fps_c,fps_d)
				if similiarty == 1:
					tmp_list.remove(db)
		print("remaining compound from drugbank is: "+str(len(tmp_list)))
		# append new compound into Original list
		for remains in tmp_list:
			Original.append(remains)




		ab_csv.close()


	# write to new file 
	# remove the original similes from Original list 
	# for i in final_csvreader:
	# 	csv_writer_checked.writerow(i)
	# 	i_similes = i[1]

	# 	Original.remove(i_similes)
	for i in Original:
		csv_writer_checked.writerow(i)
	checked_file.close()

	# for file in file_name:
	# 	ab_csv = open(file, newline='')
	# 	ab_csvreader = csv.reader(ab_csv, delimiter=',')
	# 	for row in ab_csvreader:
	# 		row_similes = row[1]
	# 		if row_similes in Original:
	# 			csv_writer_checked.writerow(row)
	# 			Original.remove(row_similes)
	# 		else:
	# 			continue
	# 	ab_csv.close()

	# csv_write_file.close()
	# checked_file.close()
	# final_csv.close()






# this function combine drugbank and chembl dataset
def combine_via_chemsimilarity(drugbank_file,chembl_file):
	# print(drugbank_file)
	# print(chembl_file)

	checked_file = open("final_.csv","w",newline='')
	csv_writer_checked = csv.writer(checked_file,quoting=csv.QUOTE_ALL)
	# this file is for keep track of duplicate compounds 
	# if drugbank state the compound is inhibitor but chembl state substrate; then it needs to investigate
	checked_file_2 = open("duplicates.csv","w",newline='')
	csv_writer_checked_2 = csv.writer(checked_file_2,quoting=csv.QUOTE_ALL)
	# currently only support Drugbank data and ChEMBL data
	# later could add self-annotating data 
	try:
		drugbank_csv = open(drugbank_file, newline='')
		drugbank_csvreader = csv.reader(drugbank_csv, delimiter=',')
		ChEMBL_csv = open(chembl_file, newline='')
		ChEMBL_csvreader = csv.reader(ChEMBL_csv, delimiter=',')

	except:
		print(os.getcwd())
		sys.exit(0)


	DRUGBANK = []
	for row in drugbank_csvreader:
		DRUGBANK.append(row)
	CHEMBL   = []
	for row in ChEMBL_csvreader:
		CHEMBL.append(row)

	# if selecting drugbank compound exist in chembl;
	# print it/ save it to file
	# later need automatically store into file 
	for cl in CHEMBL:
		for db in DRUGBANK:
			try:
				mol_object_c = Chem.MolFromSmiles(cl[1])
				mol_object_d = Chem.MolFromSmiles(db[1])

				fps_c = FingerprintMols.FingerprintMol(mol_object_c)
				fps_d = FingerprintMols.FingerprintMol(mol_object_d)
				similiarty  = DataStructs.FingerprintSimilarity(fps_c,fps_d)
				if similiarty == 1:
					single_list = ["Duplicates"]
					csv_writer_checked_2.writerow(single_list)
					csv_writer_checked_2.writerow(cl)
					csv_writer_checked_2.writerow(db)
					# db_list = list(db)
					# csv_writer.writerow(db_list)
					DRUGBANK.remove(db)
			except:
				print(cl[1])
				print(db[1])

	checked_file_2.close()
	print("remaining compound from drugbank is: "+str(len(DRUGBANK)))
	for i in CHEMBL:
		csv_writer_checked.writerow(i)
	for i in DRUGBANK:
		csv_writer_checked.writerow(i)


	# csv_write_file.close()
	checked_file.close()
	checked_file.close()
	print("similarity check done ...")
	return None




# all file need have standard csv header for chembl
# assume all chembl id will be last one
def combine(file_name):

	csv_write_file = open("COMBINED.csv","w",newline='')
	csv_writer = csv.writer(csv_write_file,quoting=csv.QUOTE_ALL)



	combined_chembl_id = []
	for file in file_name:
		tmp_csv = open(file, newline='')
		csvreader = csv.reader(tmp_csv, delimiter=',')
		for row in csvreader:
			CHMEBL_ID = len(row) - 1

			combined_chembl_id.append(row[CHMEBL_ID])

		tmp_csv.close()

	Non_dup_chembl_id = list(set(combined_chembl_id))
	# print(Non_dup_chembl_id)  # printed non duplicated data 
	# sys.exit(0)

	for file in file_name:
		tmp_csv = open(file, newline='')
		csvreader = csv.reader(tmp_csv, delimiter=',')
		for row in csvreader:
			CHMEBL_ID = len(row) - 1
			CHMEBL_ID = row[CHMEBL_ID]
			if CHMEBL_ID in Non_dup_chembl_id:
				csv_writer.writerow(row)
				Non_dup_chembl_id.remove(CHMEBL_ID)
			else:
				continue
		tmp_csv.close()
	# worked
	print("COMBINED.csv created! .......")

	return None

def walk():

	F = []
	current_dir = os.getcwd()
	current_dir = current_dir+"/"

	for dirpath, dirnames, filenames in os.walk(current_dir):
		for i in filenames:
			if "csv" in i and "HMDB" not in i:
				tmp_fileName = dirpath+i
				F.append(tmp_fileName)
	return F





def main():

	file_list = walk()
	# print(file_list)  # print correct csv file name 
	# sys.exit(0)
	# combine(file_list)
	drubg_bank = "MDR1_drugbank.csv"
	chembl 	   = "MDR1ChEMBL.csv"

	combine_via_chemsimilarity(drubg_bank,chembl) 	#  this line always execute first
	combined_new_dataset()					#  this line always execute after combine_via_chemsimilarity






if __name__ == '__main__':
	main()






