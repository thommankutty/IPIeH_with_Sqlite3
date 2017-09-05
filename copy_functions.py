import shutil
import os
import json
from shutil import copyfile

#list for running through the folders in the directory
pp_list = ['PP01', 'PP02', 'PP03', 'PP04', 'PP05', 'PP06', 'PP07', 'PP08', 'PP09', 'PP10', 'PP11', 'PP12', 'PP13',
	           'PP14', 'PP15', 'PP16']

#creates folder if directory does not exist
def create_Folder_If_Not_Exist(destination_path):
	if not os.path.exists(destination_path):
		os.makedirs(destination_path)
		print("directory not found; directory is created for "+destination_path)

#copies file from Source folder to result folder
def copy_Files_From_Source(path,destination):

	for i in range(len(pp_list)):
		counter = 0
		# creates the folder path for source file
		folder_path = os.path.join(path,pp_list[i])
		# creates the folder path for destination files
		destination_path = os.path.join(destination,pp_list[i])
		create_Folder_If_Not_Exist(destination_path)

		for root,dirs,files in os.walk(folder_path):
			for file in files:
				if file.endswith(".day"):

					variable_path = os.path.join(root, file)
					shutil.copy(variable_path,destination_path)

					counter += 1
		print(str(counter) + " files copied to " +destination_path )

