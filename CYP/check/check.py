import subprocess
import csv
import os
import sys
from subprocess import Popen, PIPE, STDOUT

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


def check(file_name,cyp):
	check_file = open(file_name, "r");
	check_file_reader = csv.reader(check_file,quoting=csv.QUOTE_ALL)

	total_tested = 0;
	original_R   = 0;
	predicted_correct = 0;
	non_reactant_predicted_correct = 0;
	predicted_wrong   = 0;
	reactant = 0;
	non_reactant = 0;
	for row in check_file_reader:
		SMILES = row[1]
		check_smiles = "SMILES="+ SMILES

		p = Popen(['java', '-jar', 'CypReactBundle/cypreact.jar', 'CypReactBundle/',check_smiles, 'test.csv', cyp], stdout=PIPE, stderr=STDOUT)
		temp_list = []

		for line in p.stdout:
			stdout_put = line.decode('ascii')
			temp_list.append(stdout_put)
			#print(stdout_put)
		result = temp_list[3]
		result = result.split(":")
		result = result[len(result)-1]
		result = result.replace(" ","")
		result = result.replace("\n","")
		actual = row[2]

		if "substrate" in actual.lower() or ("active" in actual.lower() and "not" not in actual.lower()):

			if result == "R":
				predicted_correct = predicted_correct + 1  #True positive
			else:
				predicted_wrong   = predicted_wrong + 1    #False positive

			reactant = reactant + 1
		elif "inactive" in actual.lower() or "not active" in actual.lower():
			if result == "N":
				non_reactant_predicted_correct = non_reactant_predicted_correct + 1    # True negative
			else:
				non_reactant_predicted_wrong   = predicted_wrong + 1				   # False negative
			non_reactant = non_reactant + 1
		else:
			print(actual)
		sys.exit(0)

	reactant_accuracy = (predicted_correct / reactant) * 100
	non_reactant_accuracy = (non_reactant_predicted_correct / non_reactant) *100
	rectant_inaccuracy = 100 - reactant_accuracy
	non_reactant_inaccuracy = 100 - non_reactant_accuracy

	print(reactant_accuracy,non_reactant_accuracy,rectant_inaccuracy,non_reactant_inaccuracy)
	return [reactant_accuracy,non_reactant_accuracy,rectant_inaccuracy,non_reactant_inaccuracy]
	
		


def main():
	#p = Popen(['java', '-jar', 'CypReactBundle/cypreact.jar', 'CypReactBundle/',"SMILES=c1ccccc1NCC", 'test.csv', '1A2' ], stdout=PIPE, stderr=STDOUT)
	# result = subprocess.call(['java', '-jar', 'CypReactBundle/cypreact.jar', 'CypReactBundle/',"SMILES=c1ccccc1NCC", 'test.csv', '1A2' ])
	# print(result)
	#for line in p.stdout:
		#stdout_put = line.decode('ascii')
		#print(stdout_put)
	files = walk("csv")

	for f in files:
		if "test" not in f:
		# print(f)
			if "1A2" in f:
				check(f,"1A2")


if __name__ == '__main__':
	main()