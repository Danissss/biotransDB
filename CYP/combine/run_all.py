import sys
import os
# from ParseChEMBLBioAct import ChEMBL_Data_cleanup
from combine import combine_via_chemsimilarity





# Just use os.listdir and os.path.isfile instead of os.walk for file only in current dir

def walk(filetype):

	F = []
	FR = []
	current_dir = os.getcwd()
	current_dir = current_dir+"/"
	files = [f for f in os.listdir('.') if os.path.isfile(f)]

	# get file only in current directory
	for fr in os.listdir('.'):
		if os.path.isfile(fr):
			if filetype in fr and "cypreact" not in fr.lower():
				FR.append(fr)



	for dirpath, dirnames, filenames in os.walk(current_dir):
		for i in filenames:
			# print(i)
			if "cypreact" not in i.lower():
				if filetype in i:
					tmp_fileName = dirpath+i
					F.append(tmp_fileName)
	return FR



def main():
	cwd = os.getcwd()
	# os.chdir("/Users/xuan/Desktop/biotransDB/Create_dataset_from_DB/chembl_compound_parse/new_dir")
	filenames = walk("csv")
	# print(filenames)
	cypreact_file = cwd +"/Extracted_CypReactDataset.csv"

	for file in filenames:
		# print(file)
		combine_via_chemsimilarity(file,cypreact_file)
		os.chdir(cwd)
		sys.exit(0)


if __name__ == '__main__':
	main()





