

import os
import re                 #regular expressions
import glob
import string
import pandas as pd       #pandas
import numpy as np
import csv
import xlsxwriter



def string_search(string_search, line, dict_name, date):
	"""
	**only valid for integers
	REQUIRED FIELDS:
	- string search = the string to be searched, example "Units Inspected"
	- dict name     = the name of the dictionary to store the data into, must be an empty dictionary
	- date          = date of the file, extracted by splitting the file name and taking out the first part
	NOT REQUIRED
	- line          = each line of the file, leave as is
	"""
	searchObj = re.search(string_search, line)
	if searchObj:
		number = re.search(r"((\d+)(\s+))", line)
		dict_name[date] = number.group(1)


def yield_search(string_search, line, dict_name, date):
	"""
	**only valid for floats
	REQUIRED FIELDS:
	- string search = the string to be searched, example "Units Yield"
	- dict name     = the name of the dictionary to store the data into, must be an empty dictionary
	- date          = date of the file, extracted by splitting the file name and taking out the first part
	NOT REQUIRED
	- line          = each line of the file, leave as is
	"""
	searchObj = re.search(string_search, line)
	if searchObj:
		#dict_name[date] = number.group(1).strip()
		number = re.search(r"(\d+\.\d+)", line)
		dict_name[date] = number.group(1).strip()


def get_final_csv(excel_file_name, current_dir):
	"""

	REQUIRED FIELDS:

	- excel_file_name : name of the excel file
	- current_dir     : the source directory from which the files are pulled.
	"""
	units_inspected = {}
	units_passed = {}
	units_yield = {}
	nc_dict = {}
	spot_dict = {}
	tear_dict = {}
	gap_dict = {}
	nolens_dict = {}
	nosaline_dict = {}
	innertear_dict = {}

	os.chdir(current_dir)
	file_list = os.listdir(current_dir)

	for file in file_list:

		if file.endswith(".day"):

			date = file.split(".")[0]

			with open(file) as f:
				for line in f:
					string_search("Units Inspected", line, units_inspected, date)

					string_search("Units Inspected", line, units_inspected, date)
					string_search("Units Passed", line, units_passed, date)
					yield_search("Units Yield", line, units_yield, date)
					string_search("Non-Circular", line, nc_dict, date)
					string_search("Spot", line, spot_dict, date)
					string_search("Tear Lens", line, tear_dict, date)
					string_search("Gap Lens", line, gap_dict, date)
					string_search("No Lens", line, nolens_dict, date)
					string_search("No Saline", line, nosaline_dict, date)
					string_search("Inner Tear", line, innertear_dict, date)

	series_total_inspected = pd.Series(units_inspected)
	series_total_passed = pd.Series(units_passed)
	series_total_yield = pd.Series(units_yield)
	series_total_nc = pd.Series(nc_dict)
	series_total_spot = pd.Series(spot_dict)
	series_total_tear = pd.Series(tear_dict)
	series_total_gap = pd.Series(gap_dict)
	series_total_nolens = pd.Series(nolens_dict)
	series_total_nosaline = pd.Series(nosaline_dict)
	series_total_innertear = pd.Series(innertear_dict)

	# print(series_total_inspected)

	df_total_inspected = pd.DataFrame(series_total_inspected)
	df_total_passed = pd.DataFrame(series_total_passed)
	df_total_yield = pd.DataFrame(series_total_yield)
	df_total_nc = pd.DataFrame(series_total_nc)
	df_total_spot = pd.DataFrame(series_total_spot)
	df_total_tear = pd.DataFrame(series_total_tear)
	df_total_gap = pd.DataFrame(series_total_gap)
	df_total_nolens = pd.DataFrame(series_total_nolens)
	df_total_nosaline = pd.DataFrame(series_total_nosaline)
	df_total_innertear = pd.DataFrame(series_total_innertear)

	new_df = pd.concat([df_total_inspected,
	                    df_total_passed,
	                    df_total_yield,
	                    df_total_nc,
	                    df_total_spot,
	                    df_total_tear,
	                    df_total_gap,
	                    df_total_nolens,
	                    df_total_nosaline,
	                    df_total_innertear], axis=1)

	new_df.columns = ["Units Inspected",
	                  "Units Passed",
	                  "Units Yield",
	                  "Non Circular",
	                  "Spot",
	                  "Tear",
	                  "Gap",
	                  "No Lens",
	                  "No Saline",
	                  "Inner Tear"]

	# print(new_df)

	# print("the total inspected is : ", series_total_inspected.sum())
	new_df.to_csv(excel_file_name)


def os_path(path):
	empty_list = []
	for root,dirs,files in os.walk(path):
		empty_list.append(root)
	return empty_list


def main_function(path, new_path):

		"""
		returns the information on main_function
		"""
		file_path = os_path(path)
		file_path = file_path[1:]

		for file in file_path:
			file_name_raw = (file.split(path + "\\"))[1]
			excel_file_name_pre = str(file_name_raw) + ".csv"

			excel_file_name = os.path.join(new_path, excel_file_name_pre)



			get_final_csv(excel_file_name, file)

			print(excel_file_name_pre + " is created at " + excel_file_name)


def new_main_function(pp_list, raw_destination,excel_files_destination):
	for i in range(len(pp_list)):

		file_name = pp_list[i]
		file_name_with_csv = file_name +'.csv'
		file_name_with_csv_root = os.path.join(excel_files_destination,file_name_with_csv)

		folder_path = os.path.join(raw_destination, pp_list[i])

		get_final_csv(file_name_with_csv_root,folder_path)

		print("The "+pp_list[i]+' excel file has been created ')