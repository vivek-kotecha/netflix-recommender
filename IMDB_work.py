###################################################################
"""python module to work with IMDB Data Files """
###################################################################

# Import libraries
import numpy as np
import pandas as pd

import os
import re
import string

# Set-up directory and Files
# imdb_dir = os.getcwd() + "\\IMDB_Dataset\\"
# imdb_file_names = ["title_akas.tsv", "title_basics.tsv", "title_crew.tsv", "title_principals.tsv", "name_basics.tsv"]

imdb_dir = None

def read_imdb_files(file_name, file_directory = imdb_dir):
    """
Function to read the ".tsv" files downloaded from IMDB interface
----------------------------------------------------------------
Name: read_imdb_files

Parameters: 
- file_name: name of the IMDB dataset file. 
- file_directory: name of the directory that contains the IMDB dataset files. Parameter has been set to default option.

Returns: a dataframe containing all the records of the IMDB dataset file with every column stored as "object" dtype

Additional Info: 
- all the fields are stored as object dtype to avoid any errors 
- prints the shape and missing value % for the datafile
    """
    
    df = pd.read_csv(file_directory + file_name, delimiter = "\t", dtype = "object", na_values = "\\N")
    null_count = pd.Series((df.isnull().sum()/ df.shape[0]).mul(100).round(2))
    null_df = pd.DataFrame({"ColumnName" : null_count.index, "MissingValue%" : null_count.values})
    
    print("The data file {f} contains {r} rows and {c} columns".format(f = file_name, r = df.shape[0], c = df.shape[1]),
          "=".rjust(60, "="), 
          null_df, sep = "\n")
    return df