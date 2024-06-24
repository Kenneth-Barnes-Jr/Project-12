--- Foundation ---

import os

# This is path of my Working Directory
Project_Directory= "Directory path"

# Initialize an empty list to store file information
file_info_list = []

# Walk through the directory and collect file information
for root, _, files in os.walk(Project_Directory):
    for filename in files:
        file_path = os.path.join(root, filename) 
        file_size = os.path.getsize(file_path)  # This line will pull the info of the files "file_size"
        file_info = {'path': file_path, 'size': file_size} # This will combine both, the "file path" and "file size"
        file_info_list.append(file_info)

# Print the list of dictionaries
for file_info in file_info_list:
    print(f"{{'path': '{file_info['path']}', 'size': {file_info['size']}}}")


--- Advanced ---

import os

# The start of my function to extract data from the current working directory
def ADVANCED (Project_Directory=None ):

    # This is the path of my Working Directory
    Project_Directory= "Directory path"
    
    if Project_Directory is None:
        Project_Directory = os.getcwd()
       
    # Initialize an empty list to store file information
    DataBase = []

    # Walk through the directory and collect file information
    for root, _, files in os.walk(Project_Directory):
        for filename in files:
            file_path = os.path.join(root, filename) 
            file_size = os.path.getsize(file_path)  # This line will pull the info of the files "file_size"
            Data = {'path': file_path, 'size': file_size} # This will combine both, the "file path" and "file size"
            DataBase.append(Data)
    
    return DataBase

# This is the path of my Working Directory
Project_Directory= "Directory path"
DataBase = ADVANCED(Project_Directory)

# Print the list of dictionaries
for Data in DataBase:
    print(f"{{'path': '{Data['path']}', 'size': {Data['size']}}}")
