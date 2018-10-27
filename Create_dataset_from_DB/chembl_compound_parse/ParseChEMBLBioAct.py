import csv 
import sys
import sqlite3 


def investigate_duplicate_ChEMBLID():


















# create three different csv file
# _substrate_v_inhibitor.csv
# _inactive_v_active.csv
# _duplicated.csv
def ChEMBL_Data_cleanup(FileName):
	Final_list = []
	ChEMBLID_Tracker = []

	write_file = open(FileName+'_cleaned.csv', 'w', newline='')
	spamwriter = csv.writer(write_file, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

	duplicated_chembl_id_file = open("duplicated_chembl_id_file.txt","w")
	duplicated_chembl_id = []

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
		spamwriter.writerow(["CMPD_CHEMBLID","ACTIVITY_COMMENT","CANONICAL_SMILES","PUBMED_ID"])
		
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

			# Cleanup the data
			# this one doesn't really work
			# if curation_type == "Expert" and assay_organism == "Homo sapiens":

			# 	temp_list_1 = [ChEMBL_ID,activity,smiles,reference]
			# 	spamwriter.writerow(temp_list_1)
			# else:
			# 	continue
			if ChEMBL_ID not in ChEMBLID_Tracker:
				ChEMBLID_Tracker.append(ChEMBL_ID)
			
				# if ChEMBL_ID not in ChEMBLID_Tracker:
				# 	temp_list_1 = [ChEMBL_ID,activity,smiles,reference,assay]
				# 	ChEMBLID_Tracker.append(ChEMBL_ID)
				# else:
				# 	continue
				temp_list = [ChEMBL_ID,activity,smiles,reference,curation_type]
				# print(str(temp_list))
				# sys.exit(0)
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
						# els_.append(temp_list)
						continue
				else:
					continue
			else:
				duplicated_chembl_id_file.write(ChEMBL_ID+",")
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

	with open(FileName+"_substrate_v_inhibitor.csv", "w",newline='') as writeFile_1:
		writer_csv_1 = csv.writer(writeFile_1, quoting=csv.QUOTE_ALL)
		for i in substrate_v_inhibitor:
			writer_csv_1.writerow(i)


	with open(FileName+"_inactive_v_active.csv", "w",newline='') as writeFile_2:
		writer_csv_2 = csv.writer(writeFile_2, quoting=csv.QUOTE_ALL)
		for i in substrate_v_inhibitor:
			writer_csv_2.writerow(i)


	with open(FileName+"_duplicated.csv", "w",newline='') as writeFile_3:
		writer_csv_3 = csv.writer(writeFile_3, quoting=csv.QUOTE_ALL)
		for i in duplicated:
			writer_csv_3.writerow(i)

	writeFile_1.close()
	writeFile_2.close()
	writeFile_3.close()


	return Final_list





def main():

	FileName = sys.argv[1]
	ChEMBL_data = ChEMBL_Data_cleanup(FileName)
	duplicate_file_name = FileName + "_duplicated.csv"
	investigate_duplicate_ChEMBLID(duplicate_file_name)

	


if __name__ == '__main__':
	main()