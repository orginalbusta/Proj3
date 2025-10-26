"""
Convert County Health Rankings Trends CSV to visualization format
Specifically designed for chr_trends_csv_2025.csv file format
"""

import csv
import re
from collections import defaultdict

print("County Health Rankings Trends Converter")
print("=" * 60)

input_file = 'data/chr_trends_csv_2025.csv'
output_file = 'data/county_health_data.csv'

# Metrics we want to extract (from the measurename column)
metric_mapping = {
    'Premature death': 'premature_death',
    'Life expectancy': 'life_expectancy',
    'Adult obesity': 'adult_obesity',
    'Diabetes prevalence': 'diabetes',
    'Unemployment': 'unemployment',
    'Median household income': 'median_income',
    'Adult smoking': 'adult_smoking',
    'Physical inactivity': 'physical_inactivity',
    'Uninsured': 'uninsured',
    'Primary care physicians': 'primary_care_rate',
    'High school completion': 'hs_graduation',
}

print(f"\nReading: {input_file}")

# First pass: collect all data by county and year
county_data = defaultdict(lambda: defaultdict(dict))
counties_info = {}  # Store county name and state by FIPS

with open(input_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    
    total_rows = 0
    processed_rows = 0
    
    for row in reader:
        total_rows += 1
        
        # Skip US-level aggregates
        if row['countycode'] == '000':
            continue
        
        # Create FIPS code (statecode + countycode)
        fips = row['statecode'] + row['countycode']
        
        # Skip if FIPS is invalid
        if len(fips) != 5:
            continue
        
        # Store county info
        if fips not in counties_info:
            counties_info[fips] = {
                'county': row['county'],
                'state': row['state']
            }
        
        # Parse year from yearspan (e.g., "2018-2020" -> 2019 middle year)
        yearspan = row['yearspan']
        if '-' in yearspan:
            years = yearspan.split('-')
            year = (int(years[0]) + int(years[1])) // 2
        else:
            year = int(yearspan)
        
        # Only include years 2014-2024
        if year < 2014 or year > 2024:
            continue
        
        # Get the metric name
        measure = row['measurename']
        
        # Check if this is a metric we want
        if measure in metric_mapping:
            metric_key = metric_mapping[measure]
            
            # Get the value
            rawvalue = row['rawvalue'].replace(',', '').strip()
            
            if rawvalue and rawvalue != '':
                try:
                    value = float(rawvalue)
                    county_data[fips][year][metric_key] = value
                    processed_rows += 1
                except ValueError:
                    pass

print(f"\n[OK] Read {total_rows:,} rows")
print(f"[OK] Processed {processed_rows:,} relevant data points")
print(f"[OK] Found {len(counties_info):,} unique counties")

# Second pass: create output rows
output_rows = []

for fips in sorted(counties_info.keys()):
    info = counties_info[fips]
    
    for year in range(2014, 2025):
        if year in county_data[fips]:
            metrics = county_data[fips][year]
            
            # Only include if we have at least 2 metrics
            if len(metrics) >= 2:
                row = {
                    'fips': fips,
                    'county': info['county'],
                    'state': info['state'],
                    'year': year,
                }
                
                # Add all metrics (empty string if not available)
                for display_name, metric_key in metric_mapping.items():
                    row[metric_key] = metrics.get(metric_key, '')
                
                output_rows.append(row)

print(f"[OK] Created {len(output_rows):,} output rows")

# Calculate coverage by year
years_coverage = defaultdict(set)
for row in output_rows:
    years_coverage[row['year']].add(row['fips'])

print(f"\n[OK] Coverage by year:")
for year in sorted(years_coverage.keys()):
    print(f"  {year}: {len(years_coverage[year]):,} counties")

# Write output file
fieldnames = ['fips', 'county', 'state', 'year'] + list(metric_mapping.values())

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(output_rows)

print(f"\n[SUCCESS] Conversion complete!")
print(f"  Output file: {output_file}")
print(f"  Total rows: {len(output_rows):,}")
print(f"  Counties with data: {len(counties_info):,}")
print(f"  Years covered: 2014-2024")

# Show sample of data
print(f"\n[OK] Sample data (first 3 rows):")
for i, row in enumerate(output_rows[:3], 1):
    print(f"\n  Row {i}:")
    print(f"    FIPS: {row['fips']}")
    print(f"    County: {row['county']}, {row['state']}")
    print(f"    Year: {row['year']}")
    non_empty = [k for k, v in row.items() if k not in ['fips', 'county', 'state', 'year'] and v != '']
    print(f"    Metrics available: {len(non_empty)}")

print("\n" + "=" * 60)
print("DONE! Refresh your browser to see all counties filled in!")
print("=" * 60)


