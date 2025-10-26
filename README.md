# County Health Rankings: Interactive Visualization

## Project Overview

This is an interactive data visualization project using the **County Health Rankings & Roadmaps** dataset. The visualization enables county-by-county, year-by-year exploration of health outcomes across the United States.

## Health Metrics

The visualization includes the following health indicators:

### Health Outcomes
- Life Expectancy
- Premature Death Rate

### Health Behaviors  
- Adult Obesity
- Adult Smoking
- Physical Inactivity
- Diabetes Prevalence

### Social & Economic Factors
- Unemployment Rate
- Median Household Income
- High School Graduation Rate

### Clinical Care
- Uninsured Rate
- Primary Care Physician Rate

## Project Structure

```
Proj3/
├── index.html                      # Main HTML file
├── script.js                       # D3.js visualization code
├── styles.css                      # Styling
├── data/                           # Data directory
│   └── county_health_data.csv     # Processed data (22,113 rows)
├── convert_excel_correct.py        # CHR Excel data processor
├── integrate_places_timeseries.py  # PLACES time series integrator
├── DATA_GUIDE.md                   # Data source information
└── README.md                       # This file
```

## Features

- **Interactive Choropleth Map**: Color-coded counties by health metric
- **County Click Modal**: Click any county to explore time series data (2022-2024)
- **Year Slider**: Navigate through years to see trends
- **Metric Selector**: Switch between 13+ health indicators
- **Zoom & Pan**: Explore specific regions in detail
- **Tooltips**: Hover for quick county statistics

## Getting Started

1. **View the Visualization**
   ```bash
   # Start a local server
   python -m http.server 8000
   ```
   Then open `http://localhost:8000` in your browser

2. **Interact with the Map**
   - Click on any county to see detailed time series data
   - Use the metric selector to change what's displayed
   - Zoom and pan to explore specific regions
   - Hover over counties for quick statistics

## Data Source

Data from [County Health Rankings & Roadmaps](https://www.countyhealthrankings.org/health-data), a collaboration between the Robert Wood Johnson Foundation and the University of Wisconsin Population Health Institute.

---

**Course:** Data Visualization 209R
**Assignment:** Project 3 - Interactive Visualization  
**Date:** October 2024
