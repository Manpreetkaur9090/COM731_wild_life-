

from tabulate import tabulate


def find_column_index(header, column_name):
    """
    Find the index of a column by its name.
    
    Args:
        header (list): Header row from CSV
        column_name (str): Name of the column to find
        
    Returns:
        int: Index of the column, or -1 if not found
    """
    try:
        return header.index(column_name)
    except ValueError:
        return -1


def task_a1_wildlife_by_city(rows_list, header, city):
    """
    Task A1: Retrieve wildlife sighting details for a specified city.
    Displays: WildlifeSpecies, SpeciesCategory, NumberOfSightings, IsEndangeredSpecies
    
    Args:
        rows_list (list): List of data rows from CSV
        header (list): Header row
        city (str): City name to filter by
    """
    print(f"\n=== Task A1: Wildlife Sightings in {city} ===")
    
    # Find column indices
    city_idx = find_column_index(header, "City")
    species_idx = find_column_index(header, "WildlifeSpecies")
    category_idx = find_column_index(header, "SpeciesCategory")
    sightings_idx = find_column_index(header, "NumberOfSightings")
    endangered_idx = find_column_index(header, "IsEndangeredSpecies")
    
    if city_idx == -1:
        print("Error: Column 'City' not found.")
        return
    
    # Filter rows by city
    results = []
    for row in rows_list:
        if len(row) > city_idx and row[city_idx].strip().lower() == city.strip().lower():
            results.append([
                row[species_idx] if species_idx >= 0 else "N/A",
                row[category_idx] if category_idx >= 0 else "N/A",
                row[sightings_idx] if sightings_idx >= 0 else "N/A",
                row[endangered_idx] if endangered_idx >= 0 else "N/A"
            ])
    
    # Display results
    if results:
        print(tabulate(results, 
                      headers=["WildlifeSpecies", "SpeciesCategory", "NumberOfSightings", "IsEndangeredSpecies"],
                      tablefmt="grid"))
        print(f"\nTotal records found: {len(results)}")
    else:
        print(f"No wildlife sightings found for city '{city}'.")


def task_a2_environmental_context(rows_list, header, time_of_day, aqi_threshold):
    """
    Task A2: Retrieve environmental context based on TimeOfDay and AQI threshold.
    Displays: Temperature, Humidity, AirQualityIndex, WeatherCondition
    
    Args:
        rows_list (list): List of data rows
        header (list): Header row
        time_of_day (str): TimeOfDay to filter (e.g., 'Morning', 'Night')
        aqi_threshold (float): Maximum AQI value
    """
    print(f"\n=== Task A2: Environmental Context ({time_of_day}, AQI < {aqi_threshold}) ===")
    
    # Find column indices
    time_idx = find_column_index(header, "TimeOfDay")
    aqi_idx = find_column_index(header, "AirQualityIndex")
    temp_idx = find_column_index(header, "Temperature")
    humidity_idx = find_column_index(header, "Humidity")
    weather_idx = find_column_index(header, "WeatherCondition")
    
    if time_idx == -1 or aqi_idx == -1:
        print("Error: Required columns not found.")
        return
    
    # Filter rows
    results = []
    for row in rows_list:
        if len(row) > max(time_idx, aqi_idx):
            try:
                row_time = row[time_idx].strip()
                row_aqi = float(row[aqi_idx])
                
                if row_time.lower() == time_of_day.strip().lower() and row_aqi < aqi_threshold:
                    results.append([
                        row[temp_idx] if temp_idx >= 0 else "N/A",
                        row[humidity_idx] if humidity_idx >= 0 else "N/A",
                        row[aqi_idx],
                        row[weather_idx] if weather_idx >= 0 else "N/A"
                    ])
            except (ValueError, IndexError):
                continue
    
    # Display results
    if results:
        print(tabulate(results,
                      headers=["Temperature", "Humidity", "AirQualityIndex", "WeatherCondition"],
                      tablefmt="grid"))
        print(f"\nTotal records found: {len(results)}")
    else:
        print(f"No records found matching criteria.")


