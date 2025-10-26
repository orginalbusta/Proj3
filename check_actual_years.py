import pandas as pd

files = {
    '2020_release': 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2020_release_20251026.csv',
    '2021_release': 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2021_release_20251026.csv',
    '2022_release': 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2022_release_20251026.csv',
    '2023_release': 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2023_release_20251026.csv',
    '2024_release': 'data/PLACES__Local_Data_for_Better_Health,_County_Data_2024_release_20251026.csv',
}

for name, filepath in files.items():
    df = pd.read_csv(filepath, nrows=5000)
    years = sorted(df['Year'].unique())
    print(f"{name:15s} contains data years: {years}")


