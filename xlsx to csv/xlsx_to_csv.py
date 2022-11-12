# pip install openpyxl
import os
import pandas as pd

# path in which you have downloaded your xlsx file and created your python code file
loc = "C:\\Users\\patel\\OneDrive\\Desktop\\Python\\Python\\xlsx to csv"
files = os.listdir(loc)

for f in files:
    if f.endswith(".xlsx"):
        folder_name = f.split(".")[0]
        # print(folder_name)
        xlfile = pd.ExcelFile(f)
        sheets = xlfile.sheet_names
        # print(sheets)

        folder = './'+folder_name+'/'
        # will create a folder with same name as xlsx file name
        os.makedirs(folder)
        for sheet in sheets:
                sheet_data = xlfile.parse(sheet)
                # print(sheet_data)
                sheet_data.to_csv(os.path.join(folder, sheet+".csv"),index=False)

