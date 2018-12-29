import sys
import csv
import sqlite3 
import os

# note: default transporter is Multidrug Resistance Transporter MDR 1


def create_db():
	file = open("BindingDB_All.tsv","r")
	conn = sqlite3.connect('bindingdb.db')
	c = conn.cursor()
	# c.execute("DROP TABLE IF EXISTS BindingDB")
	c.execute("CREATE TABLE IF NOT EXISTS BindingDB\
             (Ligand_Name text, SMILES text, InChIKey text, target_name text, target_organism text,\
             target_source_organism text, chembl_id text,uniprot_id text)")

	with file as BindingDB:
		rd = csv.reader(BindingDB,delimiter="\t",quoting=csv.QUOTE_NONE)
		# read the header and remove it 
		header  = next(rd)
		# print(header)
		SMILES = header.index("Ligand SMILES")
		InChIKey = header.index("Ligand InChI Key")
		Ligand_Name = header.index("BindingDB Ligand Name")
		target_name = header.index("Target Name Assigned by Curator or DataSource")
		target_organism = header.index("Target Source Organism According to Curator or DataSource")
		target_source_organism = header.index("Target Source Organism According to Curator or DataSource")
		chembl_id = header.index("ChEMBL ID of Ligand")
		uniprot_id = header.index("UniProt (SwissProt) Primary ID of Target Chain")
		Ki_ = header.index("Ki (nM)")
		IC50_ = header.index("IC50 (nM)")
		Kd_ = header.index("Kd (nM)")
		EC50_ = header.index("EC50 (nM)")
		pH_ = header.index("pH")
		Temp_ = header.index("Temp (C)")
		PMID_ = header.index("PMID")

		for row in rd:
			try:
				tempTuple = (row[Ligand_Name], row[SMILES],row[InChIKey],row[target_name],row[target_organism],
					row[target_source_organism],row[chembl_id],row[uniprot_id])
				c.execute("INSERT INTO BindingDB VALUES (?,?,?,?,?,?,?,?)", tempTuple)
			except:
				print(row[Ligand_Name])
	conn.commit()
	conn.close()	

def extract_compound(transporterName):
	conn = sqlite3.connect('bindingdb.db')
	c = conn.cursor()
	query = "select Ligand_Name, SMILES, InChIKey, chembl_id from BindingDB \
			where target_name = '{0}';".format(transporterName)
	result = c.execute(query).fetchall()

	transporterName = transporterName.replace(" ","_")
	transporterName = transporterName.replace("/","_")

	csv_file = open("Extracted_"+transporterName+".csv", "w",newline='')
	csv_writer = csv.writer(csv_file,quoting=csv.QUOTE_ALL)
	for i in result:
		csv_writer.writerow(list(i))

	csv_file.close()



def main():
	current_dir = os.getcwd()
	my_file = current_dir+"/bindingdb.db"
	if os.path.isfile(my_file):
		print("File EXISTS.......")

	else:
		create_db()


	# if sys.argv[1]:
	# 	arg_len = len(sys.argv)
	# 	last_arg = arg_len - 1
	# 	transporterName = ""
	# 	for arg in range(1,last_arg):
	# 		transporterName = transporterName + sys.argv[arg] + " "
	# 	transporterName = transporterName+sys.argv[last_arg]
	# 	extract_compound(transporterName)

	# else:
	# 	print("Put the transporter name for extraction!")

	




			
	





if __name__ == "__main__":
	main()