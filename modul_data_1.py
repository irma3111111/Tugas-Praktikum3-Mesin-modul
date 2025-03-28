import pandas as pd

# Load the Excel file
df = pd.read_excel('data1.xlsx', sheet_name='data')

# Function to classify data types
def classify_data_types(df):
    data_types = {}
    for column in df.columns:
        if df[column].dtype == 'object':
            # Nominal data: categorical data without any order
            data_types[column] = 'Nominal'
        elif df[column].dtype in ['int64', 'float64']:
            # Check if the data is discrete or continuous
            if len(df[column].unique()) < 20:
                # Ordinal data: categorical data with a meaningful order but no consistent difference between categories
                data_types[column] = 'Ordinal'
            else:
                # Ratio data: continuous data with a true zero point
                data_types[column] = 'Ratio'
        else:
            # Default to interval if not clearly nominal, ordinal, or ratio
            data_types[column] = 'Interval'
    return data_types

# Classify the data types
data_types = classify_data_types(df)

# Print the classified data types
print(data_types)