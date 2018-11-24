import os





# determine the number of folders
# cd to each folder
# do combine work
# exit from each folder
# do next folder
# (note: in each folder, determine the number of files and parse them/ combine them)

def main():
	cwd = os.getcwd()
	os.walk(directory)
	directory_list = [x[0] for x in os.walk(directory)]
	for sub_directory in directory_list:
		print(sub_directory)
		# os.chdir(newdirectory)

if __name__ == '__main__':
	main()