"""
Create expanded sample data with more counties for better testing
"""

import csv
import random

# Expanded list of counties across the US
counties = [
    # California
    ('06001', 'Alameda', 'California'),
    ('06013', 'Contra Costa', 'California'),
    ('06037', 'Los Angeles', 'California'),
    ('06059', 'Orange', 'California'),
    ('06065', 'Riverside', 'California'),
    ('06067', 'Sacramento', 'California'),
    ('06071', 'San Bernardino', 'California'),
    ('06073', 'San Diego', 'California'),
    ('06075', 'San Francisco', 'California'),
    ('06085', 'Santa Clara', 'California'),
    
    # Texas
    ('48029', 'Bexar', 'Texas'),
    ('48113', 'Dallas', 'Texas'),
    ('48121', 'Denton', 'Texas'),
    ('48141', 'El Paso', 'Texas'),
    ('48201', 'Harris', 'Texas'),
    ('48215', 'Hidalgo', 'Texas'),
    ('48439', 'Tarrant', 'Texas'),
    ('48453', 'Travis', 'Texas'),
    
    # Florida
    ('12011', 'Broward', 'Florida'),
    ('12031', 'Duval', 'Florida'),
    ('12057', 'Hillsborough', 'Florida'),
    ('12086', 'Miami-Dade', 'Florida'),
    ('12095', 'Orange', 'Florida'),
    ('12099', 'Palm Beach', 'Florida'),
    ('12103', 'Pinellas', 'Florida'),
    
    # New York
    ('36005', 'Bronx', 'New York'),
    ('36047', 'Kings', 'New York'),
    ('36061', 'New York', 'New York'),
    ('36081', 'Queens', 'New York'),
    ('36103', 'Suffolk', 'New York'),
    ('36119', 'Westchester', 'New York'),
    
    # Pennsylvania
    ('42003', 'Allegheny', 'Pennsylvania'),
    ('42017', 'Bucks', 'Pennsylvania'),
    ('42045', 'Delaware', 'Pennsylvania'),
    ('42091', 'Montgomery', 'Pennsylvania'),
    ('42101', 'Philadelphia', 'Pennsylvania'),
    
    # Illinois
    ('17031', 'Cook', 'Illinois'),
    ('17043', 'DuPage', 'Illinois'),
    ('17097', 'Lake', 'Illinois'),
    ('17111', 'McHenry', 'Illinois'),
    ('17197', 'Will', 'Illinois'),
    
    # Ohio
    ('39035', 'Cuyahoga', 'Ohio'),
    ('39049', 'Franklin', 'Ohio'),
    ('39061', 'Hamilton', 'Ohio'),
    ('39093', 'Lorain', 'Ohio'),
    ('39113', 'Montgomery', 'Ohio'),
    
    # Georgia
    ('13067', 'Cobb', 'Georgia'),
    ('13089', 'DeKalb', 'Georgia'),
    ('13121', 'Fulton', 'Georgia'),
    ('13135', 'Gwinnett', 'Georgia'),
    
    # North Carolina
    ('37063', 'Durham', 'North Carolina'),
    ('37119', 'Mecklenburg', 'North Carolina'),
    ('37183', 'Wake', 'North Carolina'),
    
    # Michigan
    ('26049', 'Genesee', 'Michigan'),
    ('26081', 'Kent', 'Michigan'),
    ('26099', 'Macomb', 'Michigan'),
    ('26125', 'Oakland', 'Michigan'),
    ('26163', 'Wayne', 'Michigan'),
    
    # New Jersey
    ('34003', 'Bergen', 'New Jersey'),
    ('34013', 'Essex', 'New Jersey'),
    ('34017', 'Hudson', 'New Jersey'),
    ('34023', 'Middlesex', 'New Jersey'),
    
    # Virginia
    ('51013', 'Arlington', 'Virginia'),
    ('51059', 'Fairfax', 'Virginia'),
    ('51087', 'Henrico', 'Virginia'),
    ('51760', 'Richmond', 'Virginia'),
    
    # Washington
    ('53033', 'King', 'Washington'),
    ('53053', 'Pierce', 'Washington'),
    ('53061', 'Snohomish', 'Washington'),
    
    # Massachusetts
    ('25013', 'Hampden', 'Massachusetts'),
    ('25017', 'Middlesex', 'Massachusetts'),
    ('25021', 'Norfolk', 'Massachusetts'),
    ('25025', 'Suffolk', 'Massachusetts'),
    
    # Arizona
    ('04013', 'Maricopa', 'Arizona'),
    ('04019', 'Pima', 'Arizona'),
    
    # Tennessee
    ('47037', 'Davidson', 'Tennessee'),
    ('47157', 'Shelby', 'Tennessee'),
    
    # Indiana
    ('18097', 'Marion', 'Indiana'),
    
    # Missouri
    ('29095', 'Jackson', 'Missouri'),
    ('29189', 'St. Louis', 'Missouri'),
    
    # Wisconsin
    ('55025', 'Dane', 'Wisconsin'),
    ('55079', 'Milwaukee', 'Wisconsin'),
    
    # Colorado
    ('08001', 'Adams', 'Colorado'),
    ('08005', 'Arapahoe', 'Colorado'),
    ('08031', 'Denver', 'Colorado'),
    ('08035', 'Douglas', 'Colorado'),
    ('08059', 'Jefferson', 'Colorado'),
]

print(f"Creating expanded sample data with {len(counties)} counties...")

output_file = 'data/county_health_data.csv'
sample_data = []

# Generate data for each year
for year in range(2014, 2025):
    for fips, county_name, state_name in counties:
        # Use FIPS and year as seed for consistent but varied data
        random.seed(int(fips) + year)
        
        # Generate realistic-ish values with some regional patterns
        # Coastal/urban areas tend to have better outcomes
        urban_factor = 1.0 if fips[:2] in ['06', '36', '25', '53'] else 0.95
        
        row = {
            'fips': fips,
            'county': county_name,
            'state': state_name,
            'year': year,
            'life_expectancy': round((70 + random.random() * 15) * urban_factor, 1),
            'premature_death': round((2000 + random.random() * 8000) / urban_factor),
            'adult_obesity': round(20 + random.random() * 25, 1),
            'diabetes': round(8 + random.random() * 10, 1),
            'unemployment': round(2 + random.random() * 10, 1),
            'median_income': round((30000 + random.random() * 60000) * urban_factor),
            'adult_smoking': round(10 + random.random() * 15, 1),
            'physical_inactivity': round(15 + random.random() * 20, 1),
            'uninsured': round(5 + random.random() * 15, 1),
            'primary_care_rate': round(40 + random.random() * 60, 1),
            'hs_graduation': round(75 + random.random() * 20, 1),
        }
        
        sample_data.append(row)

# Write to CSV
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    fieldnames = list(sample_data[0].keys())
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sample_data)

print(f"[SUCCESS] Created expanded sample data!")
print(f"  File: {output_file}")
print(f"  Counties: {len(counties)}")
print(f"  Years: 2014-2024 (11 years)")
print(f"  Total rows: {len(sample_data)}")
print(f"\nStates covered:")
states = sorted(set(s for _, _, s in counties))
for state in states:
    count = len([c for c in counties if c[2] == state])
    print(f"  - {state}: {count} counties")
print(f"\nNOTE: This is still sample data for testing!")
print("Most US counties will still appear grey.")
print("Download real data from County Health Rankings for full coverage.")


