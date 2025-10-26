"""
Convert County Health Rankings data to D3.js-friendly format
This script reads the raw data files and creates a cleaned CSV for visualization
"""

import csv
import json
import os
from collections import defaultdict

def convert_county_health_data(input_file, output_file):
    """
    Convert County Health Rankings CSV to a format optimized for D3.js
    
    Expected input columns (adjust based on actual data):
    - FIPS or County Code
    - County
    - State
    - Year (or Release Year)
    - Various health metrics
    """
    
    print(f"Converting {input_file} to {output_file}...")
    
    # Column mapping - adjust these based on your actual data file
    # This is a template; you'll need to inspect your data and update these mappings
    column_mapping = {
        # Input column name -> Output column name
        'FIPS': 'fips',
        'County': 'county',
        'State': 'state',
        'Release Year': 'year',
        'Year': 'year',
        
        # Health metrics - update with actual column names from your data
        'Life Expectancy': 'life_expectancy',
        'Years of Potential Life Lost Rate': 'premature_death',
        'Adult Obesity': 'adult_obesity',
        'Diabetes Prevalence': 'diabetes',
        'Unemployment': 'unemployment',
        'Median Household Income': 'median_income',
        
        # Add more mappings as needed
        'Adult Smoking': 'adult_smoking',
        'Physical Inactivity': 'physical_inactivity',
        'Uninsured': 'uninsured',
        'Primary Care Physicians Rate': 'primary_care_rate',
        'High School Graduation': 'hs_graduation',
    }
    
    # Metrics to include in output
    output_metrics = [
        'fips', 'county', 'state', 'year',
        'life_expectancy', 'premature_death', 'adult_obesity', 'diabetes',
        'unemployment', 'median_income', 'adult_smoking', 'physical_inactivity',
        'uninsured', 'primary_care_rate', 'hs_graduation'
    ]
    
    try:
        with open(input_file, 'r', encoding='utf-8-sig') as infile:
            reader = csv.DictReader(infile)
            
            # Get actual column names
            actual_columns = reader.fieldnames
            print(f"\nFound {len(actual_columns)} columns in input file")
            print(f"First 10 columns: {actual_columns[:10]}")
            
            # Create reverse mapping for columns that exist
            reverse_mapping = {}
            for input_col, output_col in column_mapping.items():
                if input_col in actual_columns:
                    reverse_mapping[input_col] = output_col
                    print(f"  [OK] Mapped: {input_col} -> {output_col}")
            
            if not reverse_mapping:
                print("\n[ERROR] No matching columns found!")
                print("Please update the column_mapping in convert_data.py")
                print(f"\nAvailable columns in your file:")
                for col in actual_columns:
                    print(f"  - {col}")
                return False
            
            # Read and convert data
            output_rows = []
            skipped_rows = 0
            
            for row_num, row in enumerate(reader, start=2):
                output_row = {}
                
                # Map columns
                for input_col, output_col in reverse_mapping.items():
                    value = row.get(input_col, '').strip()
                    
                    # Clean numeric values
                    if output_col not in ['fips', 'county', 'state']:
                        # Remove commas, percentage signs, dollar signs
                        value = value.replace(',', '').replace('%', '').replace('$', '')
                        
                        # Handle empty values
                        if value == '' or value.lower() in ['n/a', 'na', 'null', 'none']:
                            value = ''
                    
                    output_row[output_col] = value
                
                # Validate required fields
                if not output_row.get('fips') or not output_row.get('county'):
                    skipped_rows += 1
                    continue
                
                # Ensure FIPS is 5 digits
                fips = output_row.get('fips', '')
                if fips and len(fips) < 5:
                    output_row['fips'] = fips.zfill(5)
                
                # Only include rows with at least one metric value
                has_data = any(output_row.get(m, '') != '' for m in output_metrics[4:])
                if has_data:
                    output_rows.append(output_row)
            
            # Write output file
            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=output_metrics)
                writer.writeheader()
                writer.writerows(output_rows)
            
            print(f"\n[SUCCESS] Conversion complete!")
            print(f"  - Input rows: {row_num - 1}")
            print(f"  - Output rows: {len(output_rows)}")
            print(f"  - Skipped rows: {skipped_rows}")
            print(f"  - Output file: {output_file}")
            
            return True
            
    except FileNotFoundError:
        print(f"[ERROR] File '{input_file}' not found!")
        print("Please download the data from County Health Rankings website")
        return False
    except Exception as e:
        print(f"[ERROR] {e}")
        return False

