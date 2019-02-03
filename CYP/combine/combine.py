import csv
import sys
import os
from rdkit import DataStructs
from rdkit import Chem
from rdkit.Chem.Fingerprints import FingerprintMols


		# CYP1A2 = header.index("1A2")  2
		# CYP2A6 = header.index("2A6")	3
		# CYP2B6 = header.index("2B6")	4
		# CYP2C8 = header.index("2C8")	5
		# CYP2C9 = header.index("2C9")	6
		# CYP2C19 = header.index("2C19")7
		# CYP2D6 = header.index("2D6")	8
		# CYP2E1 = header.index("2|E1") 9
		# CYP3A4 = header.index("3A4")	10

		
# cypfile contain single cyp class (i.e. CYP1A2)
# cypreact file contain all cyp class (i.e. 9 cyp class)
# if cypfile = 1A2:
#    cyp = [append compound from cypfile 1A2]
#    cypreact = [select the compound that only R for 1A2 from cypreact file]
# 	 see if there is any duplicates (indicate by the similarity)
#    if duplicate appear
#       remove duplicate from cyp
#
#
#    cyp = [remaining compound]
#    total_test = len(cyp)
#    correct_test = 0
#    for cyps_similes in cyp:
#        return_1A2 = cypreact_program(cyps_similes)   # either R or Y
#        if return_1A2 == chembl_annotated:
#            correct_test++
#    accuracy_on_experimental_data = correct_test / total_test
#    print("Result for "+cypfile)
#    print("Totally Test compound {0}".format(total_test))
#    print("Correct Percentage: {0}%".format(accuracy_on_experimental_data*100))


def combine_via_chemsimilarity(cypfile,cypreact):
	print("Start: "+ cypfile)
	cwd = os.getcwd()

	print(cwd+"/"+cypfile)
	
	sys.exit(0)
	


	cyp_name = cypfile.split("/")
	cyp_name = cyp_name[len(cyp_name)-1]
	cyp_name = cyp_name.split(".")[0]

# create new directory:
	newdirectory = cwd+"/"+cyp_name
	try:
		os.makedirs(newdirectory)
	except:
		print("directory exist")
	# os.chdir("/Users/xuan/Desktop/biotransDB/Create_dataset_from_DB/chembl_compound_parse/new_dir")
	os.chdir(newdirectory)

	checked_file = open(cyp_name+"_final_.csv","w",newline='')
	csv_writer_checked = csv.writer(checked_file,quoting=csv.QUOTE_ALL)
	# this file is for keep track of duplicate compounds 
	# if drugbank state the compound is inhibitor but chembl state substrate; then it needs to investigate
	checked_file_2 = open(cyp_name+"_duplicates.csv","w",newline='')
	csv_writer_checked_2 = csv.writer(checked_file,quoting=csv.QUOTE_ALL)
	# currently only support Drugbank data and ChEMBL data
	# later could add self-annotating data 

	drugbank_csv = open(cwd+"/"+cypfile, newline='')
	drugbank_csvreader = csv.reader(drugbank_csv, delimiter=',')
	ChEMBL_csv = open(cwd+"/"+cypreact, newline='')
	ChEMBL_csvreader = csv.reader(ChEMBL_csv, delimiter=',')

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

	checked_file_2.close()
	print("remaining compound from drugbank is: "+str(len(DRUGBANK)))
	for i in CHEMBL:
		csv_writer_checked.writerow(i)
	for i in DRUGBANK:
		csv_writer_checked.writerow(i)


	# csv_write_file.close()
	checked_file.close()
	print("similarity check done ...")
	return None










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
