#part 1 of query
query_code='your query Ronde_Naam like'
#part of two of query
Sub_Naam='\'%round name 2021%\''
#connecting two parts of query
query=query_code+' '+Sub_Naam
print(query)

#importing necessary modules
import pandas as pd
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server= server_name;'
                      'Database=datawarehouse_name;'
                      'Trusted_Connection=yes;')
#Dim_PP_Aanvraag
#dimensions are groups of attributes based on columns from tables or views in a data source view.
df = pd.read_sql_query(query, conn)

df.columns
