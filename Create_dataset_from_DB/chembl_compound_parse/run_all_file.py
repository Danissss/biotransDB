import csv 
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


	# List files ONLY in the current directory
	files = [f for f in os.listdir('.') if os.path.isfile(f) and filetype in f]
	return files






def main():

	file_name = walk("txt")
	cwd = os.getcwd()
	for i in file_name:
		ChEMBL_Data_cleanup(i)
		os.chdir(cwd)










if __name__ == '__main__':
	main()