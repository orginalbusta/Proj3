# County Health Rankings Data Guide

## How to Download the Data

### Step 1: Visit the Website
Go to: https://www.countyhealthrankings.org/health-data

### Step 2: Download National Data
1. Look for the "National Data & Documentation" section
2. Download the most recent year's data (typically available as Excel or CSV)
3. Look for trend files that contain historical data across multiple years

### Step 3: Recommended Files to Download
- **Analytic Data Files**: Contains detailed county-level metrics
- **Trend Files**: Multi-year data (ideal for your year-by-year visualization)
- **Data Dictionary**: Explains all the metrics and their calculations

### Step 4: File Organization
Place downloaded files in the `data/` directory:
```
Proj3/
  ├── data/
  │   ├── analytic_data_2024.csv
  │   ├── trend_data.csv
  │   └── data_dictionary.xlsx
  ├── index.html
  ├── script.js
  ├── styles.css
  └── explore_data.py
```

## Running the Data Exploration Script

### Prerequisites
Make sure you have Python installed. Then install required packages:
```bash
pip install pandas numpy
```

### Run the Exploration Script
```bash
python explore_data.py
```

This will:
- Analyze the structure of your downloaded CSV files
- Identify key columns (counties, years, metrics)
- Generate summary statistics
- Create recommendations for your visualization

## Converting Data for D3.js

After downloading the data, you'll need to convert it to a format suitable for D3.js.

### Option 1: Create a Python Conversion Script
Use the included `convert_data.py` script (see below)

### Option 2: Manual Conversion
If the data is not too large, you can:
1. Open the CSV in Excel or a text editor
2. Ensure it has these columns:
   - `fips` (5-digit county FIPS code)
   - `county` (county name)
   - `state` (state name)
   - `year` (year)
   - Health metrics (e.g., `life_expectancy`, `adult_obesity`, etc.)
3. Save as `county_health_data.csv` in the `data/` folder

## Key Metrics to Include

Based on the County Health Rankings dataset, prioritize these metrics:

### Health Outcomes
- **Life Expectancy** (years)
- **Premature Death** (years of potential life lost per 100,000)
- **Poor or Fair Health** (% of adults)
- **Poor Physical Health Days** (average per month)
- **Poor Mental Health Days** (average per month)

### Health Behaviors
- **Adult Obesity** (% of adults with BMI ≥ 30)
- **Physical Inactivity** (% of adults)
- **Excessive Drinking** (% of adults)
- **Adult Smoking** (% of adults)

### Clinical Care
- **Uninsured** (% of population)
- **Primary Care Physicians** (rate per 100,000)
- **Preventable Hospital Stays** (rate per 100,000)

### Social & Economic Factors
- **Unemployment** (% of population unemployed)
- **Children in Poverty** (% under age 18)
- **Income Inequality** (ratio)
- **Median Household Income** ($)
- **High School Completion** (%)
- **Some College** (%)

### Physical Environment
- **Air Pollution** (micrograms per cubic meter)
- **Severe Housing Problems** (%)
- **Driving Alone to Work** (%)

## Data Format Example

Your final CSV should look like:

```csv
fips,county,state,year,life_expectancy,premature_death,adult_obesity,diabetes,unemployment,median_income
01001,Autauga,Alabama,2024,75.8,8234,35.2,13.1,4.2,56562
01001,Autauga,Alabama,2023,75.6,8456,34.8,12.9,4.5,55234
01003,Baldwin,Alabama,2024,78.2,7123,31.4,11.2,3.8,62345
...
```

## FIPS Codes

County FIPS codes are 5-digit identifiers:
- First 2 digits: State code
- Last 3 digits: County code

Example: `06037` = California (06) + Los Angeles County (037)

You can find FIPS codes at: https://www.census.gov/library/reference/code-lists/ansi.html

## Next Steps

1. **Download the data** from County Health Rankings website
2. **Run explore_data.py** to understand the data structure
3. **Run convert_data.py** (or manually format) to create the final CSV
4. **Test the visualization** by opening `index.html` in a browser
5. **Iterate on the design** based on what patterns you discover

## Troubleshooting

### Problem: Data file is too large
**Solution**: Filter to specific states or years, or aggregate the data

### Problem: Missing FIPS codes
**Solution**: Use the state + county name to look up FIPS codes from Census data

### Problem: Inconsistent year ranges
**Solution**: Focus on years where most counties have data (typically recent years)

### Problem: Too many missing values
**Solution**: Either impute missing values or exclude those counties from visualization

## Resources

- **County Health Rankings**: https://www.countyhealthrankings.org/
- **D3.js Documentation**: https://d3js.org/
- **TopoJSON for US Maps**: https://github.com/topojson/us-atlas
- **FIPS Codes**: https://www.census.gov/geographies/reference-files/2020/demo/popest/2020-fips.html


