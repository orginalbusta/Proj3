import pandas as pd

print("Adding unemployment column...")

# Read Excel
df_select = pd.read_excel('data/2025 County Health Rankings Data - v3.xlsx', sheet_name='Select Measure Data')
df_select.columns = df_select.iloc[0]
df_select = df_select.iloc[1:]

# Read CSV
df_csv = pd.read_csv('data/county_health_data.csv')
df_csv['unemployment'] = ''

# Add unemployment data
for idx, row in df_select.iterrows():
    fips = str(row['FIPS']).strip().zfill(5)
    if len(fips) == 5 and not fips.endswith('000'):
        val = pd.to_numeric(row['% Unemployed'], errors='coerce')
        if pd.notna(val):
            mask = df_csv['fips'] == fips
            if mask.any():
                df_csv.loc[mask, 'unemployment'] = val

# Save
df_csv.to_csv('data/county_health_data.csv', index=False)

print(f"Added unemployment column!")
print(f"Counties with unemployment data: {(df_csv['unemployment'] != '').sum()}")


