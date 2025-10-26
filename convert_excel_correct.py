"""
Correct converter for County Health Rankings Excel file
Uses exact column names from the file
"""

import pandas as pd
import numpy as np

print("County Health Rankings Excel Converter (Corrected)")
print("=" * 60)

input_file = 'data/2025 County Health Rankings Data - v3.xlsx'
output_file = 'data/county_health_data.csv'

# Read both sheets
print("\nReading data sheets...")
df_select = pd.read_excel(input_file, sheet_name='Select Measure Data')
df_additional = pd.read_excel(input_file, sheet_name='Additional Measure Data')

# Set first row as column names
df_select.columns = df_select.iloc[0]
df_select = df_select.iloc[1:].reset_index(drop=True)

df_additional.columns = df_additional.iloc[0]
df_additional = df_additional.iloc[1:].reset_index(drop=True)

print(f"Select sheet: {len(df_select)} rows")
print(f"Additional sheet: {len(df_additional)} rows")

# Exact column mapping from the files
metrics_mapping = {
    # From Select Measure Data
    'select': {
        'Years of Potential Life Lost Rate': 'premature_death',
        '% Uninsured': 'uninsured',
        'Primary Care Physicians Rate': 'primary_care_rate',
        '% Fair or Poor Health': 'poor_health',
        'Average Number of Physically Unhealthy Days': 'poor_physical_days',
        'Average Number of Mentally Unhealthy Days': 'poor_mental_days',
        '% Vaccinated': 'vaccinated',
        '% With Access to Exercise Opportunities': 'exercise_access',
        'Preventable Hospitalization Rate': 'preventable_hosp',
        '% with Annual Mammogram': 'mammogram_rate',
        'Average Daily PM2.5': 'air_pollution',
        '% Severe Housing Problems': 'housing_problems',
    },
    # From Additional Measure Data
    'additional': {
        'Life Expectancy': 'life_expectancy',
        '% Adults with Obesity': 'adult_obesity',
        '% Adults with Diabetes': 'diabetes',
        '% Adults Reporting Currently Smoking': 'adult_smoking',
        'Median Household Income': 'median_income',
        'High School Graduation Rate': 'hs_graduation',
        '% Physically Inactive': 'physical_inactivity',
        '% Excessive Drinking': 'excessive_drinking',
        '% Children in Poverty': 'child_poverty',
        '80th Percentile Income': 'income_80th',
        '20th Percentile Income': 'income_20th',
        '% Some College': 'some_college',
        'Unemployment Rate': 'unemployment',
    }
}

# Build output
output_data = []

for idx, row in df_select.iterrows():
    fips = str(row['FIPS']).strip()
    
    # Skip invalid FIPS
    if len(fips) != 5 or not fips.isdigit() or fips.endswith('000'):
        continue
    
    output_row = {
        'fips': fips,
        'county': str(row['County']).strip(),
        'state': str(row['State']).strip(),
        'year': 2024
    }
    
    # Add metrics from Select sheet
    for col_name, output_name in metrics_mapping['select'].items():
        if col_name in df_select.columns:
            try:
                value = pd.to_numeric(row[col_name], errors='coerce')
                output_row[output_name] = value if pd.notna(value) else ''
            except:
                output_row[output_name] = ''
    
    output_data.append(output_row)

# Convert to DataFrame
df_output = pd.DataFrame(output_data)

# Add metrics from Additional sheet
print("\nMerging Additional Measure Data...")
for col_name, output_name in metrics_mapping['additional'].items():
    if col_name in df_additional.columns:
        print(f"  Adding: {col_name} -> {output_name}")
        
        for idx, row in df_additional.iterrows():
            fips = str(row['FIPS']).strip()
            
            if len(fips) == 5 and fips.isdigit():
                try:
                    value = pd.to_numeric(row[col_name], errors='coerce')
                    if pd.notna(value):
                        mask = df_output['fips'] == fips
                        if mask.any():
                            df_output.loc[mask, output_name] = value
                except:
                    pass

print(f"\n[SUCCESS] Processed {len(df_output)} counties")

# Data completeness
print(f"\n[OK] Data completeness by metric:")
metrics_stats = []
for col in df_output.columns:
    if col not in ['fips', 'county', 'state', 'year']:
        non_empty = (df_output[col] != '').sum()
        pct = (non_empty / len(df_output)) * 100
        metrics_stats.append((col, non_empty, pct))
        print(f"  {col:25s}: {non_empty:4d} ({pct:5.1f}%)")

# Save
df_output.to_csv(output_file, index=False)

print(f"\n[SUCCESS] Saved to {output_file}")
print(f"  Total counties: {len(df_output)}")
print(f"  Total metrics: {len([c for c in df_output.columns if c not in ['fips','county','state','year']])}")

# Show best metrics
print(f"\n[OK] Metrics with best coverage (>90%):")
for col, count, pct in sorted(metrics_stats, key=lambda x: -x[2])[:10]:
    if pct > 90:
        print(f"  {col:25s}: {pct:5.1f}%")

print("\n" + "=" * 60)
print("DONE! Update JavaScript and refresh browser!")
print("=" * 60)


