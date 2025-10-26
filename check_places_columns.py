import pandas as pd

for year in [2020, 2021, 2022, 2023, 2024]:
    df = pd.read_csv(f'data/PLACES__Local_Data_for_Better_Health,_County_Data_{year}_release_20251026.csv', nrows=5)
    print(f"{year} columns: {list(df.columns)}")
    print()


