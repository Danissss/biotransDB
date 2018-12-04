import csv 
import sys
import sqlite3 
import os 


def investigate_duplicate_ChEMBLID():
	return None




# create three different csv file
# _substrate_v_inhibitor.csv
# _inactive_v_active.csv
# _duplicated.csv
def ChEMBL_Data_cleanup(FileName):

	# create new directory:
	transporter_name = FileName.split('.')[0]
	cwd = os.getcwd()
	FileName = cwd+"/"+FileName

	newdirectory = cwd+"/"+transporter_name
	try:
		os.makedirs(newdirectory)
	except:
		print("directory exist...")
	# os.chdir("/Users/xuan/Desktop/biotransDB/Create_dataset_from_DB/chembl_compound_parse/new_dir")
	os.chdir(newdirectory)
	
	# now working on new directory



	Final_list = []
	ChEMBLID_Tracker = []
	duplicated_chembl_id = []

	# keep track of index
	CMPD_CHEMBLID = None
	ACTIVITY_COMMENT = None
	CANONICAL_SMILES = None
	PUBMED_ID = None
	ASSAY_ORGANISM = None
	Autocuration = None
	with open(FileName) as fd:
		rd = csv.reader(fd, delimiter="\t")

		for row in rd:
			CMPD_CHEMBLID = row.index("CMPD_CHEMBLID")
			ACTIVITY_COMMENT = row.index("ACTIVITY_COMMENT")
			CANONICAL_SMILES = row.index("CANONICAL_SMILES")
			PUBMED_ID = row.index("PUBMED_ID")
			ASSAY_ORGANISM = row.index("ASSAY_ORGANISM")
			Autocuration = row.index("CURATED_BY")
			break
		next(rd) # remove the header;


		substrate = []
		substrate_c_id = []
		inhibitor = []
		inhibitor_c_id = []
		Active = []
		inactive = []
		duplicated = []
		els_ = []
		for row in rd:
			ChEMBL_ID = row[CMPD_CHEMBLID]
			activity  = row[ACTIVITY_COMMENT]
			smiles    = row[CANONICAL_SMILES]
			reference = row[PUBMED_ID]
			assay_organism = row[ASSAY_ORGANISM]
			# curation type doesn't matter 
			curation_type = row[Autocuration] 

			if ChEMBL_ID not in ChEMBLID_Tracker:
				ChEMBLID_Tracker.append(ChEMBL_ID)
			

				temp_list = [ChEMBL_ID,smiles,activity,reference]
				

				# write file with following style
				# later will manually check duplicated compound if there any conflict
				if activity != "":
					if "substrate" in activity and "not" not in activity:
						substrate.append(temp_list)
						# substrate is active compound for the protein target;
						Active.append(temp_list)  
						substrate_c_id.append(ChEMBL_ID)
					elif "inhibitor" in activity and "not" not in activity:
						inhibitor.append(temp_list)
						# inhibitor is active compound for the protein target;
						Active.append(temp_list)
						inhibitor_c_id.append(ChEMBL_ID)
					elif activity == "Active":
						Active.append(temp_list)
					elif activity == "Not Active" or activity == "inactive":
						inactive.append(temp_list)
					else:
						els_.append(temp_list)
						continue
				else:
					continue
			else:
				# duplicated_chembl_id_file.write(ChEMBL_ID+",")
				duplicated_chembl_id.append(ChEMBL_ID)
				duplicated.append(temp_list)

			#find the compound that are both substrate and inhibitor
		conflict_id = []
		for sub_id in substrate_c_id:
			if sub_id in inhibitor_c_id:
				conflict_id.append(sub_id)
			else:
				continue
		# print(len(conflict_id))





	substrate_v_inhibitor = substrate + inhibitor
	active_v_inactive = Active + inactive

	with open(newdirectory+"/_substrate_v_inhibitor.csv", "w",newline='') as writeFile_1:
		writer_csv_1 = csv.writer(writeFile_1, quoting=csv.QUOTE_ALL)
		for i in substrate_v_inhibitor:
			writer_csv_1.writerow(i)


	with open(newdirectory+"/_inactive_v_active.csv", "w",newline='') as writeFile_2:
		writer_csv_2 = csv.writer(writeFile_2, quoting=csv.QUOTE_ALL)
		for i in active_v_inactive:
			writer_csv_2.writerow(i)


	with open(newdirectory+"/_duplicated.csv", "w",newline='') as writeFile_3:
		writer_csv_3 = csv.writer(writeFile_3, quoting=csv.QUOTE_ALL)
		for i in duplicated:
			writer_csv_3.writerow(i)

	with open(newdirectory+"/_else_type.csv", "w",newline='') as writeFile_5:
		writer_csv_5 = csv.writer(writeFile_5, quoting=csv.QUOTE_ALL)
		for i in els_:
			writer_csv_5.writerow(i)



	# this is for investigate the duplicate compound in ChEMBL database 
	new_chembl_file = open(FileName,"r")
	new_cheml_csv_reader = csv.reader(new_chembl_file,delimiter=',')
	duplicated_id_file =  open(newdirectory+"/_duplicated_id_for_investigate.csv", "w",newline='')
	writer_csv_4 = csv.writer(duplicated_id_file, quoting=csv.QUOTE_ALL)

	for duplicate_compound in duplicated:

		chembl_id = duplicate_compound[0]
		tmp_id_list = [chembl_id]
		writer_csv_4.writerow(chembl_id)
		for row in new_cheml_csv_reader:
			if row[CMPD_CHEMBLID] == chembl_id:
				tmp_list_for_duplicate = [row[CMPD_CHEMBLID],row[ACTIVITY_COMMENT],row[PUBMED_ID]]
				writer_csv_4.writerow(tmp_list_for_duplicate)


	duplicated_id_file.close()





	writeFile_1.close()
	writeFile_2.close()
	writeFile_3.close()
	writeFile_5.close()
	new_chembl_file.close()
	duplicated_id_file.close()



	return Final_list





def main():

	FileName = sys.argv[1]
	ChEMBL_data = ChEMBL_Data_cleanup(FileName)
	duplicate_file_name = FileName + "_duplicated.csv"
	investigate_duplicate_ChEMBLID(duplicate_file_name)

	


if __name__ == '__main__':
	main()