#Combine Multiple Excel Worksheets Into a Single Pandas Dataframe 
df = pd.concat(pd.read_excel('faillissement_database.xlsx', sheet_name=None), ignore_index=True)
