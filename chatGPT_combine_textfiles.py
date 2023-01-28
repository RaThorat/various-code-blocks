# combine multiple text files into one text file using python
#method 1
import glob
import os
os.getcwd()

files_path = '/Users/Documents/Python_scripts/Nieuwe map' # use your path
all_files = glob.glob(os.path.join(files_path, "*.txt"))

file_big = 'all_combined.txt'
with open(file_big, 'wb') as fnew:
    for f in all_files:
        with open(f, 'rb') as fold:
            for line in fold:
                fnew.write(line)
                fnew.write("\n".encode(encoding='utf_8'))
#method 2
import glob
files_path = '/Users/Documents/Python_scripts/datasets_for_NLP' # use your path
all_files = glob.glob(os.path.join(files_path, "*.txt"))
df_RL1 = pd.concat((pd.read_csv(f) for f in all_files))

#method 3
from glob import glob
output = open("allstates.txt", "w")
output.write("state,sex,year,name,count\n")
for fname in glob("*.TXT"):
    print("Adding", fname)
    f = open(fname)
    output.write(f.read())
    f.close()
output.close()

#The code provided combines multiple text files into one text file using three different methods. Here are a few suggestions to improve the code:

#Use more descriptive variable names: Instead of using generic variable names such as file_big, df_RL1, and output, consider using more descriptive variable names that explain the purpose of the variable.

#Use consistent file extension: Instead of using different file extensions in the different methods, consider using a consistent file extension for all the text files.

#Add error handling: The code doesn't include any error handling to handle cases where the text files are not found or are in a different format. It's a good idea to add error handling to the code to handle these cases.

#Use pathlib module: Instead of using os.path.join() method, consider using the pathlib module to join the paths. This is more pythonic and more readable.

#Here's an example of the updated code using method 1:

from pathlib import Path

files_path = Path('/Users/Documents/Python_scripts/Nieuwe_map') # use your path
all_files = files_path.glob('*.txt')

combined_file = files_path / 'all_combined.txt'
with open(combined_file, 'w') as outfile:
    for file in all_files:
        try:
            with open(file, 'r') as infile:
                outfile.write(infile.read())
                outfile.write("\n")
        except Exception as e:
            print(f"Error reading file {file}: {e}")
 
#This updated code uses more descriptive variable names, consistent file extension, error handling and pathlib module to make the code more readable and maintainable.
