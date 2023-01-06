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

# Combine textfiles


# Combining jupyter notebooks

# Data anonimisation

# Sql pandas connection

# Web scrapping

# Use of google key to get lattitudes and longitudes

# Example of seaborn image

# Combine Multiple Excel Worksheets Into a Single Pandas Dataframe 
