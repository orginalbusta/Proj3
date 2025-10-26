"""
County Health Rankings Data Explorer
This script downloads and explores the County Health Rankings data
"""

import urllib.request
import os
import json
import csv
from collections import defaultdict

# Create data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

print("County Health Rankings & Roadmaps Data Explorer")
print("=" * 60)
print("\nIMPORTANT: Please visit https://www.countyhealthrankings.org/health-data")
print("and download the data files manually to the 'data/' folder.")
print("\nTypically, the data is available as:")
print("- National Data & Documentation (Excel files)")
print("- State-specific CSV files")
print("- Trend data files covering multiple years")
print("\nLook for files like:")
print("- 'analytic_data2024.csv' or similar")
print("- 'Trend files' that contain year-over-year data")
print("\n" + "=" * 60)

def explore_csv_file(filepath):
    """Explore a CSV file and print basic statistics"""
    print(f"\n\n{'='*60}")
    print(f"Exploring: {filepath}")
    print("=" * 60)
    
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            headers = next(reader)
            
            print(f"\n[OK] Number of columns: {len(headers)}")
            print(f"\n[OK] Column names (first 20):")
            for i, header in enumerate(headers[:20], 1):
                print(f"  {i:2d}. {header}")
            
            if len(headers) > 20:
                print(f"  ... and {len(headers) - 20} more columns")
            
            # Read first few rows
            rows = []
            for i, row in enumerate(reader):
                if i >= 5:
                    break
                rows.append(row)
            
            print(f"\n[OK] Total rows (sample): Read {len(rows)} rows")
            
            # Check for year columns
            year_columns = [h for h in headers if 'year' in h.lower()]
            if year_columns:
                print(f"\n[OK] Year-related columns found: {year_columns}")
            
            # Check for county columns
            county_columns = [h for h in headers if 'county' in h.lower() or 'fips' in h.lower()]
            if county_columns:
                print(f"\n[OK] County-related columns found: {county_columns}")
            
            # Check for state columns
            state_columns = [h for h in headers if 'state' in h.lower()]
            if state_columns:
                print(f"\n[OK] State-related columns found: {state_columns}")
            
            print("\n[OK] Sample data (first 3 rows):")
            for i, row in enumerate(rows[:3], 1):
                print(f"\n  Row {i}:")
                for j, (header, value) in enumerate(zip(headers[:10], row[:10])):
                    print(f"    {header}: {value}")
                if len(row) > 10:
                    print(f"    ... and {len(row) - 10} more fields")
            
            return {
                'filepath': filepath,
                'num_columns': len(headers),
                'headers': headers,
                'sample_rows': rows,
                'year_columns': year_columns,
                'county_columns': county_columns,
                'state_columns': state_columns
            }
    except Exception as e:
        print(f"[ERROR] reading file: {e}")
        return None

def explore_data_directory():
    """Explore all CSV files in the data directory"""
    data_dir = 'data'
    
    if not os.path.exists(data_dir):
        print(f"\n[ERROR] Directory '{data_dir}' not found!")
        return
    
    files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    
    if not files:
        print(f"\n[ERROR] No CSV files found in '{data_dir}' directory!")
        print("\nPlease download data files from:")
        print("https://www.countyhealthrankings.org/health-data")
        return
    
    print(f"\n[OK] Found {len(files)} CSV file(s) in '{data_dir}':")
    for f in files:
        print(f"  - {f}")
    
    # Explore each file
    results = []
    for file in files:
        result = explore_csv_file(os.path.join(data_dir, file))
        if result:
            results.append(result)
    
    # Generate summary
    print("\n\n" + "=" * 60)
    print("SUMMARY & RECOMMENDATIONS")
    print("=" * 60)
    
    if results:
        print("\n[SUCCESS] Data files successfully analyzed!")
        print("\nKey metrics to consider for visualization:")
        print("  - Life Expectancy")
        print("  - Premature Death Rate")
        print("  - Adult Obesity Rate")
        print("  - Diabetes Prevalence")
        print("  - Unemployment Rate")
        print("  - Median Household Income")
        print("  - High School Graduation Rate")
        print("  - Access to Exercise Opportunities")
        
        print("\nRecommended interaction techniques:")
        print("  1. Choropleth map with color intensity by metric")
        print("  2. Year slider/dropdown for temporal navigation")
        print("  3. Hover tooltips showing detailed county statistics")
        print("  4. Metric selector dropdown to change the displayed measure")
        print("  5. State filter to focus on specific states")
        print("  6. Zoom and pan capabilities for detailed exploration")
        
        print("\nNext steps:")
        print("  1. Identify which file contains multi-year county data")
        print("  2. Select 3-5 key health metrics for visualization")
        print("  3. Create a filtered/cleaned JSON dataset for D3.js")
        print("  4. Start building the D3.js visualization")
    
    return results

if __name__ == "__main__":
    explore_data_directory()
    
    print("\n\n" + "=" * 60)
    print("Data exploration complete!")
    print("=" * 60)

