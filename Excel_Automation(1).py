# Import Python Modules
# Pandas (data analysis)
import pandas as pd
# Numpy (matrices & arrays)
import numpy as np
# Matplotlib (plot graph)
import matplotlib.pyplot as plt

# Name of Excel Workbooks (assign a variable to the file paths of the excel workbooks)
#excel_file_1 = "Paste File Path Here"
#excel_file_2 = 'Paste File Path Here' 

# Read Excel Files
#df1 = pd.read_excel(excel_file_1, sheet_name = "First", engine='openpyxl')  
#df2 = pd.read_excel(excel_file_1, sheet_name = "Second", engine = 'openpyxl')
#df3 = pd.read_excel(excel_file_2, engine='openpyxl')  # default is read first sheet in the excel file

# View Data Frame
#print(df1) 

# View One Column's Values
#print(df1["Paste One Column Title From df1 Excel File Here"]) 

# Combining Data From Different Excel Workbooks
#df_all = pd.concat([df1,df2,df3], axis=1)
#print(df_all)

# Organize Data (column names given as an example)
#pivot = df_all.groupby(["Column 1"]).mean()
#test = pivot.loc[:,"Column 2":"Column 3"] 
#print(test) # prints out average of column titled "Column 1" from lowest to highest, and all the columns between "Column 2" to "Column 3"

# Graphing
#test.plot(kind="bar") # create bar graph
#plt.show()

# Output Data to New Excel Workbook (We want df_all in one single excel file)
#df_all.to_excel("Paste Desired File Path Here For This New Excel File")