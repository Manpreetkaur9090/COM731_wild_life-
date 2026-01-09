
import pandas as pd
from tabulate import tabulate


def load_dataframe(file_path):
    """
    Load CSV file into pandas DataFrame.
    
    Args:
        file_path (str): Path to CSV file
        
    Returns:
        DataFrame: Loaded pandas DataFrame
    """
    try:
        df = pd.read_csv(file_path)
        print(f"\n✓ DataFrame loaded: {len(df)} rows, {len(df.columns)} columns")
        return df
    except Exception as e:
        print(f"Error loading DataFrame: {str(e)}")
        return None


def task_b1_top_species_green(df, green_threshold, season):
    """
    Task B1: Find top 3 most frequently sighted species in green zones.
    Filters by green space threshold and season.
    
    Args:
        df (DataFrame): Wildlife data
        green_threshold (float): Minimum green space nearby
        season (str): Season to filter by
    """
    print(f"\n=== Task B1: Top 3 Species in Green Zones ===")
    print(f"Filters: Green Space > {green_threshold}, Season = {season}")
    
    # Filter data
    filtered_df = df[(df['NearbyGreenSpaces'] > green_threshold) & 
                     (df['Season'].str.lower() == season.lower())]
    
    if filtered_df.empty:
        print("No records found matching criteria.")
        return
    
    # Group by species and sum sightings
    species_sightings = filtered_df.groupby('WildlifeSpecies')['NumberOfSightings'].sum()
    top_3_species = species_sightings.nlargest(3)
    
    # Display results
    result_table = []
    for species, sightings in top_3_species.items():
        result_table.append([species, sightings])
    
    print(tabulate(result_table, 
                  headers=["WildlifeSpecies", "Total Sightings"],
                  tablefmt="grid"))
    print(f"\nTotal records analyzed: {len(filtered_df)}")


def task_b2_env_influence_by_city(df, city):
    """
    Task B2: Analyze environmental influence on sightings for a specific city.
    Computes average sightings and duration grouped by weather and TimeOfDay.
    
    Args:
        df (DataFrame): Wildlife data
        city (str): City name to filter by
    """
    print(f"\n=== Task B2: Environmental Influence in {city} ===")
    
    # Filter by city
    city_df = df[df['City'].str.lower() == city.lower()]
    
    if city_df.empty:
        print(f"No records found for city '{city}'.")
        return
    
    # Group by WeatherCondition and TimeOfDay
    grouped = city_df.groupby(['WeatherCondition', 'TimeOfDay']).agg({
        'NumberOfSightings': 'mean',
        'SightingDuration_Min': 'mean'
    }).round(2)
    
    # Display results
    print("\nAverage Sightings and Duration by Weather & TimeOfDay:")
    print(grouped.to_string())
    print(f"\nTotal records analyzed: {len(city_df)}")


def task_b3_interaction_analysis(df, interaction_type):
    """
    Task B3: Analyze human-wildlife interaction patterns.
    For specified InteractionType, compute average environmental factors
    for sightings with duration > average duration for that InteractionType.
    
    Args:
        df (DataFrame): Wildlife data
        interaction_type (str): Type of interaction to analyze
    """
    print(f"\n=== Task B3: Human-Wildlife Interaction Analysis ({interaction_type}) ===")
    
    # Filter by InteractionType
    interaction_df = df[df['InteractionType'].str.lower() == interaction_type.lower()]
    
    if interaction_df.empty:
        print(f"No records found for InteractionType '{interaction_type}'.")
        return
    
    # Calculate average duration for this InteractionType
    avg_duration = interaction_df['SightingDuration_Min'].mean()
    print(f"\nAverage sighting duration for '{interaction_type}': {avg_duration:.2f} minutes")
    
    # Filter for durations greater than average
    longer_sightings = interaction_df[interaction_df['SightingDuration_Min'] > avg_duration]
    
    if longer_sightings.empty:
        print("No sightings with duration above average.")
        return
    
    # Group by ResidentialAreaType and compute averages
    grouped = longer_sightings.groupby('ResidentialAreaType').agg({
        'NoiseLevel_dB': 'mean',
        'HumanActivityLevel': lambda x: x.value_counts().index[0] if len(x) > 0 else 'N/A',
        'LightPollutionLevel': 'mean'
    }).round(2)
    
    grouped.columns = ['Avg NoiseLevel_dB', 'Most Common Activity Level', 'Avg LightPollutionLevel']
    
    # Display results
    print(f"\nAnalysis for sightings with duration > {avg_duration:.2f} min:")
    print(grouped.to_string())
    print(f"\nRecords analyzed: {len(longer_sightings)}")


def task_b4_custom_endangered_correlation(df):
    """
    Task B4 (Custom): Analyze correlation between green space and sightings 
    for endangered species only.
    
    This custom task is unique to Project 1.
    
    Args:
        df (DataFrame): Wildlife data
    """
    print(f"\n=== Task B4: Green Space vs Sightings (Endangered Species) ===")
    
    # Filter for endangered species
    endangered_df = df[df['IsEndangeredSpecies'].str.lower() == 'yes']
    
    if endangered_df.empty:
        print("No endangered species found in dataset.")
        return
    
    # Create bins for green space
    green_bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    green_labels = ['0-0.2', '0.2-0.4', '0.4-0.6', '0.6-0.8', '0.8-1.0']
    
    endangered_df = endangered_df.copy()
    endangered_df['Green_Space_Range'] = pd.cut(endangered_df['NearbyGreenSpaces'], 
                                                  bins=green_bins, 
                                                  labels=green_labels, 
                                                  include_lowest=True)
    
    # Group by green space range
    grouped = endangered_df.groupby('Green_Space_Range', observed=True).agg({
        'NumberOfSightings': 'mean',
        'WildlifeSpecies': 'count'
    }).round(2)
    
    grouped.columns = ['Avg NumberOfSightings', 'Count of Observations']
    
    # Display results
    print("\nCorrelation Analysis (Green Space Ranges):")
    print(grouped.to_string())
    print(f"\nTotal endangered species records: {len(endangered_df)}")
    
    # Calculate correlation coefficient
    correlation = endangered_df['NearbyGreenSpaces'].corr(endangered_df['NumberOfSightings'])
    print(f"\nPearson Correlation Coefficient: {correlation:.4f}")
