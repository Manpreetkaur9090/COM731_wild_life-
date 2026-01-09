"""
Visualization Module for Project 1 (Procedural Style)
Implements Task C (C1-C4) using matplotlib.
Variable naming: snake_case
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def task_c1_temp_humidity_by_city(df, season):
    """
    Task C1: Compare average temperature and humidity across cities for a given season.
    Creates a grouped bar chart.
    
    Args:
        df (DataFrame): Wildlife data
        season (str): Season to filter by
    """
    print(f"\n=== Task C1: Temperature & Humidity by City ({season}) ===")
    
    # Filter by season
    season_df = df[df['Season'].str.lower() == season.lower()]
    
    if season_df.empty:
        print(f"No data found for season '{season}'.")
        return
    
    # Group by city and calculate averages
    city_stats = season_df.groupby('City').agg({
        'Temperature': 'mean',
        'Humidity': 'mean'
    }).round(2)
    
    # Prepare data for plotting
    cities = city_stats.index.tolist()
    avg_temp = city_stats['Temperature'].tolist()
    avg_humidity = city_stats['Humidity'].tolist()
    
    # Create grouped bar chart
    x_pos = np.arange(len(cities))
    width = 0.35
    
    plt.figure(figsize=(10, 6))
    plt.bar(x_pos - width/2, avg_temp, width, label='Avg Temperature (°C)', color='orangered')
    plt.bar(x_pos + width/2, avg_humidity, width, label='Avg Humidity (%)', color='steelblue')
    
    plt.xlabel('City')
    plt.ylabel('Value')
    plt.title(f'Average Temperature and Humidity by City - {season}')
    plt.xticks(x_pos, cities)
    plt.legend()
    plt.tight_layout()
    
    # Save figure
    filename = f'project_1_c1_temp_humidity_{season}.png'
    plt.savefig(filename)
    print(f"✓ Chart saved as '{filename}'")
    plt.show()


def task_c2_species_trends(df, city):
    """
    Task C2: Plot yearly trend of average sightings for each SpeciesCategory in a city.
    Creates line plots.
    
    Args:
        df (DataFrame): Wildlife data
        city (str): City name to filter by
    """
    print(f"\n=== Task C2: SpeciesCategory Trends in {city} ===")
    
    # Filter by city
    city_df = df[df['City'].str.lower() == city.lower()]
    
    if city_df.empty:
        print(f"No data found for city '{city}'.")
        return
    
    # Group by year and SpeciesCategory
    trends = city_df.groupby(['Year', 'SpeciesCategory'])['NumberOfSightings'].mean().unstack(fill_value=0)
    
    # Create line plot
    plt.figure(figsize=(10, 6))
    
    for category in trends.columns:
        plt.plot(trends.index, trends[category], marker='o', label=category)
    
    plt.xlabel('Year')
    plt.ylabel('Average NumberOfSightings')
    plt.title(f'Wildlife Sighting Trends by SpeciesCategory - {city}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save figure
    filename = f'project_1_c2_species_trends_{city}.png'
    plt.savefig(filename)
    print(f"✓ Chart saved as '{filename}'")
    plt.show()


def task_c3_awareness_pie(df, city):
    """
    Task C3: Create pie chart showing proportion of average public awareness 
    by ResidentialAreaType for a city.
    
    Args:
        df (DataFrame): Wildlife data
        city (str): City name to filter by
    """
    print(f"\n=== Task C3: Public Awareness Distribution in {city} ===")
    
    # Filter by city
    city_df = df[df['City'].str.lower() == city.lower()]
    
    if city_df.empty:
        print(f"No data found for city '{city}'.")
        return
    
    # Group by ResidentialAreaType
    awareness_by_area = city_df.groupby('ResidentialAreaType')['PublicAwarenessLevel'].mean()
    
    # Create pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(awareness_by_area.values, 
            labels=awareness_by_area.index, 
            autopct='%1.1f%%',
            startangle=90,
            colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    
    plt.title(f'PublicAwarenessLevel by ResidentialAreaType - {city}')
    plt.tight_layout()
    
    # Save figure
    filename = f'project_1_c3_awareness_{city}.png'
    plt.savefig(filename)
    print(f"✓ Chart saved as '{filename}'")
    plt.show()


def task_c4_custom_noise_scatter(df):
    """
    Task C4 (Custom): Scatter plot of Noise Level vs NumberOfSightings 
    for endangered species only.
    
    This custom task is unique to Project 1.
    
    Args:
        df (DataFrame): Wildlife data
    """
    print(f"\n=== Task C4: Noise Level vs Sightings (Endangered Species) ===")
    
    # Filter for endangered species
    endangered_df = df[df['IsEndangeredSpecies'].str.lower() == 'yes']
    
    if endangered_df.empty:
        print("No endangered species found in dataset.")
        return
    
    # Extract data for scatter plot
    noise_levels = endangered_df['NoiseLevel_dB']
    sightings = endangered_df['NumberOfSightings']
    species_names = endangered_df['WildlifeSpecies']
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(noise_levels, sightings, alpha=0.6, s=100, color='coral', edgecolors='black')
    
    # Add labels for each point
    for i, species in enumerate(species_names):
        plt.annotate(species, (noise_levels.iloc[i], sightings.iloc[i]), 
                    fontsize=8, alpha=0.7, xytext=(5, 5), textcoords='offset points')
    
    plt.xlabel('NoiseLevel_dB')
    plt.ylabel('NumberOfSightings')
    plt.title('Noise Level vs NumberOfSightings (Endangered Species Only)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save figure
    filename = 'project_1_c4_noise_scatter_endangered.png'
    plt.savefig(filename)
    print(f"✓ Chart saved as '{filename}'")
    plt.show()
    
    print(f"\nTotal endangered species records plotted: {len(endangered_df)}")
