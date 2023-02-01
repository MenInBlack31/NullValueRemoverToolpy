# NullValueRemoverToolpy
usage: null_val_remover.py [-h] -p  [-n | -q]

For data preprocessing, This tool can be used to remove Null values (NaN values) from a CSV file. It removes
the entire row of the null value section. Data Preprocessing plays an important role in Machine Learning
etc. Not all datasets are formatted properly for building machine learning models, some datasets contain
NULL sets. To fix this, we can either add the average value of the entire column to those Null values (NaN
sets), or we can remove those Null rows. Therefore, I developed a simple Python tool to eliminate those NULL
values and empty values from a CSV file . Hope this tool will help you . Have a great day :)

options:
  -h, --help    show this help message and exit
  -p , --path   Path of the file (if it is in pwd then enter name.csv ,if not enter full file path)
  -n, --normal  If enabled it will show all progress
  -q, --quiet   If enabled the program will not return any progress info but it will be executed
.
.
.
(IN FUTURE) Will update this tool to fill missing values using linear method (mean values) In FUTURE . 
.
.
.
.
.
Have a great day :)
