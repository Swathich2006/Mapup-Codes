import pandas as pd

def check_timestamps(dataframe):
    # Convert the 'timestamp' column to datetime format
    dataframe['timestamp'] = pd.to_datetime(dataframe['timestamp'])
    
    # Group by 'id' and 'id_2' and check if timestamps are in the correct order
    incorrect_timestamps = dataframe.groupby(['id', 'id_2'])['timestamp'].apply(lambda x: x.diff().dt.total_seconds() < 0).fillna(False)
    
    return incorrect_timestamps

df = pd.read_csv("C:\Downloads\dataset-2.csv")

# Call the function with the DataFrame
result_series = check_timestamps(df)

# Print the boolean series with a multi-index
print(result_series)
