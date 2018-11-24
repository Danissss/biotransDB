import sys
import os
from ParseChEMBLBioAct import ChEMBL_Data_cleanup







def walk(filetype):

	F = []
	current_dir = os.getcwd()
	current_dir = current_dir+"/"

	for dirpath, dirnames, filenames in os.walk(current_dir):
		for i in filenames:
			if filetype in i:
				tmp_fileName = dirpath+i
				F.append(tmp_fileName)
	return F



def main():
	
	# os.chdir("/Users/xuan/Desktop/biotransDB/Create_dataset_from_DB/chembl_compound_parse/new_dir")
	
	filenames = walk("txt")
	for file in filenames:
		CYP_split = file.split('/')
		CYP_txt = CYP_split[len(CYP_split)-1]
		CYP = CYP_txt.split(".")[0]
		ChEMBL_Data_cleanup(CYP)





if __name__ == '__main__':
	main()





