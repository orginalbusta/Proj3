"""
Convert County Health Rankings Excel file to visualization format
This should have ALL the metrics including socioeconomic data
"""

import pandas as pd
import os

print("County Health Rankings Excel Converter")
print("=" * 60)

input_file = 'data/2025 County Health Rankings Data - v3.xlsx'
output_file = 'data/county_health_data.csv'

print(f"\nAnalyzing: {input_file}")

# First, check what sheets are available
xl_file = pd.ExcelFile(input_file)
print(f"\nAvailable sheets: {xl_file.sheet_names}")

# Usually the data is in a sheet called "Ranked Measure Data" or similar
# Let's try to find the right sheet
for sheet in xl_file.sheet_names[:5]:
    print(f"\nChecking sheet: {sheet}")
    try:
        df = pd.read_excel(input_file, sheet_name=sheet, nrows=5)
        print(f"  Columns: {list(df.columns)[:10]}")
        print(f"  Shape: {df.shape}")
    except Exception as e:
        print(f"  Error: {e}")

print("\n" + "=" * 60)
print("Looking for the main data sheet...")

# Common sheet names for CHR data
data_sheet_candidates = [
    'Ranked Measure Data',
    'Additional Measure Data', 
    'Outcomes & Factors Rankings',
    'Data',
    'Sheet1'
]

data_sheet = None
for sheet in xl_file.sheet_names:
    if any(candidate.lower() in sheet.lower() for candidate in data_sheet_candidates):
        data_sheet = sheet
        break

if data_sheet is None:
    # Just use the first sheet that looks like data
    data_sheet = xl_file.sheet_names[0]

print(f"Using sheet: {data_sheet}")

# Read the data
df = pd.read_excel(input_file, sheet_name=data_sheet)
print(f"\nLoaded {len(df)} rows, {len(df.columns)} columns")

# Show first few columns
print(f"\nFirst 10 columns: {list(df.columns)[:10]}")

# Show a sample row
print(f"\nSample row (first 10 fields):")
for col in df.columns[:10]:
    print(f"  {col}: {df[col].iloc[0]}")


