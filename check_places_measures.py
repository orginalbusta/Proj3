import pandas as pd

df = pd.read_csv('data/PLACES__Local_Data_for_Better_Health,_County_Data_2024_release_20251026.csv')
print('All unique measures in PLACES:')
for m in sorted(df['Measure'].unique()):
    print(f'  - {m}')


