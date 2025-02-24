import pandas as pd

# Read the Excel file
file_path = r"D:\\machine learning\ML\\Excel-Sales-Template.xlsx"
dataset = pd.read_excel(file_path)

# Display first 5 rows
print(dataset.head())  
#percentage null value
# Check for missing values (percentage)
null_percentage = (dataset.isnull().sum() / dataset.shape[0]) * 100

print("\nPercentage of missing values:\n")
print(null_percentage)
dataset.fillna(10).head(10)

