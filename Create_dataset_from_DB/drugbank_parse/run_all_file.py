import csv
import os
import sys
from extract_data import extract_all_transporter_from_drugbankid

def extract_all(transporter_list):
	for i in transporter_list:
		extract_all_transporter_from_drugbankid(i)
		


def main():
	transporter_list = ["BE0003648","BE0003667","BE0003668","BE0001061","BE0003642","BE0001004","BE0003659",
	"BE0003655","BE0001042","BE0001018","BE0003643","BE0000669","BE0001069","BE0001067","BE0001032",
	"BE0003653","BE0003647","BE0001066","BE0003646","BE0003645","BE0000879","BE0004782","BE0001018",
	"BE0001134","BE0001069","BE0001188","BE0003657","BE0004752","BE0001032","BE0000757","BE0000106",
	"BE0001061","BE0001188","BE0003640","BE0003648","BE0003647","BE0001004","BE0003659","BE0001042",
	"BE0003644","BE0003667","BE0003668","BE0001069","BE0003657","BE0001067","BE0000703","BE0001032",
	"BE0003642","BE0001042","BE0001032","BE0001067","BE0001188","BE0003639"]

	new_list = list(set(transporter_list))
	extract_all(new_list)






if __name__ == '__main__':
	main()