import pandas as pd

df = pd.read_csv('data/county_health_data.csv', dtype={'fips': str})

print("Data Coverage by Year:")
print("-" * 70)
for year in [2020, 2021, 2022, 2023, 2024]:
    year_df = df[df['year'] == year]
    print(f"\n{year}:")
    print(f"  Adult Obesity:       {year_df['adult_obesity'].notna().sum():,} / {len(year_df):,} ({year_df['adult_obesity'].notna().sum()/len(year_df)*100:.1f}%)")
    print(f"  Adult Smoking:       {year_df['adult_smoking'].notna().sum():,} / {len(year_df):,} ({year_df['adult_smoking'].notna().sum()/len(year_df)*100:.1f}%)")
    print(f"  Diabetes:            {year_df['diabetes'].notna().sum():,} / {len(year_df):,} ({year_df['diabetes'].notna().sum()/len(year_df)*100:.1f}%)")
    print(f"  Physical Inactivity: {year_df['physical_inactivity'].notna().sum():,} / {len(year_df):,} ({year_df['physical_inactivity'].notna().sum()/len(year_df)*100:.1f}%)")

# Check a few specific counties
print("\n" + "=" * 70)
print("Sample County Data (Jefferson County, Alabama - FIPS 01073):")
print("=" * 70)
sample = df[df['fips'] == '01073'][['year', 'adult_obesity', 'adult_smoking', 'diabetes', 'life_expectancy']].sort_values('year')
print(sample.to_string(index=False))

print("\n" + "=" * 70)
print("Sample County Data (Los Angeles County, California - FIPS 06037):")
print("=" * 70)
sample2 = df[df['fips'] == '06037'][['year', 'adult_obesity', 'adult_smoking', 'diabetes', 'life_expectancy']].sort_values('year')
print(sample2.to_string(index=False))


