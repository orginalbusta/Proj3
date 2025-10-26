# Data Guide

## Data Sources

### Primary Dataset
**County Health Rankings & Roadmaps** - 2025 Release (v3)
- Website: https://www.countyhealthrankings.org/health-data
- File: `2025 County Health Rankings Data - v3.xlsx`

### Time Series Dataset
**CDC PLACES** (Local Data for Better Health)
- Website: https://www.cdc.gov/places/
- Files: County-level data releases (2020-2024)

## Data Processing

The visualization uses pre-processed data in `data/county_health_data.csv`.

### To Regenerate Data

If you need to regenerate the data from source files:

1. Place source data files in the `data/` folder:
   - `2025 County Health Rankings Data - v3.xlsx`
   - CDC PLACES county data CSV files

2. Run the data processing scripts:
```bash
# Process CHR 2024 baseline
python convert_excel_correct.py

# Integrate PLACES time series data
python integrate_places_timeseries.py
```

## Data Coverage

- **Counties**: 3,159 U.S. counties
- **Years**: 2022-2024 (time series in county click modal)
- **Metrics**: 13+ health and socioeconomic indicators

### 2022 Data (Real Historical)
- Source: CDC PLACES
- Metrics: Adult obesity, smoking, diabetes, physical inactivity, etc.
- Coverage: 99.5% of counties

### 2023-2024 Data
- Source: County Health Rankings 2024
- All metrics available
- Coverage: 100% of counties

## License

Data is publicly available from County Health Rankings & Roadmaps and CDC PLACES.
