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
	print("\n")
	print(file_name+"start...")
	
	check_file = open(file_name, "r");
	check_file_reader = csv.reader(check_file,quoting=csv.QUOTE_ALL)

	total_tested = 0
	original_R   = 0
	predicted_correct = 0
	non_reactant_predicted_correct = 0
	predicted_wrong   = 0
	exception = 0
	reactant = 0
	non_reactant = 0
	for row in check_file_reader:
		SMILES = row[1]
		check_smiles = "SMILES="+ SMILES

		p = Popen(['java', '-jar', 'CypReactBundle/cypreact.jar', 'CypReactBundle/',check_smiles, 'test.csv', cyp], stdout=PIPE, stderr=STDOUT)
		temp_list = []

		for line in p.stdout:
			stdout_put = line.decode('ascii')
			temp_list.append(stdout_put)
			#print(stdout_put)
		try:
			result = temp_list[3]
			result = result.split(":")
			result = result[len(result)-1]
			result = result.replace(" ","")
			result = result.replace("\n","")
		except:
			result = "exception"
			print("exception: " + str(row))
		actual = row[2]
		

		if "substrate" in actual.lower() or ("active" in actual.lower() and "not" not in actual.lower()):

			if result == "R":
				predicted_correct = predicted_correct + 1  #True positive
			elif result == "exception":
				exception = exception+1
			else:
				predicted_wrong   = predicted_wrong + 1    #False positive

			reactant = reactant + 1
		elif "inactive" in actual.lower() or "not active" in actual.lower():
			if result == "N":
				non_reactant_predicted_correct = non_reactant_predicted_correct + 1    # True negative
			elif result == "exception":
				exception = exception + 1
			else:
				non_reactant_predicted_wrong   = predicted_wrong + 1				   # False negative
			non_reactant = non_reactant + 1
		else:
			print(actual)
		

	reactant_accuracy = (predicted_correct / reactant) * 100
	non_reactant_accuracy = (non_reactant_predicted_correct / non_reactant) *100
	rectant_inaccuracy = 100 - reactant_accuracy
	non_reactant_inaccuracy = 100 - non_reactant_accuracy
	
	print("non_reactant: "+str(non_reactant))
	print("reactant: "+str(reactant))
	print(reactant_accuracy,non_reactant_accuracy,rectant_inaccuracy,non_reactant_inaccuracy)
	return [reactant_accuracy,non_reactant_accuracy,rectant_inaccuracy,non_reactant_inaccuracy]
	
def check_phase2(file_name,cyp):
	print(file_name+"start...")
	print("\n")
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
		try:
			result = temp_list[3]
			result = result.split(":")
			result = result[len(result)-1]
			result = result.replace(" ","")
			result = result.replace("\n","")
		except:
			result = "N"
			print("exception: " + str(row))
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
		

	reactant_accuracy = (predicted_correct / reactant) * 100
	non_reactant_accuracy = (non_reactant_predicted_correct / non_reactant) *100
	rectant_inaccuracy = 100 - reactant_accuracy
	non_reactant_inaccuracy = 100 - non_reactant_accuracy
	print("non_reactant: "+str(non_reactant))
	print("reactant: "+str(reactant))
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
				# print(non_reactant) # 221
				# print(reactant)     # 12831
				# [reactant_accuracy,non_reactant_accuracy,rectant_inaccuracy,non_reactant_inaccuracy]
				# 77.51539240900944 27.149321266968325 22.484607590990564 72.85067873303167 (for 1A2; Date: 2018-11-28)
				
				# result = check(f,"1A2")
				result = check(f,"1A2")
				
			elif "3A4" in f:
				# non_reactant: 2910
				# reactant: 12515
				# 92.08949260886936 9.415807560137457 7.910507391130636 90.58419243986255
				result = check(f,"3A4")

			elif "2A6" in f:
				# non_reactant: 19
				# reactant: 7
				# 57.14285714285714 73.68421052631578 42.85714285714286 26.31578947368422
				result = check(f,"2A6")

			elif "2B6" in f:
				# non_reactant: 53
				# reactant: 13
				# 69.23076923076923 52.83018867924528 30.769230769230774 47.16981132075472
				result = check(f,"2B6")

			elif "2C8" in f:
				# non_reactant: 33
				# reactant: 10
				# 60.0 36.36363636363637 40.0 63.63636363636363
				result = check(f,"2C8")

			elif "2C9" in f:
				# non_reactant: 503
				# reactant: 12504
				# 79.90243122200896 25.24850894632207 20.097568777991043 74.75149105367794
				result = check(f,"2C9")

			elif "2C19" in f:
				# non_reactant: 388
				# reactant: 13083
				# 73.72162348085301 51.28865979381443 26.27837651914699 48.71134020618557
				result = check(f,"2C19")

			elif "2D6" in f:
				# non_reactant: 485
				# reactant: 13490
				# 78.39881393624908 35.670103092783506 21.601186063750916 64.3298969072165
				result = check(f,"2D6")

			elif "2E1" in f:
				# non_reactant: 7
				# reactant: 7
				# 71.42857142857143 71.42857142857143 28.57142857142857 28.57142857142857

				# result = check(f,"2E1")
				result = check(f,"2E1")
			else:
				print("unknown: "+f)





if __name__ == '__main__':
	main()