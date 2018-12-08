import os
import sys
import csv
from bindingDB import extract_compound


current_list = [
	"ATP-binding cassette sub-family G member 2",
	"Canalicular multispecific organic anion transporter 1",
	"Canalicular multispecific organic anion transporter 2",
	"Multidrug resistance-associated protein 2 (MRP2)",
	"Multidrug and toxin extrusion protein 1",
	"Multidrug and toxin extrusion protein 2",
	"Multidrug resistance-associated protein 4",
	"Multidrug resistance-associated protein 5",
	"Solute carrier family 15 member 1",
	"Solute carrier family 15 member 2",
	"Solute carrier family 22 member 1",
	"Solute carrier family 22 member 2",
	"Solute carrier family 22 member 5",
	"Solute carrier family 22 member 6",
	"Solute carrier family 22 member 7",
	"Solute carrier family 22 member 8",
	"Solute carrier family 22 member 11",
	"Solute carrier family 22 member 12",

	"Solute carrier organic anion transporter family member 1A2",
	"Solute carrier organic anion transporter family member 1B1 (OATP1B1)",
	"Solute carrier organic anion transporter family member 1B3 (OATP1B3)",
	"Solute carrier organic anion transporter family member 2A1",
	"Solute carrier organic anion transporter family member 2B1",

	"Multidrug Resistance Transporter MDR 1",
	"MDR1",

	"P-glycoprotein 1 (Pgp/MDR1)"]



def main():
	for i in current_list:
		extract_compound(i)





if __name__ == '__main__':
	main()