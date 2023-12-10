import pandas as pd

def generate_car_matrix(dataframe):
    pivot_df = dataframe.pivot(index='id_1', columns='id_2', values='car')
    car_matrix = pivot_df.fillna(0)
    
    return car_matrix

# Read the CSV into a DataFrame
df = pd.read_csv("Downloads\dataset-1.csv")

# Call the function with the DataFrame
result_matrix = generate_car_matrix(df)