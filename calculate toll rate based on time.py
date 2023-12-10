import pandas as pd

# Assuming 'calculate_distance_matrix' is the function from Question 3
def calculate_distance_matrix(dataframe):
    toll_locations = pd.unique(dataframe[['toll_booth_A', 'toll_booth_B']].values.ravel('K'))
    distance_matrix = pd.DataFrame(index=toll_locations, columns=toll_locations)
    distance_matrix = distance_matrix.fillna(0)
    
    for index, row in dataframe.iterrows():
        toll_A = row['toll_booth_A']
        toll_B = row['toll_booth_B']
        distance = row['distance']
        distance_matrix.at[toll_A, toll_B] += distance
        distance_matrix.at[toll_B, toll_A] += distance
    
    return distance_matrix

def calculate_time_based_toll_rates(distance_matrix):
    # Define time intervals and corresponding toll rates
    time_intervals = {
        (0, 6): 5,     # 12:00 AM to 6:00 AM
        (6, 12): 7,    # 6:00 AM to 12:00 PM
        (12, 18): 10,  # 12:00 PM to 6:00 PM
        (18, 24): 8    # 6:00 PM to 12:00 AM
    }
    
    # Create a DataFrame for time-based toll rates
    time_based_toll_rates = pd.DataFrame(index=distance_matrix.index, columns=distance_matrix.columns)
    
    # Assign toll rates based on the time intervals
    for interval, rate in time_intervals.items():
        start, end = interval
        time_based_toll_rates.loc[:, start:end] = rate
    
    return time_based_toll_rates


df = pd.read_csv("C:\Downloads\dataset-3.csv")

# Call the function to calculate the distance matrix
distance_matrix = calculate_distance_matrix(df)

# Call the function to calculate time-based toll rates
time_based_toll_rates = calculate_time_based_toll_rates(distance_matrix)

# Print the resulting time-based toll rates
print(time_based_toll_rates)
