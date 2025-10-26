"""
Full converter for County Health Rankings Excel file
Extracts all major health and socioeconomic metrics
"""

import pandas as pd
import numpy as np

print("County Health Rankings Full Excel Converter")
print("=" * 60)

input_file = 'data/2025 County Health Rankings Data - v3.xlsx'
output_file = 'data/county_health_data.csv'

# Read both data sheets
print("\nReading Select Measure Data sheet...")
df_select = pd.read_excel(input_file, sheet_name='Select Measure Data')

print("\nReading Additional Measure Data sheet...")
df_additional = pd.read_excel(input_file, sheet_name='Additional Measure Data')

print(f"\nSelect Measure Data: {df_select.shape}")
print(f"Additional Measure Data: {df_additional.shape}")

# The first row contains the actual headers
# Extract FIPS, State, County from first 3 columns
df_select.columns = df_select.iloc[0]
df_select = df_select.iloc[1:].reset_index(drop=True)

df_additional.columns = df_additional.iloc[0]
df_additional = df_additional.iloc[1:].reset_index(drop=True)

# Get core columns
fips_col = df_select.columns[0]
state_col = df_select.columns[1]
county_col = df_select.columns[2]

print(f"\nCore columns: {fips_col}, {state_col}, {county_col}")

# Metrics to extract - looking for specific column names
metrics_to_find = {
    # Health Outcomes
    'Years of Potential Life Lost Rate': 'premature_death',
    'Life Expectancy': 'life_expectancy',
    'Poor or Fair Health': 'poor_health',
    'Poor Physical Health Days': 'poor_physical_days',
    'Poor Mental Health Days': 'poor_mental_days',
    
    # Health Behaviors
    'Adult Obesity': 'adult_obesity',
    'Adult Smoking': 'adult_smoking',
    'Physical Inactivity': 'physical_inactivity',
    'Diabetes Prevalence': 'diabetes',
    'Excessive Drinking': 'excessive_drinking',
    
    # Clinical Care
    'Uninsured': 'uninsured',
    'Primary Care Physicians': 'primary_care_rate',
    'Preventable Hospital Stays': 'preventable_hosp',
    'Flu Vaccinations': 'flu_vaccinations',
    
    # Social & Economic Factors
    'Unemployment': 'unemployment',
    'Children in Poverty': 'child_poverty',
    'Income Inequality': 'income_inequality',
    'Median Household Income': 'median_income',
    'High School Completion': 'hs_graduation',
    'Some College': 'some_college',
    
    # Physical Environment
    'Air Pollution - Particulate Matter': 'air_pollution',
    'Severe Housing Problems': 'housing_problems',
}

# Find columns in both dataframes
found_metrics = {}

# Check Select Measure Data
for metric_name, output_name in metrics_to_find.items():
    if metric_name in df_select.columns:
        found_metrics[output_name] = ('select', metric_name)
        print(f"  Found in Select: {metric_name} -> {output_name}")

# Check Additional Measure Data  
for metric_name, output_name in metrics_to_find.items():
    if output_name not in found_metrics and metric_name in df_additional.columns:
        found_metrics[output_name] = ('additional', metric_name)
        print(f"  Found in Additional: {metric_name} -> {output_name}")

print(f"\nFound {len(found_metrics)} metrics")

# Build output dataframe
output_data = []

for idx, row in df_select.iterrows():
    fips = str(row[fips_col]).strip()
    
    # Skip if not a valid FIPS code
    if len(fips) != 5 or not fips.isdigit():
        continue
    
    # Skip state-level aggregates (FIPS ending in 000)
    if fips.endswith('000'):
        continue
    
    output_row = {
        'fips': fips,
        'county': str(row[county_col]).strip(),
        'state': str(row[state_col]).strip(),
        'year': 2024  # This is 2024-2025 data
    }
    
    # Extract metrics from Select sheet
    for output_name, (source, metric_name) in found_metrics.items():
        if source == 'select':
            value = row[metric_name]
            # Convert to numeric, handling any issues
            try:
                value = pd.to_numeric(value, errors='coerce')
                output_row[output_name] = value if pd.notna(value) else ''
            except:
                output_row[output_name] = ''
        else:
            output_row[output_name] = ''  # Will fill from additional later
    
    output_data.append(output_row)

# Convert to DataFrame
df_output = pd.DataFrame(output_data)

# Add metrics from Additional sheet
for output_name, (source, metric_name) in found_metrics.items():
    if source == 'additional':
        print(f"\nAdding {output_name} from Additional sheet...")
        
        # Match by FIPS
        for idx, row in df_additional.iterrows():
            fips = str(row[fips_col]).strip()
            
            if len(fips) == 5 and fips.isdigit():
                value = row[metric_name]
                try:
                    value = pd.to_numeric(value, errors='coerce')
                    if pd.notna(value):
                        mask = df_output['fips'] == fips
                        if mask.any():
                            df_output.loc[mask, output_name] = value
                except:
                    pass

print(f"\n[SUCCESS] Processed {len(df_output)} counties")

# Show data completeness
print(f"\n[OK] Data completeness by metric:")
for col in df_output.columns:
    if col not in ['fips', 'county', 'state', 'year']:
        non_empty = (df_output[col] != '').sum()
        pct = (non_empty / len(df_output)) * 100
        print(f"  {col:25s}: {non_empty:4d} counties ({pct:5.1f}%)")

# Save to CSV
df_output.to_csv(output_file, index=False)

print(f"\n[SUCCESS] Saved to {output_file}")
print(f"  Total rows: {len(df_output)}")
print(f"  Total metrics: {len([c for c in df_output.columns if c not in ['fips','county','state','year']])}")

# Show sample
print(f"\n[OK] Sample data:")
sample = df_output.head(3)
for idx, row in sample.iterrows():
    print(f"\n  {row['county']}, {row['state']} ({row['fips']})")
    metrics_with_data = [col for col in df_output.columns 
                        if col not in ['fips','county','state','year'] and row[col] != '']
    print(f"    Metrics with data: {len(metrics_with_data)}")

print("\n" + "=" * 60)
print("DONE! Refresh your browser to see the full data!")
print("=" * 60)


