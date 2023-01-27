#import module
import pandas as pd

#import data
df = pd.read_excel("yourdata.xlsx")
#crosscheck the dataframe
df.head(2)

#convert the data of the column you want to anonymise into strings
df['columns_name']=df['columns_name'].astype(str)

#anonymise with hashlib
import hashlib
df['columns_name']=df['columns_name'].apply(lambda x:hashlib.sha256(x.encode()).hexdigest())

#Analysis by chatGPT
#You can move the import statements for the pandas and hashlib modules to the top of your code to make it more readable.

#Instead of hardcoding the file name in the pd.read_excel() function, you can use a variable to store the file name and pass it to the function. This will make it easier to switch between different files without having to change the code.

#It is also a good practice to add comments to your code explaining what it does, especially if the code is complex or if it will be used by other people.

#To make it more secure, you can use a salt value before hashing.

#You can consider using a library like Faker to generate fake data in place of actual data.

#It could be useful to add some validation to check that the file exists and is in the correct format before trying to read it.

# With these suggestions your code would look like:
import pandas as pd
import hashlib
from os.path import isfile

file = "yourdata.xlsx"
if isfile(file):
    df = pd.read_excel(file)
else:
    raise ValueError(f"{file} not found.")

df.head(2)

#convert the data of the column you want to anonymise into strings
df['columns_name']=df['columns_name'].astype(str)

#anonymise with hashlib
salt = b'your_salt_value' # a random value
df['columns_name']=df['columns_name'].apply(lambda x: hashlib.sha256(salt + x.encode()).hexdigest())
