# various-code-blocks

# Table reorientation
The code imports the pandas library and creates a dataframe containing information about research grant applications. The data includes the application number, applicant, gender, title of the research, and keywords associated with the research. The data is then grouped by the application number, applicant, gender, and title, and the keywords are aggregated and joined together with commas. The resulting data is stored in a new dataframe called df_pv2. The head of the original dataframe and the new dataframe are displayed.

# Visualisaing and rendering of entity recognizer
This script demonstrates how to use the displacy visualization module from spacy to display named entity recognition (NER) in a web interface. 
## Prerequisites

Install the spacy library: pip install spacy

Download and load a pre-trained NER model: nlp = spacy.load("your_ner_model")

## Usage

  Set the text to be processed by the NER model in the doc1 variable.

  Run the script: python main.py

  Open the displayed URL in your browser to view the NER visualization.

## Dependency plot
This code generates a dependency plot of a given document using the displacy library.

To use this code, you must first import the displacy library and create a document object. Then, you can use the render() function to generate the dependency plot, passing in the document object and specifying the desired style as "dep".

The resulting plot is saved to a file at the specified output path, in this case "/home/gebruiker/Documenten/dependency_plot.svg". The file is opened in write mode and encoded in utf-8 to ensure proper formatting and character representation.

This dependency plot can be useful for analyzing the grammatical structure of a document and understanding the relationships between words and phrases.

# Combine Multiple Text Files Into One Text File Using Python
This code contains three methods for combining multiple text files into a single text file using Python.

## Method 1

This method uses the glob and os modules to search for all .txt files in a specified directory. It then combines these files into a new file called all_combined.txt.

## Method 2

This method uses the glob module to search for all .txt files in a specified directory, and the pd.concat() function from the pandas module to combine the contents of these files into a single pandas dataframe called df_RL1.

## Method 3

This method uses the glob module to search for all .TXT files in the current directory. It then opens each file and adds its contents to a new file called allstates.txt. The first line of allstates.txt is a header row with the columns state, sex, year, name, and count.

# Combine Multiple Excel Worksheets Into a Single Pandas Dataframe
This code is used to combine multiple excel worksheets into a single pandas dataframe. It does this by using the pd.concat() function from the pandas library to read in the excel file faillissement_database.xlsx and combining all of the worksheets within the file into a single dataframe. The ignore_index parameter is set to True, which means that the index values of the original worksheets will be ignored and the final dataframe will be given a new index starting at 0.

To use this code, you will need to have the pandas library installed and the file faillissement_database.xlsx in the same directory as your script. You may need to adjust the file path if the file is located elsewhere.

# Anonymisation with Hashlib
This code uses the pandas module to import and work with data stored in an Excel file. It also uses the hashlib module to anonymise a specific column in the data.

To use this code, replace "yourdata.xlsx" with the file path for your Excel file and "columns_name" with the name of the column you want to anonymise.

The code first imports the pandas module and uses it to import the data from the Excel file. It then displays the first two rows of the dataframe to allow for crosschecking.

Next, the code converts the data in the specified column to strings and then uses the hashlib module to apply a sha256 hash to each value in the column. The resulting hash is then displayed in the dataframe.

This code can be useful for protecting sensitive information in your data while still allowing for analysis.

# Example of seaborn image
This code generates a bar chart showing the combination of disciplines submitted by applicants during a funding round. The interaction between technical science and other disciplines from various domains is shown as an example. This graph helps to answer the question of whether there are certain disciplines that perform particularly well in a particular subsidy round.

## Dependencies
This code requires the following packages:matplotlib, seaborn

## How to Use
The code can be run as is, but it requires a dataframe called df_305 to be defined. This dataframe should have the following columns:

  Discipline: the discipline of the applicant
  
  Disciplines: the combination of disciplines the applicant has submitted
  
  Value: the value of the applicant's submission
  
  Attribute: the attribute of the applicant's submission
  
  Domain: the domain the applicant's submission belongs to
  
Once df_305 has been defined, running the code will produce a bar chart showing the interaction of technical science with other disciplines in different domains. The x-axis represents the combination of disciplines, the y-axis represents the value of the submission, and the bars are grouped by the attribute of the submission. The chart is split into rows by domain, and each row is labeled with the corresponding domain. The x-axis tick labels are rotated 45 degrees and aligned to the right for readability. The legend for the attribute is shown in the first row of the chart. The x- and y-axis labels are removed and the title of the chart is set to "Interaction of discipline Technical science with other sciences". The top of the chart is adjusted for aesthetic purposes.

# Sql pandas connection
This code is used to generate a SQL query and retrieve data from a database using pyodbc and pandas. The first part of the query is defined as query_code and the second part is defined as Sub_Naam. These two parts are then combined using string concatenation to create the full query, which is stored in the query variable.

The necessary modules, pandas and pyodbc, are imported at the beginning of the code. Then, a connection to the SQL Server is established using the pyodbc.connect() function, providing the necessary connection details.

The data is then retrieved using the pd.read_sql_query() function, which executes the query on the specified connection and stores the results in a Pandas dataframe. The columns of this dataframe are then printed.

# Extracting Information from a Website and Wikipedia Tables
This script contains two methods for extracting information from the web.

## Method 1: BeautifulSoup

The first method uses the BeautifulSoup library to parse HTML and extract all text elements from a webpage specified by the url variable. It then filters out unwanted elements specified in the blacklist variable, and stores the remaining text in the output variable.

In other words: this code is using the Python requests library to fetch the HTML content of a webpage, specified by the url variable. It then uses the BeautifulSoup library to parse the HTML and extract all text elements. The output variable is used to store all the text elements that are not in the blacklist list. The blacklist is a list of HTML elements that the code is instructed to ignore. The final step is to print the output variable, which should contain all the text from the webpage that was not ignored. 

## Method 2: read_html

The second method uses the read_html function from the pandas.io.html library to extract tables from a Wikipedia page specified by the page variable. It stores the resulting list of tables in the wikitables variable and prints the number of tables extracted.

## Dependencies

requests library for sending HTTP requests

bs4 (BeautifulSoup) library for parsing HTML

pandas library for working with tables

## Usage
To use these methods, modify the values of the url and page variables to point to the desired webpages. You may also need to modify the blacklist variable to include any additional elements you wish to exclude from the output variable in method 1.
