import pandas as pd

def filter_routes(dataframe):
    # Group by 'route' and calculate the average of 'truck' for each route
    route_avg_truck = dataframe.groupby('route')['truck'].mean()
    
    # Filter routes where the average of 'truck' is greater than 7
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    
    # Sort the list of selected routes
    selected_routes.sort()
    
    return selected_routes


# Read the CSV into a DataFrame
df = pd.read_csv("C:\Downloads\dataset-1.csv")

# Call the function with the DataFrame
result_routes = filter_routes(df)

# Print the sorted list of selected routes
print(result_routes)
