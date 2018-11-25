import sys
import os
# from ParseChEMBLBioAct import ChEMBL_Data_cleanup
from combine import combine_via_chemsimilarity






def walk(filetype):

	F = []
	current_dir = os.getcwd()
	current_dir = current_dir+"/"

	for dirpath, dirnames, filenames in os.walk(current_dir):
		for i in filenames:
			# print(i)
			if "cypreact" not in i.lower():
				if filetype in i:
					tmp_fileName = dirpath+i
					F.append(tmp_fileName)
	return F



def main():
	cwd = os.getcwd()
	# os.chdir("/Users/xuan/Desktop/biotransDB/Create_dataset_from_DB/chembl_compound_parse/new_dir")
	filenames = walk("csv")
	print(filenames)
	cypreact_file = cwd +"/Extracted_CypReactDataset.csv"
	# print(filenames)
	for file in filenames:
		combine_via_chemsimilarity(file,cypreact_file)
		os.chdir(cwd)



if __name__ == '__main__':
	main()





