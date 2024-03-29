import os
import csv
import sys
from combineTwoDataset import combined_new_dataset
from combineTwoDataset import combine_via_chemsimilarity





# determine the number of folders
# cd to each folder
# do combine work
# exit from each folder
# do next folder
# (note: in each folder, determine the number of files and parse them/ combine them)

def main():
	cwd = os.getcwd()
	# os.walk(directory)
	directory_list = [x[0] for x in os.walk(cwd)]
	directory_file_list = [x[2] for x in os.walk(cwd)]
	directory_list.pop(0)
	directory_list.pop(0)
	for sub_directory in directory_list:
		os.chdir(sub_directory)
		current_dir = os.getcwd()
		# print(os.getcwd())
		chembl_file = None
		drugbank_file = None
		if "__pycache__" not in sub_directory:
			for dirpath, dirnames, filenames in os.walk(current_dir):
				for files in filenames:
				# print(files)
					if "final" in files:
						chembl_file = current_dir +"/"+files
					else:
						drugbank_file = current_dir +"/"+files
			# print(chembl_file)
			# print(drugbank_file)
			# print("===============?===============")
			combine_via_chemsimilarity(drugbank_file,chembl_file)

			os.chdir(cwd)
			print(os.getcwd())
			print("==============================")
			# sys.exit(0)


if __name__ == '__main__':
	main()