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
