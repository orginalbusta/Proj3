"""
Integrate REAL PLACES data with correct year mapping
PLACES release files contain data from 2 years prior!
"""

import pandas as pd

print("=" * 70)
print("INTEGRATING REAL PLACES DATA (Correct Year Mapping)")
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

# Map release files to the data years they contain (using the MOST RECENT year in each file)
places_file_mapping = {
    2018: ('2020_release', 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2020_release_20251026.csv'),
    2019: ('2021_release', 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2021_release_20251026.csv'),
    2020: ('2022_release', 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2022_release_20251026.csv'),
    2021: ('2023_release', 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2023_release_20251026.csv'),
    2022: ('2024_release', 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2024_release_20251026.csv'),
}

# State abbreviation mapping
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

all_years_data = []

# Process years 2018-2022 (the years we have PLACES data for)
for data_year, (release_name, filepath) in sorted(places_file_mapping.items()):
    print(f"\n[3.{data_year}] Processing {release_name} (contains {data_year} data)...")
    
    # Load PLACES data
    df = pd.read_csv(filepath, low_memory=False)
    
    # Filter to the specific year and measures we care about
    df = df[(df['Year'] == data_year) & (df['Measure'].isin(PLACES_MAPPING.keys()))]
    
    print(f"    Raw rows after filtering: {len(df)}")
    
    # Format FIPS codes
    if 'LocationID' in df.columns:
        df['fips'] = df['LocationID'].astype(str).str.zfill(5)
        pivot_index = ['fips', 'LocationName', 'StateAbbr']
    else:
        # For 2018 (2020_release), match by county name
        df['county_state_key'] = df['LocationName'].str.strip() + '|' + df['StateAbbr'].str.strip()
        pivot_index = ['county_state_key', 'LocationName', 'StateAbbr']
    
    # Pivot to get one row per county
    pivot_df = df.pivot_table(
        index=pivot_index,
        columns='Measure',
        values='Data_Value',
        aggfunc='first'
    ).reset_index()
    
    # Rename columns
    pivot_df = pivot_df.rename(columns=PLACES_MAPPING)
    
    # Start with CHR 2024 structure
    year_df = chr_2024[['fips', 'county', 'state']].copy()
    year_df['year'] = data_year
    
    # Merge PLACES data
    if 'fips' in pivot_df.columns:
        # Direct FIPS match
        merge_cols = ['fips'] + [c for c in PLACES_MAPPING.values() if c in pivot_df.columns]
        year_df = year_df.merge(
            pivot_df[merge_cols],
            on='fips',
            how='left'
        )
    else:
        # Match by county name and state (for 2018)
        year_df['state_abbr'] = year_df['state'].map(state_abbr_map)
        year_df['county_name'] = year_df['county'].str.replace(' County', '').str.replace(' Parish', '').str.strip()
        year_df['match_key'] = year_df['county_name'] + '|' + year_df['state_abbr']
        
        pivot_df_match = pivot_df.rename(columns={'county_state_key': 'match_key'})
        merge_cols = ['match_key'] + [c for c in PLACES_MAPPING.values() if c in pivot_df_match.columns]
        year_df = year_df.merge(
            pivot_df_match[merge_cols],
            on='match_key',
            how='left'
        )
        year_df = year_df.drop(columns=['state_abbr', 'county_name', 'match_key'])
    
    # Add CHR 2024 metrics that PLACES doesn't have
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
    
    # Count coverage
    places_coverage = {metric: year_df[metric].notna().sum() for metric in PLACES_MAPPING.values() if metric in year_df.columns}
    print(f"    Data coverage: {places_coverage}")
    
    all_years_data.append(year_df)

# Add years 2023-2024 using CHR 2024 data (no PLACES data available yet)
print(f"\n[4] Adding 2023-2024 (using CHR 2024 data, PLACES not available)")
for year in [2023, 2024]:
    year_df = chr_2024.copy()
    year_df['year'] = year
    all_years_data.append(year_df)
    print(f"    Added {year} with CHR 2024 values")

# Combine all years
combined_df = pd.concat(all_years_data, ignore_index=True)
combined_df = combined_df.sort_values(['fips', 'year'])

# Ensure FIPS is 5-digit string
combined_df['fips'] = combined_df['fips'].astype(str).str.zfill(5)

print(f"\n[5] Final combined dataset:")
print(f"    Total rows: {len(combined_df):,}")
print(f"    Years: {sorted(combined_df['year'].unique())}")
print(f"    Counties: {combined_df['fips'].nunique()}")

# Save
combined_df.to_csv('data/county_health_data.csv', index=False)

print(f"\n[SUCCESS] Real historical data integrated!")
print(f"\nData breakdown:")
print(f"  - 2018-2022: REAL PLACES historical data")
print(f"  - 2023-2024: CHR 2024 values (PLACES data not yet available)")
print(f"  - All years: CHR 2024 for socioeconomic metrics (no historical source)")
print("=" * 70)

# Verify
print(f"\n[6] Data quality check:")
sample_fips = '06037'  # Los Angeles
sample_data = combined_df[combined_df['fips'] == sample_fips][['year', 'adult_obesity', 'diabetes', 'life_expectancy']].sort_values('year')
print(f"\n    Los Angeles County (06037):")
print(sample_data.to_string(index=False))

