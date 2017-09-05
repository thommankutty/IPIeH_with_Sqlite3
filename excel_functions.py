import os
import re                 #regular expressions
import glob
import string
import pandas as pd
import numpy as np
import csv
import xlsxwriter


def get_defects(file):
	csv_file = pd.read_csv(file)
	df = pd.DataFrame(csv_file)

	defect_list = list(df)[4:]

	empty_dic = {}
	for i in defect_list:
		empty_dic[i] = df[i].sum()

	return empty_dic


def defects_to_dataframe(path,destination_path):
	os.chdir(path)

	final_destination_path = os.path.join(destination_path, "defects_stats.csv")

	file_list = os.listdir(os.getcwd())

	defect_dict = {}

	for file in file_list:
		defect_dict[file.split('.')[0]] = get_defects(file)

	df_1 = pd.DataFrame(defect_dict)

	df_1.to_csv(final_destination_path)
	print("========================================================")
	print("========================================================")
	print("========================================================")
	print("The defects data file has been created at  "+ destination_path)
	return df_1