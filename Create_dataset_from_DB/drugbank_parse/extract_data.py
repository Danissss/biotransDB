import sqlite3
import csv
import sys


def main():
	databaseFile = "test_drugbank.db"
	conn = sqlite3.connect(databaseFile)
	c = conn.cursor()
	try: 
		transporter_name = sys.argv[1]
		if sys.argv[1]:
			arg_len = len(sys.argv)
			last_arg = arg_len - 1
			transporterName = ""
			for arg in range(1,last_arg):
				transporterName = transporterName + sys.argv[arg] + " "
			transporterName = transporterName+sys.argv[last_arg]
			# print(transporterName)
			# sys.exit(0)
		else:
			print("Put the transporter name for extraction!")
		
	except:
		transporter_name = "Multidrug resistance protein 1"

	query = "with combined_table as (select drugbank_drug.drug_id, drugbank_drug.drug_name, drugbank_drug.drug_smiles, \
			drugbank_drug.ChEMBL_ID,drugbank_transport.drug_transport_name, actions from drugbank_drug, drugbank_transport \
			where drugbank_drug.drug_id = drugbank_transport.drug_id and drug_smiles is not null),\
			extract_table as (select drug_name, drug_smiles, drug_transport_name, actions, ChEMBL_ID from combined_table where drug_id \
			in (select drug_id from combined_table)) select * from extract_table where drug_transport_name = \
			'{0}';".format(transporterName)
	
	result = c.execute(query).fetchall()
	
	csv_file = open("Extracted_"+transporterName+".csv", "w",newline='')
	csv_writer = csv.writer(csv_file,quoting=csv.QUOTE_ALL)
	for i in result:

		csv_writer.writerow(list(i))

	csv_file.close()






if __name__ == '__main__':
	main()






