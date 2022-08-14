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
