import csv
import sys
import os
from rdkit import Chem
from rdkit.Chem import Descriptors3D
from rdkit.Chem import AllChem


## mol: rdkit molecule object
## descriptor: type of descriptor in rdkit; default=molecular
##
def generate_descriptors(mol,descriptor="molecular"):
	descriptors_value = []
	if descriptor 	== "molecular":
		# rdkit.Chem.Descriptors3D module
		# https://www.rdkit.org/docs/source/rdkit.Chem.Descriptors3D.html#module-rdkit.Chem.Descriptors3D
		a = Descriptors3D.Asphericity(mol)				# molecular asphericity
		print(a)
		descriptors_value.append(a)
		# descriptors_value.append(Descriptors3D.Eccentricity(mol))
		a = Descriptors3D.Eccentricity(mol)				# molecular eccentricity
		a = Descriptors3D.InertialShapeFactor			# Inertial shape factor
		a = Descriptors3D.NPR1							# Normalized principal moments ratio 1 (=I1/I3)
		a = Descriptors3D.NPR2							# Normalized principal moments ratio 2 (=I2/I3)
		a = Descriptors3D.PMI1							# First (largest) principal moment of inertia
		a = Descriptors3D.PMI2							# Second (largest) principal moment of inertia
		a = Descriptors3D.PMI3							# Third (largest) principal moment of inertia
		a =	Descriptors3D.RadiusOfGyration				# Radius of gyration
		a = Descriptors3D.SpherocityIndex				# Molecular spherocityIndex
		# rdkit.Chem.Descriptors module
		# https://www.rdkit.org/docs/source/rdkit.Chem.Descriptors.html#module-rdkit.Chem.Descriptors

	elif descriptor == "atomic":
		return None



	elif descriptor == "fingerprint":
		return None

	else:
		print("no such descriptor in RDKit".upper())
		print("AVAILABLE DESCRIPTORS: molecular; atomic; fingerprint;")
		sys.exit(0)

	return descriptors_value

def generate_molecular_descriptor_csv(file_name):
	# checked_file = open("final_with_other_dataset.csv","w",newline='')
	# csv_writer_checked = csv.writer(checked_file,quoting=csv.QUOTE_ALL)
	datafile 			= open(file_name,"r",newline='')
	datafile_csv_reader = csv.reader(datafile,quoting=csv.QUOTE_ALL)

	training_data_file  = open(file_name.split(".")[0]+"training.csv", "w",newline='')
	training_csv	    = csv.writer(training_data_file,quoting=csv.QUOTE_ALL)

	# Generating the descriptor by given types 
	for row in datafile_csv_reader:
		SMILES = row[1]
		mol = Chem.MolFromSmiles(SMILES)
		mol = Chem.AddHs(mol)
		AllChem.EmbedMolecule(mol)       # add 3D coordinates by embedding the molecule (this uses the ETKDG method
		AllChem.UFFOptimizeMolecule(mol) # uses UFF to optimize a molecule’s structure
		descriptors = generate_descriptors(mol)
		sys.exit(0)
	return None










def main():

	sample_file = "/Users/xuan/Desktop/biotransDB/Xuan_ml_package/Xuan_learner/Sample_data.csv"
	generate_molecular_descriptor_csv(sample_file)
	print("molecular descriptor generated!".upper())




if __name__ == '__main__':
	main()