def analyze_data_file(filepath):
    """
    Analyze a data file and print useful information
    """
    print(f"\nAnalyzing: {filepath}")
    print("=" * 60)
    
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            
            print(f"\nColumns ({len(headers)}):")
            for i, header in enumerate(headers, 1):
                print(f"  {i:3d}. {header}")
            
            # Sample first few rows
            print(f"\nFirst row sample:")
            row = next(reader)
            for key, value in list(row.items())[:10]:
                print(f"  {key}: {value}")
            
    except Exception as e:
        print(f"Error: {e}")

def create_sample_data():
    """
    Create a sample data file for testing if no real data is available
    """
    output_file = 'data/county_health_data.csv'
    
    os.makedirs('data', exist_ok=True)
    
    print("Creating sample data file...")
    
    # Sample data for a few counties across multiple years
    sample_data = []
    
    states = [
        ('06', 'California', [('037', 'Los Angeles'), ('073', 'San Diego')]),
        ('48', 'Texas', [('201', 'Harris'), ('113', 'Dallas')]),
        ('36', 'New York', [('061', 'New York'), ('047', 'Kings')]),
        ('17', 'Illinois', [('031', 'Cook'), ('043', 'DuPage')]),
    ]
    
    for year in range(2014, 2025):
        for state_fips, state_name, counties in states:
            for county_fips, county_name in counties:
                fips = state_fips + county_fips
                
                # Generate realistic-ish random values
                import random
                random.seed(int(fips) + year)
                
                row = {
                    'fips': fips,
                    'county': county_name,
                    'state': state_name,
                    'year': year,
                    'life_expectancy': round(70 + random.random() * 15, 1),
                    'premature_death': round(2000 + random.random() * 8000),
                    'adult_obesity': round(20 + random.random() * 25, 1),
                    'diabetes': round(8 + random.random() * 10, 1),
                    'unemployment': round(2 + random.random() * 10, 1),
                    'median_income': round(30000 + random.random() * 60000),
                    'adult_smoking': round(10 + random.random() * 15, 1),
                    'physical_inactivity': round(15 + random.random() * 20, 1),
                    'uninsured': round(5 + random.random() * 15, 1),
                    'primary_care_rate': round(40 + random.random() * 60, 1),
                    'hs_graduation': round(75 + random.random() * 20, 1),
                }
                
                sample_data.append(row)
    
    # Write sample data
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = list(sample_data[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sample_data)
    
    print(f"[SUCCESS] Created sample data with {len(sample_data)} rows")
    print(f"  File: {output_file}")
    print(f"  Years: 2014-2024")
    print(f"  Counties: {len(states) * 2}")
    print("\nNOTE: This is sample data for testing!")
    print("Replace with real data from County Health Rankings website.")

def main():
    print("County Health Rankings Data Converter")
    print("=" * 60)
    
    # Check if data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')
        print("[OK] Created 'data' directory")
    
    # Look for data files
    data_files = [f for f in os.listdir('data') if f.endswith('.csv') and f != 'county_health_data.csv']
    
    if not data_files:
        print("\n[INFO] No data files found in 'data/' directory")
        print("\nOptions:")
        print("  1. Download data from https://www.countyhealthrankings.org/health-data")
        print("  2. Create sample data for testing")
        
        choice = input("\nCreate sample data? (y/n): ").lower()
        if choice == 'y':
            create_sample_data()
        else:
            print("\nPlease download data files and place them in the 'data/' directory")
        return
    
    print(f"\nFound {len(data_files)} data file(s):")
    for i, f in enumerate(data_files, 1):
        print(f"  {i}. {f}")
    
    # If only one file, use it
    if len(data_files) == 1:
        input_file = os.path.join('data', data_files[0])
        choice = input(f"\nAnalyze this file? (y/n): ").lower()
        if choice == 'y':
            analyze_data_file(input_file)
        
        choice = input(f"\nConvert this file to D3.js format? (y/n): ").lower()
        if choice == 'y':
            output_file = 'data/county_health_data.csv'
            convert_county_health_data(input_file, output_file)
    else:
        # Multiple files - let user choose
        choice = input("\nEnter file number to analyze (or 'q' to quit): ")
        if choice.isdigit() and 1 <= int(choice) <= len(data_files):
            input_file = os.path.join('data', data_files[int(choice) - 1])
            analyze_data_file(input_file)
            
            choice = input(f"\nConvert this file? (y/n): ").lower()
            if choice == 'y':
                output_file = 'data/county_health_data.csv'
                convert_county_health_data(input_file, output_file)

if __name__ == "__main__":
    main()

