import subprocess
import csv
import os
import sys
from subprocess import Popen, PIPE, STDOUT









def main():
	p = Popen(['java', '-jar', 'CypReactBundle/cypreact.jar', 'CypReactBundle/',"SMILES=c1ccccc1NCC", 'test.csv', '1A2' ], stdout=PIPE, stderr=STDOUT)
	# result = subprocess.call(['java', '-jar', 'CypReactBundle/cypreact.jar', 'CypReactBundle/',"SMILES=c1ccccc1NCC", 'test.csv', '1A2' ])
	# print(result)
	for line in p.stdout:
		stdout_put = line.decode('ascii')
		print(stdout_put)



if __name__ == '__main__':
	main()