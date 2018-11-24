import os
import sys
import csv










def main():

	complete_data_file = "/Users/xuan/Desktop/Phase_2_data_clean_up/PhaseIISubstratesVsNonSubstrates_whole_set.csv"
	filled_data_file = "/Users/xuan/Desktop/Phase_2_data_clean_up/PhaseIISubstratesVsNonSubstrates_structure_filled.csv"

	result_file = "/Users/xuan/Desktop/Phase_2_data_clean_up/unfilled.csv"
	csv_file = open(complete_data_file,'r', newline='')
	complete_data_csv = csv.reader(csv_file, delimiter=',')
	csv_file_filled = open(filled_data_file,'r', newline='')
	csv_file_filled_reader = csv.reader(csv_file_filled,delimiter=',')

	result_file_csv = open(result_file,'w',newline='')
	result_file_csv_writer = csv.writer(result_file_csv,delimiter=',')


	complete_data_csv_header = next(complete_data_csv)
	indices_enz = [i for i, x in enumerate(complete_data_csv_header) if x == "ENZ"]
	indices_ref = [i for i, x in enumerate(complete_data_csv_header) if x == "REF"]

	complete_data_csv_header_2 = next(csv_file_filled_reader)

	dataset_name = []
	dataset_name_fill = []
	dataset_ = []
	for row in complete_data_csv:
		if row[5].upper() == "YES":
			enzymes_list = []
			reference_list = []
			for enz in range(0,len(indices_enz)):
				enz_inds = indices_enz[enz]
				enzymes = row[enz_inds]
				if enzymes == "":
					continue
				else:
					enzymes = row[enz_inds]
					reference = row[enz_inds+1]
					enzymes_list.append(enzymes)
					enzymes_list.append(reference)
					# reference_list.append(reference)

			# print(enzymes_list)
			# print(reference_list)

			dataset_.append(row[0])
			dataset_.append(enzymes_list)

			dataset_name.append(dataset_)
		print(dataset_name)
		sys.exit(0)
			# print(row[0])

	for row in csv_file_filled_reader:
		
		dataset_name_fill.append(row[0])
		# print(row[0])
	# print("--")
	# for row in complete_data_csv:
	# x = set(range(10))
	# y = x - set([2, 3, 7])
	# remaining = dataset_name - set(dataset_name_fill)
	remaining = list(set(dataset_name) - set(dataset_name_fill))
	# print(remaining)
	print(len(remaining))
	for i in remaining:
		print(i)
		result_file_csv_writer.writerow([i])
	# for i in dataset_name_fill:
	# 	# print(i)
	# 	for k in dataset_name:
	# 		if i == k:
	# 			continue

	# 		else:
	# 			result_file_csv_writer.writerow([i])


	csv_file.close()
	csv_file_filled.close()
	result_file_csv.close()





if __name__ == '__main__':
	main()