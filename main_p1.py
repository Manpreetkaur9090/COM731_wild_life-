
import loader_p1
import retriever_p1
import analyzer_p1
import visualizer_p1


def display_main_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("     URBAN WILDLIFE ANALYSIS - PROJECT 1")
    print("="*60)
    print("1. Task A - CSV Retrieval Tasks (A1-A4)")
    print("2. Task B - Pandas Analysis Tasks (B1-B4)")
    print("3. Task C - Visualization Tasks (C1-C4)")
    print("4. Run Full Pipeline (All Tasks)")
    print("5. Exit")
    print("="*60)


def run_task_a_menu(rows_list, header):
    """
    Run Task A sub-menu for retrieval tasks.
    
    Args:
        rows_list (list): List of data rows from CSV
        header (list): Header row
    """
    while True:
        print("\n" + "-"*60)
        print("  TASK A - CSV RETRIEVAL TASKS")
        print("-"*60)
        print("1. A1 - Wildlife Sightings by City")
        print("2. A2 - Environmental Context")
        print("3. A3 - Human Impact Indicators")
        print("4. A4 - Custom Filter (Duration & Season)")
        print("5. Show Available Columns")
        print("6. Back to Main Menu")
        print("-"*60)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            city = input("Enter city name: ").strip()
            retriever_p1.task_a1_wildlife_by_city(rows_list, header, city)
        
        elif choice == '2':
            time_of_day = input("Enter TimeOfDay (e.g., Morning, Afternoon, Night): ").strip()
            try:
                aqi_threshold = float(input("Enter maximum AQI threshold: ").strip())
                retriever_p1.task_a2_environmental_context(rows_list, header, time_of_day, aqi_threshold)
            except ValueError:
                print("Error: Please enter a valid number for AQI threshold.")
        
        elif choice == '3':
            try:
                min_urban_dev = float(input("Enter minimum UrbanDevelopmentIndex: ").strip())
                min_proximity = float(input("Enter minimum Proximity to Water: ").strip())
                retriever_p1.task_a3_human_impact(rows_list, header, min_urban_dev, min_proximity)
            except ValueError:
                print("Error: Please enter valid numbers.")
        
        elif choice == '4':
            try:
                min_duration = float(input("Enter minimum sighting duration (minutes): ").strip())
                season = input("Enter season (Spring, Summer, Fall, Winter): ").strip()
                retriever_p1.task_a4_custom_duration_season(rows_list, header, min_duration, season)
            except ValueError:
                print("Error: Please enter a valid number for duration.")
        
        elif choice == '5':
            retriever_p1.display_available_columns(header)
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice. Please try again.")


def run_task_b_menu(df):
    """
    Run Task B sub-menu for pandas analysis tasks.
    
    Args:
        df (DataFrame): Pandas DataFrame with wildlife data
    """
    while True:
        print("\n" + "-"*60)
        print("  TASK B - PANDAS ANALYSIS TASKS")
        print("-"*60)
        print("1. B1 - Top Species in Green Zones")
        print("2. B2 - Environmental Influence by City")
        print("3. B3 - Human-Wildlife Interaction Analysis")
        print("4. B4 - Green Space vs Sightings (Endangered)")
        print("5. Back to Main Menu")
        print("-"*60)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            try:
                green_threshold = float(input("Enter minimum green space threshold: ").strip())
                season = input("Enter season: ").strip()
                analyzer_p1.task_b1_top_species_green(df, green_threshold, season)
            except ValueError:
                print("Error: Please enter a valid number for threshold.")
        
        elif choice == '2':
            city = input("Enter city name: ").strip()
            analyzer_p1.task_b2_env_influence_by_city(df, city)
        
        elif choice == '3':
            interaction_type = input("Enter InteractionType (e.g., Observation, Feeding, Conflict): ").strip()
            analyzer_p1.task_b3_interaction_analysis(df, interaction_type)
        
        elif choice == '4':
            analyzer_p1.task_b4_custom_endangered_correlation(df)
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")


def run_task_c_menu(df):
    """
    Run Task C sub-menu for visualization tasks.
    
    Args:
        df (DataFrame): Pandas DataFrame with wildlife data
    """
    while True:
        print("\n" + "-"*60)
        print("  TASK C - VISUALIZATION TASKS")
        print("-"*60)
        print("1. C1 - Temperature & Humidity by City")
        print("2. C2 - SpeciesCategory Trends")
        print("3. C3 - Public Awareness Distribution")
        print("4. C4 - Noise vs Sightings (Endangered)")
        print("5. Back to Main Menu")
        print("-"*60)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            season = input("Enter season: ").strip()
            visualizer_p1.task_c1_temp_humidity_by_city(df, season)
        
        elif choice == '2':
            city = input("Enter city name: ").strip()
            visualizer_p1.task_c2_species_trends(df, city)
        
        elif choice == '3':
            city = input("Enter city name: ").strip()
            visualizer_p1.task_c3_awareness_pie(df, city)
        
        elif choice == '4':
            visualizer_p1.task_c4_custom_noise_scatter(df)
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")


def run_full_pipeline(rows_list, header, df):
    """
    Run a sample of all tasks in sequence.
    
    Args:
        rows_list (list): List data for Task A
        header (list): Header row
        df (DataFrame): DataFrame for Tasks B and C
    """
    print("\n" + "="*60)
    print("  RUNNING FULL PIPELINE (SAMPLE TASKS)")
    print("="*60)
    
    # Sample Task A
    print("\n[Running Sample Task A1]")
    retriever_p1.task_a1_wildlife_by_city(rows_list, header, "New York")
    
    # Sample Task B
    print("\n[Running Sample Task B1]")
    analyzer_p1.task_b1_top_species_green(df, 0.3, "Spring")
    
    # Sample Task C
    print("\n[Running Sample Task C1]")
    visualizer_p1.task_c1_temp_humidity_by_city(df, "Summer")
    
    print("\n" + "="*60)
    print("  FULL PIPELINE COMPLETED")
    print("="*60)


def main():
    """Main entry point for the application."""
    print("\nWelcome to Urban Wildlife Analysis System (Project 1)")
    print("Coding Style: Procedural | Naming Convention: snake_case")
    
    # Initialize data (Task A0)
    header, rows_list, file_path = loader_p1.initialize_data()
    
    if header is None or rows_list is None:
        print("Failed to load data. Exiting.")
        return
    
    # Load DataFrame for Tasks B and C
    df = analyzer_p1.load_dataframe(file_path)
    
    if df is None:
        print("Failed to load DataFrame. Exiting.")
        return
    
    # Main menu loop
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            run_task_a_menu(rows_list, header)
        
        elif choice == '2':
            run_task_b_menu(df)
        
        elif choice == '3':
            run_task_c_menu(df)
        
        elif choice == '4':
            run_full_pipeline(rows_list, header, df)
        
        elif choice == '5':
            print("\nThank you for using Urban Wildlife Analysis System!")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
