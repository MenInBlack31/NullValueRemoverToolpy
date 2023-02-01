import pandas as pd
import argparse
parser = argparse.ArgumentParser(description='For data preprocessing, This tool can be used to remove Null values (NaN values) from a CSV file. It removes the entire row of the null value section. Data Preprocessing plays an important role in Machine Learning etc. Not all datasets are formatted properly for building machine learning models, some datasets contain NULL sets. To fix this, we can either add the average value of the entire column to those Null values (NaN sets), or we can remove those Null rows.\n Therefore, I developed a simple Python tool to eliminate those NULL values and empty values from a CSV file\n. Hope this tool will help you \n\n. Have a great day :)' )
parser.add_argument('-p','--path',type=str,metavar='',required=True, help='Path of the file (if it is in pwd then enter name.csv ,if not enter full file path)')
group = parser.add_mutually_exclusive_group()
group.add_argument('-n','--normal', action='store_true',help='If enabled it will show all progress')
group.add_argument('-q','--quiet', action='store_true',help='If enabled the program will not return any progress info but it will be executed')
args=parser.parse_args()
path = args.path

if args.normal:
        data = pd.read_csv(path)
        stat = data.isnull().sum()
        print("Before Removing")
        print(stat)
        print(data.shape)
        print("----------------------")
        datafile = data.dropna()
        print("After Removing")
        print(datafile)
        print(datafile.shape)
        print("----------------------")
        save_name = input("Enter a new name for the file(With the required file extension):")
        datafile.to_csv(save_name)
        print("Filesaved as",save_name)
if args.quiet:
        data = pd.read_csv(path)  
        stat = data.isnull().sum()
        datafile = data.dropna()
        save_name = input("Enter a new name for the file(With the required file extension)")
        datafile.to_csv(save_name)
        print("File name saved as",save_name)
else:
        print("Choose either Normal mode(-n) or Quiet mode(-q). For further more details use --help or -h")
#Customly made by Taruukrishna 
#Have a great day