def task_a3_human_impact(rows_list, header, min_urban_dev_index, min_proximity_to_water):
    """
    Task A3: Retrieve human impact indicators based on thresholds.
    Displays: HumanActivityLevel, NoiseLevel_dB, LightPollutionLevel, GarbageManagementScore
    
    Args:
        rows_list (list): List of data rows
        header (list): Header row
        min_urban_dev_index (float): Minimum UrbanDevelopmentIndex
        min_proximity_to_water (float): Minimum ProximityToWaterSource
    """
    print(f"\n=== Task A3: Human Impact Indicators ===")
    print(f"Filters: Urban Dev Index >= {min_urban_dev_index}, Proximity to Water >= {min_proximity_to_water}")
    
    # Find column indices
    urban_dev_idx = find_column_index(header, "UrbanDevelopmentIndex")
    proximity_idx = find_column_index(header, "ProximityToWaterSource")
    activity_idx = find_column_index(header, "HumanActivityLevel")
    noise_idx = find_column_index(header, "NoiseLevel_dB")
    light_idx = find_column_index(header, "LightPollutionLevel")
    garbage_idx = find_column_index(header, "GarbageManagementScore")
    
    if urban_dev_idx == -1 or proximity_idx == -1:
        print("Error: Required columns not found.")
        return
    
    # Filter rows
    results = []
    for row in rows_list:
        if len(row) > max(urban_dev_idx, proximity_idx):
            try:
                urban_dev = float(row[urban_dev_idx])
                proximity = float(row[proximity_idx])
                
                if urban_dev >= min_urban_dev_index and proximity >= min_proximity_to_water:
                    results.append([
                        row[activity_idx] if activity_idx >= 0 else "N/A",
                        row[noise_idx] if noise_idx >= 0 else "N/A",
                        row[light_idx] if light_idx >= 0 else "N/A",
                        row[garbage_idx] if garbage_idx >= 0 else "N/A"
                    ])
            except (ValueError, IndexError):
                continue
    
    # Display results
    if results:
        print(tabulate(results,
                      headers=["HumanActivityLevel", "NoiseLevel_dB", "LightPollutionLevel", "GarbageManagementScore"],
                      tablefmt="grid"))
        print(f"\nTotal records found: {len(results)}")
    else:
        print(f"No records found matching criteria.")


def task_a4_custom_duration_season(rows_list, header, min_duration, season):
    """
    Task A4 (Custom): Retrieve species sightings filtered by sighting duration and season.
    Displays: Species, NumberOfSightings, Sighting Duration, Season
    
    This custom task is unique to Project 1.
    
    Args:
        rows_list (list): List of data rows
        header (list): Header row
        min_duration (float): Minimum sighting duration in minutes
        season (str): Season to filter by
    """
    print(f"\n=== Task A4: Custom Filter (Duration > {min_duration} min, Season = {season}) ===")
    
    # Find column indices
    species_idx = find_column_index(header, "WildlifeSpecies")
    sightings_idx = find_column_index(header, "NumberOfSightings")
    duration_idx = find_column_index(header, "SightingDuration_Min")
    season_idx = find_column_index(header, "Season")
    
    if duration_idx == -1 or season_idx == -1:
        print("Error: Required columns not found.")
        return
    
    # Filter rows
    results = []
    for row in rows_list:
        if len(row) > max(duration_idx, season_idx):
            try:
                duration = float(row[duration_idx])
                row_season = row[season_idx].strip()
                
                if duration > min_duration and row_season.lower() == season.strip().lower():
                    results.append([
                        row[species_idx] if species_idx >= 0 else "N/A",
                        row[sightings_idx] if sightings_idx >= 0 else "N/A",
                        row[duration_idx],
                        row[season_idx]
                    ])
            except (ValueError, IndexError):
                continue
    
    # Display results
    if results:
        print(tabulate(results,
                      headers=["WildlifeSpecies", "NumberOfSightings", "SightingDuration_Min", "Season"],
                      tablefmt="grid"))
        print(f"\nTotal records found: {len(results)}")
    else:
        print(f"No records found matching criteria.")


def display_available_columns(header):
    """
    Display all available column names for reference.
    
    Args:
        header (list): Header row from CSV
    """
    print("\n=== Available Columns ===")
    for i, col in enumerate(header, 1):
        print(f"{i}. {col}")
