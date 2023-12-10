import pandas as pd

def calculate_distance_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Assuming df has columns 'id_start', 'id_end', and 'distance'
    distance_matrix = df.pivot(index='id_start', columns='id_end', values='distance').fillna(0)
    return distance_matrix

def unroll_distance_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Assuming df is a distance matrix DataFrame
    unrolled_df = df.unstack().reset_index(name='distance').rename(columns={'level_0': 'id_start', 'id_end': 'id_end'})
    return unrolled_df

def find_ids_within_ten_percentage_threshold(df: pd.DataFrame, reference_id: int) -> pd.DataFrame:
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Assuming df has columns 'id_start', 'id_end', and 'distance'
    average_distances = df.groupby('id_start')['distance'].mean().reset_index(name='average_distance')
    reference_distance = average_distances.loc[average_distances['id_start'] == reference_id, 'average_distance'].values[0]
    
    threshold = 0.1  # 10%
    ids_within_threshold = average_distances[
        (reference_distance * (1 - threshold) <= average_distances['average_distance']) &
        (average_distances['average_distance'] <= reference_distance * (1 + threshold))
    ]
    return ids_within_threshold

def calculate_toll_rate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Assuming df has columns 'id_start', 'id_end', and 'distance'
    # This is a placeholder, replace it with your actual logic
    df['toll_rate'] = df['distance'] * 0.1
    return df

def calculate_time_based_toll_rates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Assuming df has columns 'id_start', 'id_end', 'distance'
    # and 'timestamp' indicating the time of travel
    # This is a placeholder, replace it with your actual logic
    df['time_based_toll_rate'] = df['distance'] * 0.2
    return df

# Load dataset-3
file_path3 = '../datasets/dataset-3.csv'
df3 = pd.read_csv(file_path3)

# Apply the functions
distance_matrix_result = calculate_distance_matrix(df3)
unrolled_result = unroll_distance_matrix(distance_matrix_result)
ids_within_threshold_result = find_ids_within_ten_percentage_threshold(unrolled_result, reference_id=1001400)
toll_rate_result = calculate_toll_rate(unrolled_result)
time_based_toll_rate_result = calculate_time_based_toll_rates(unrolled_result)

# Display the results (you can modify this part based on your requirements)
print("Distance Matrix:")
print(distance_matrix_result)

print("\nUnrolled DataFrame:")
print(unrolled_result)

print("\nIDs Within Ten Percentage Threshold:")
print(ids_within_threshold_result)

print("\nToll Rates:")
print(toll_rate_result)

print("\nTime-Based Toll Rates:")
print(time_based_toll_rate_result)
