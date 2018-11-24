import sys
import csv
import os


def extract_cypreact_dataset():

	file = open("CypReactDataset.tsv","r")
	csv_file = open("Extracted_"+CypReactDataset+".csv", "w",newline='')
	csv_writer = csv.writer(csv_file,quoting=csv.QUOTE_ALL)

	with file as cypreact:
		rd = csv.reader(cypreact,delimiter="\t",quoting=csv.QUOTE_NONE)

		# read the header and remove it 
		header  = next(rd)
		for i in range(0,20):
			print(header[i])
		# print(header)
		SMILES = header.index("IsomericSmiles")
		Ligand_Name = header.index("Name")
		CYP1A2 = header.index("1A2")   # this will return R (reactant) or Y (?)
		CYP2A6 = header.index("2A6")
		CYP2B6 = header.index("2B6")
		CYP2C8 = header.index("2C8")
		CYP2C9 = header.index("2C9")
		CYP2C19 = header.index("2C19")
		CYP2D6 = header.index("2D6")
		CYP2E1 = header.index("2|E1")
		CYP3A4 = header.index("3A4")

		for row in rd:
			try:
				tempTuple = (row[Ligand_Name], row[SMILES],row[CYP1A2],row[CYP2A6],row[CYP2B6],
					row[CYP2C8],row[CYP2C9],row[CYP2C19],row[CYP2D6],row[CYP2E1],row[CYP3A4])
				csv_writer.writerow(tempTuple)
			except:
				print(row[Ligand_Name])
	file.close()
	csv_file.close()
	print("DONE\n")


def main():
	extract_cypreact_dataset()




if __name__ == '__main__':
	main()