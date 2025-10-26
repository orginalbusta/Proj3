# County Health Rankings: Interactive Visualization

## Project Overview

This is an interactive data visualization project using the **County Health Rankings & Roadmaps** dataset. The visualization enables county-by-county, year-by-year exploration of health outcomes across the United States.

**Live Demo:** *(To be deployed on GitHub Pages)*

## Features

- **Interactive Choropleth Map**: Color-coded counties based on selected health metrics
- **Temporal Navigation**: Year slider to explore trends from 2014-2024
- **Dynamic Filters**: Select different health metrics and filter by state
- **Details-on-Demand**: Hover tooltips showing detailed county statistics
- **Zoom & Pan**: Interactive exploration of geographic regions
- **Real-time Statistics**: Automatically calculated insights for displayed data

## Technologies Used

- **D3.js v7**: For data visualization and DOM manipulation
- **TopoJSON**: For efficient geographic data representation
- **Vanilla JavaScript**: No frameworks, pure JS implementation
- **HTML5 & CSS3**: Modern, responsive design

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
├── index.html              # Main HTML file
├── script.js               # D3.js visualization code
├── styles.css              # Styling
├── data/                   # Data directory
│   └── county_health_data.csv
├── explore_data.py         # Data exploration script
├── convert_data.py         # Data conversion utility
├── DATA_GUIDE.md          # Guide for downloading data
└── README.md              # This file
```

## Getting Started

### Prerequisites

- Modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3.x (for data processing scripts)
- Git (for version control)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Proj3.git
   cd Proj3
   ```

2. **Download the data**
   
   Option A: Use sample data (already included)
   ```bash
   # Sample data is already created in data/county_health_data.csv
   ```

   Option B: Download real data from County Health Rankings
   - Visit: https://www.countyhealthrankings.org/health-data
   - Download the national data files
   - Run the conversion script:
   ```bash
   python convert_data.py
   ```

3. **Open the visualization**
   ```bash
   # Simply open index.html in your browser
   # Or use a local server:
   python -m http.server 8000
   # Then visit: http://localhost:8000
   ```

## Data Processing

### Exploring the Data

Run the exploration script to understand your data:

```bash
python explore_data.py
```

This will:
- Analyze CSV structure
- Identify key columns
- Show sample data
- Provide recommendations

### Converting Data

To convert downloaded County Health Rankings data:

```bash
python convert_data.py
```

Follow the prompts to:
- Analyze your data files
- Map columns to required format
- Create D3.js-compatible CSV

See `DATA_GUIDE.md` for detailed instructions.

## Usage

### Basic Navigation

1. **Select a Year**: Use the slider to navigate through different years
2. **Choose a Metric**: Select from the dropdown to visualize different health indicators
3. **Filter by State**: Optionally focus on specific states
4. **Hover for Details**: Mouse over counties to see detailed information
5. **Zoom & Pan**: Click and drag to pan, scroll to zoom
6. **Reset**: Click the reset button to return to default view

### Interpreting the Visualization

- **Darker colors** typically indicate higher values (or worse outcomes for negative metrics)
- **Lighter colors** indicate lower values (or better outcomes for negative metrics)
- **Gray counties** have no data available for the selected metric/year
- **State boundaries** are shown in bold lines

## Deployment to GitHub Pages

### Setup

1. **Ensure your repository is public**

2. **Enable GitHub Pages**
   - Go to repository Settings
   - Navigate to Pages section
   - Select "main" branch
   - Choose "/ (root)" folder
   - Save

3. **Your site will be live at:**
   ```
   https://YOUR_USERNAME.github.io/Proj3/
   ```

### Updating

Simply push changes to the main branch:
```bash
git add .
git commit -m "Update visualization"
git push origin main
```

GitHub Pages will automatically update within a few minutes.

## Development

### Project Requirements (from Assignment)

- ✅ Use only D3.js (no high-level plotting libraries)
- ✅ Enable interactive exploration
- ✅ Deploy to GitHub Pages
- ✅ Include design rationale writeup
- ✅ Document development process

### Interaction Techniques Implemented

1. **Dynamic Queries**: Year and metric selection filters
2. **Details-on-Demand**: Hover tooltips
3. **Zoom & Pan**: Geographic navigation
4. **Coordinated Views**: Map updates with filter changes
5. **Visual Feedback**: Hover highlights

## Team Information

**Team Members:**
- [Your Name] - [Your Role]
- [Team Member 2] - [Their Role]
- [Team Member 3] - [Their Role]
- [Team Member 4] - [Their Role]

**Development Time:** 
- Approximately [X] person-hours
- Most time spent on: Data cleaning, D3.js map implementation, interaction design

## Design Decisions

### Why Choropleth Map?

We chose a choropleth map because:
- **Geographic Context**: Health outcomes are strongly tied to location
- **Pattern Recognition**: Easy to identify regional trends and disparities
- **Familiarity**: Users are comfortable with geographic representations
- **Scalability**: Can show all U.S. counties simultaneously

### Visual Encodings

- **Color**: Sequential scheme for quantitative data
- **Position**: Geographic coordinates (latitude/longitude)
- **Boundaries**: Distinguish states and counties

### Interaction Design

- **Progressive Disclosure**: Show overview first, details on demand
- **Immediate Feedback**: Real-time updates on interaction
- **Multiple Perspectives**: Different metrics reveal different patterns
- **Temporal Comparison**: Year slider enables trend analysis

### Alternatives Considered

1. **Scatter Plot Matrix**: Would show correlations but lose geography
2. **Small Multiples**: Could show multiple years but reduce detail
3. **Animated Transitions**: Auto-play through years (decided user control is better)
4. **Bubble Map**: Would emphasize specific counties but create visual clutter

## Data Source

Data from [County Health Rankings & Roadmaps](https://www.countyhealthrankings.org/health-data), a collaboration between the Robert Wood Johnson Foundation and the University of Wisconsin Population Health Institute.

## License

This project is for educational purposes as part of a data visualization course.

## Acknowledgments

- County Health Rankings & Roadmaps for the dataset
- D3.js community for excellent documentation and examples
- Mike Bostock for TopoJSON and U.S. Atlas

## Resources

- [D3.js Documentation](https://d3js.org/)
- [County Health Rankings](https://www.countyhealthrankings.org/)
- [TopoJSON](https://github.com/topojson/topojson)
- [U.S. Atlas](https://github.com/topojson/us-atlas)

---

**Course:** Data Visualization  
**Assignment:** Project 3 - Interactive Visualization  
**Date:** October 2024
