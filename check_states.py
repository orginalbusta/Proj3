import pandas as pd

df = pd.read_csv('data/county_health_data.csv')

states = ['California', 'Colorado', 'Arkansas', 'Alabama', 'Arizona']

print("Checking state data:\n")
for state in states:
    state_data = df[df['state'] == state]
    count = len(state_data)
    print(f'{state}: {count} counties')
    if count > 0:
        print(f'  Sample FIPS: {state_data["fips"].head(3).tolist()}')
        print(f'  Sample life_expectancy: {state_data["life_expectancy"].head(3).tolist()}')

print(f"\n\nAll unique states in CSV:")
print(sorted(df['state'].unique())[:20])


