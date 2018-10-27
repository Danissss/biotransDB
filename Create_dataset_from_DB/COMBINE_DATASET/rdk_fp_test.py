from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols






ms = [Chem.MolFromSmiles('CCOC'), Chem.MolFromSmiles('CCO'),Chem.MolFromSmiles('COC')]
fps = [FingerprintMols.FingerprintMol(x) for x in ms]

for i in fps:
	# print the fingerprint 
	print(i)


# print the similarity score 
print(DataStructs.FingerprintSimilarity(fps[0],fps[1]))