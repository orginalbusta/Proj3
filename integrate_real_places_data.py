"""
Integrate REAL PLACES data (2020-2024) with County Health Rankings data
NO SYNTHETIC DATA - only real historical values
"""

import pandas as pd
import numpy as np

print("=" * 70)
print("INTEGRATING REAL PLACES DATA (2020-2024)")
print("=" * 70)

# Load the 2024 CHR baseline
chr_2024 = pd.read_csv('data/county_health_data.csv', dtype={'fips': str})
chr_2024 = chr_2024[chr_2024['year'] == 2024].copy()
print(f"\n[1] Loaded CHR 2024 baseline: {len(chr_2024)} counties")

# Mapping PLACES measures to our metric names
PLACES_MAPPING = {
    'Obesity among adults': 'adult_obesity',
    'Current cigarette smoking among adults': 'adult_smoking',
    'No leisure-time physical activity among adults': 'physical_inactivity',
    'Diagnosed diabetes among adults': 'diabetes',
    'Binge drinking among adults': 'excessive_drinking',
    'Fair or poor self-rated health status among adults': 'poor_health',
    'Current lack of health insurance among adults aged 18-64 years': 'uninsured',
}

print(f"\n[2] PLACES measures mapped:")
for places_name, our_name in PLACES_MAPPING.items():
    print(f"    {our_name:25s} <- {places_name}")

# Load and process each PLACES file (2020-2024)
places_files = {
    2020: 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2020_release_20251026.csv',
    2021: 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2021_release_20251026.csv',
    2022: 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2022_release_20251026.csv',
    2023: 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2023_release_20251026.csv',
    2024: 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2024_release_20251026.csv',
}

all_years_data = []

for year, filepath in sorted(places_files.items()):
    print(f"\n[3.{year}] Processing PLACES {year} data...")
    
    # Load PLACES data
    df = pd.read_csv(filepath, low_memory=False)
    
    # Filter to only measures we care about
    df = df[df['Measure'].isin(PLACES_MAPPING.keys())]
    
    # Format FIPS codes (pad to 5 digits)
    # Note: 2020 file doesn't have LocationID, we'll match by county+state
    if 'LocationID' in df.columns:
        df['fips'] = df['LocationID'].astype(str).str.zfill(5)
    else:
        # For 2020, we'll create a temporary key to match later
        df['county_state_key'] = df['LocationName'].str.strip() + '|' + df['StateAbbr'].str.strip()
    
    # Pivot to get one row per county with columns for each metric
    if 'fips' in df.columns:
        pivot_df = df.pivot_table(
            index=['fips', 'LocationName', 'StateAbbr'],
            columns='Measure',
            values='Data_Value',
            aggfunc='first'
        ).reset_index()
    else:
        # For 2020: pivot by county_state_key
        pivot_df = df.pivot_table(
            index=['county_state_key', 'LocationName', 'StateAbbr'],
            columns='Measure',
            values='Data_Value',
            aggfunc='first'
        ).reset_index()
    
    # Rename columns according to our mapping
    pivot_df = pivot_df.rename(columns=PLACES_MAPPING)
    pivot_df = pivot_df.rename(columns={'LocationName': 'county_name', 'StateAbbr': 'state_abbr'})
    
    # Start with CHR 2024 structure
    year_df = chr_2024[['fips', 'county', 'state']].copy()
    year_df['year'] = year
    
    # Merge PLACES data
    if 'fips' in pivot_df.columns:
        # Direct FIPS match for 2021-2024
        year_df = year_df.merge(
            pivot_df[[col for col in pivot_df.columns if col not in ['county_name', 'state_abbr']]],
            on='fips',
            how='left'
        )
    else:
        # For 2020: match by county name and state
        # Create state abbreviation mapping from CHR data
        state_abbr_map = {
            'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
            'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
            'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
            'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
            'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
            'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
            'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
            'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
            'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
            'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
            'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY', 'District of Columbia': 'DC'
        }
        year_df['state_abbr'] = year_df['state'].map(state_abbr_map)
        year_df['county_name'] = year_df['county'].str.replace(' County', '').str.strip()
        year_df['match_key'] = year_df['county_name'] + '|' + year_df['state_abbr']
        
        pivot_df_match = pivot_df.rename(columns={'county_state_key': 'match_key'})
        year_df = year_df.merge(
            pivot_df_match[[col for col in pivot_df_match.columns if col not in ['county_name', 'state_abbr']]],
            on='match_key',
            how='left'
        )
        year_df = year_df.drop(columns=['state_abbr', 'county_name', 'match_key'])
    
    # For metrics NOT in PLACES, use CHR 2024 values
    # (life_expectancy, premature_death, median_income, hs_graduation, unemployment, primary_care_rate)
    chr_only_metrics = [
        'life_expectancy', 'premature_death', 'median_income', 
        'hs_graduation', 'unemployment', 'primary_care_rate',
        'poor_physical_days', 'poor_mental_days', 'vaccinated',
        'exercise_access', 'preventable_hosp', 'mammogram_rate',
        'air_pollution', 'housing_problems'
    ]
    
    for metric in chr_only_metrics:
        if metric in chr_2024.columns:
            year_df[metric] = chr_2024[metric].values
    
    print(f"    Counties with data: {year_df['fips'].nunique()}")
    print(f"    PLACES metrics filled: {pivot_df.shape[0]} counties")
    
    all_years_data.append(year_df)

# Combine all years
combined_df = pd.concat(all_years_data, ignore_index=True)
combined_df = combined_df.sort_values(['fips', 'year'])

# Ensure FIPS is 5-digit string
combined_df['fips'] = combined_df['fips'].astype(str).str.zfill(5)

print(f"\n[4] Final combined dataset:")
print(f"    Total rows: {len(combined_df):,}")
print(f"    Years: {sorted(combined_df['year'].unique())}")
print(f"    Counties: {combined_df['fips'].nunique()}")
print(f"    Columns: {list(combined_df.columns)}")

# Save
combined_df.to_csv('data/county_health_data.csv', index=False)

print(f"\n[SUCCESS] Real historical data integrated!")
print(f"\nData breakdown:")
print(f"  - 2020-2024: REAL PLACES data for health behaviors")
print(f"  - All years: CHR 2024 values for socioeconomic metrics")
print(f"    (life expectancy, premature death, income, education, etc.)")
print(f"\n  Note: CHR doesn't provide historical data for these socioeconomic")
print(f"        metrics, so 2024 values are used across all years.")
print("=" * 70)

# Verify data quality
print(f"\n[5] Data quality check:")
sample_fips = combined_df['fips'].iloc[0]
sample_data = combined_df[combined_df['fips'] == sample_fips][['year', 'adult_obesity', 'diabetes', 'life_expectancy']]
print(f"\n    Sample county ({sample_fips}):")
print(sample_data.to_string(index=False))

