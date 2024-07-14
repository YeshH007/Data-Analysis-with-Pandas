import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    # Remove rows with missing values
    df.dropna(inplace=True)
    return df

def analyze_data(df):
    # Calculate the mean of a specific column
    mean_value = df['column_name'].mean()
    return mean_value

def filter_data(df):
    # Filter rows based on a condition
    return df[df['column_name'] > 100]

def display_data(df):
    print(df.head())

file_path = 'data.csv'
data = load_data(file_path)
cleaned_data = clean_data(data)
mean_value = analyze_data(cleaned_data)
filtered_data = filter_data(cleaned_data)
display_data(filtered_data)
print(f"Mean value: {mean_value}")
