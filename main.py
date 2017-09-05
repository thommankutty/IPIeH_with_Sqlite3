from copy_functions import copy_Files_From_Source,create_Folder_If_Not_Exist
from data_functions import *
from excel_functions import *
import time


#####################################################################################
# locate files from the folder and copy to the new folder

raw_path = r'C:\Users\Sree\Desktop\WORK\Automated Reports\NewVersionrawData'
path = raw_path
raw_destination = r'C:\Users\Sree\Desktop\WORK\Automated Reports\NewVersion\resultFolder'
finalData = r'C:\Users\Sree\Desktop\WORK\Automated Reports\NewVersion\finalData'
excel_files_destination = r"C:\Users\Sree\Desktop\WORK\Automated Reports\NewVersion\excelFiles"
#####################################################################################

create_Folder_If_Not_Exist(raw_destination)
create_Folder_If_Not_Exist(finalData)
create_Folder_If_Not_Exist(excel_files_destination)

print("sleep for 4 seconds")
print("---------------------------------------------")
time.sleep(4)

copy_Files_From_Source(raw_path,raw_destination)

#list for running through the folders in the directory
pp_list = ['PP01', 'PP02', 'PP03', 'PP04', 'PP05', 'PP06', 'PP07', 'PP08', 'PP09', 'PP10', 'PP11', 'PP12', 'PP13',
	           'PP14', 'PP15', 'PP16']
#####################################################################################

# copy files to the new source
copy_Files_From_Source(raw_path,raw_destination)
# create folder if doesnt exist
# create_Folder_If_Not_Exist(excel_files_destination)

new_main_function(pp_list,raw_destination,excel_files_destination)

print("pausing for 5 seconds")
time.sleep(5)

defects_to_dataframe(excel_files_destination,finalData)





