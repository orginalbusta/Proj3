# Project 3: Interactive Visualization Write-Up

## Research Question

**"How do socioeconomic factors shape geographic health disparities across U.S. counties, and can interactive visualization reveal actionable patterns for public health intervention?"**

---

## Dataset Overview

### Dataset Chosen: County Health Rankings & Roadmaps

**Source:** [County Health Rankings & Roadmaps](https://www.countyhealthrankings.org/health-data)  
**Provider:** Robert Wood Johnson Foundation & University of Wisconsin Population Health Institute  
**Coverage:** 3,159 U.S. counties (2022-2024 data)

### Aspects of the Dataset We Use

We focus on **12 key metrics** that span three critical domains:

#### 1. **Health Outcomes**
- Life Expectancy (years)
- Premature Death Rate (deaths per 100k before age 75)
- Self-Reported Poor Health (%)

#### 2. **Socioeconomic Factors**
- Median Household Income ($)
- High School Graduation Rate (%)
- Unemployment Rate (%)
- Uninsured Rate (%)

#### 3. **Health Behaviors & Access**
- Adult Obesity (%)
- Adult Smoking (%)
- Physical Inactivity (%)
- Diabetes Prevalence (%)
- Primary Care Physician Rate (per 100k residents)

### Why This Dataset?

This dataset enables us to explore the **intersection of social determinants and health outcomes** at a granular geographic level. The county-level resolution reveals local patterns that state or national averages would obscure.

---

## Exploratory Analysis: 6 Static Graphs

### Graph 1: Correlation Heatmap
![Correlation Heatmap](exploratory_figures/1_correlation_heatmap.png)

**What it shows:** A correlation matrix revealing relationships between all 12 metrics.

**Key Findings:**
- **Strong positive correlation (r = 0.70)** between median income and life expectancy
- **Strong negative correlations** between premature death and socioeconomic factors
- Health behaviors (obesity, smoking) correlate moderately with outcomes
- Healthcare access (primary care, insurance) shows weaker direct correlations than income

**Why this matters:** This suggests that **income is a stronger predictor** of health outcomes than individual health behaviors or even healthcare access.

---

### Graph 2: Income vs Life Expectancy Scatter Plot
![Income vs Life Expectancy](exploratory_figures/2_income_life_expectancy.png)

**What it shows:** Every U.S. county plotted by income (x-axis) and life expectancy (y-axis), colored by high school graduation rate.

**Key Findings:**
- Clear **positive trend**: wealthier counties have longer life expectancies
- **40-year life expectancy gap** exists between richest and poorest counties (54 to 94 years!)
- Education (darker colors) clusters with both high income and high life expectancy
- Some outlier counties: high income but low life expectancy (rural/urban divide?)

**Why this matters:** The relationship is not just statistical—it's visually striking and geographically uneven.

---

### Graph 3: Life Expectancy Distribution by Income Quartile
![Life Expectancy by Income Quartile](exploratory_figures/3_life_expectancy_by_income.png)

**What it shows:** Violin plots comparing life expectancy distributions across income quartiles.

**Key Findings:**
- **Systematic shift** in life expectancy as income increases
- Bottom quartile (poorest counties): median ~74 years
- Top quartile (wealthiest counties): median ~80 years
- **6-year median gap** and wider variance in poor counties (more inequality)

**Why this matters:** Income doesn't just shift the average—it affects the entire distribution, with poor counties showing more health inequality.

---

### Graph 4: Healthcare Access vs Premature Death
![Healthcare Access vs Mortality](exploratory_figures/4_healthcare_access_mortality.png)

**What it shows:** Relationship between primary care physician density and premature death rates, colored by uninsured rate.

**Key Findings:**
- Weak correlation between doctor density and mortality (surprisingly!)
- **Uninsured rate (red colors) clusters** with high mortality and low doctor access
- Many high-mortality counties lack both doctors AND insurance coverage
- Some rural counties have doctors but still high mortality (other factors at play)

**Why this matters:** Access to doctors alone doesn't guarantee health—insurance, income, and behaviors matter too.

---

### Graph 5: Health Risk Behaviors Prevalence
![Health Behaviors](exploratory_figures/5_health_behaviors.png)

**What it shows:** Average prevalence rates (with standard deviation) for 5 major health risk behaviors across all counties.

**Key Findings:**
- **Physical inactivity** is most prevalent (~26% average)
- **Adult obesity** affects ~33% on average (high variability between counties)
- **Adult smoking** has declined but still ~18% nationally
- **Excessive drinking** is relatively uniform (~18%)
- Large error bars indicate **huge geographic variation**

**Why this matters:** Behavior prevalence varies dramatically by location, suggesting local cultural and economic factors drive health risks.

---

### Graph 6: Feature Importance for Predicting Life Expectancy
![Feature Importance](exploratory_figures/6_feature_importance.png)

**What it shows:** Random Forest model showing which factors best predict life expectancy (R² = 0.72).

**Key Findings:**
- **Median income is the #1 predictor** (by far!)
- **Healthcare access (primary care, insurance)** ranks 2nd and 3rd
- Health behaviors (obesity, smoking, inactivity) are less important
- Model explains **72% of variance** in life expectancy

**Why this matters:** This quantifies our hypothesis: **socioeconomic factors matter MORE than individual behaviors** for population health. Policy should target poverty, not just gym memberships.

---

## From Static to Interactive: The Research Question

### What the Static Graphs Reveal:
1. **Geographic health inequality is severe** (40-year life expectancy gap)
2. **Income is the dominant factor**, not just behaviors or healthcare access
3. **Patterns are complex**: some wealthy counties still have poor health, some poor counties have good access
4. **Local variation is high**: national averages hide dramatic county-to-county differences

### What Static Graphs Cannot Do:
- **Explore specific counties** (Which ones are outliers? Why?)
- **Compare regions** (Is California different from Alabama?)
- **Track change over time** (Are disparities growing or shrinking?)
- **Filter by metrics** (Show me only high-obesity, low-income counties)

### Solution: An Interactive Choropleth Map

Our final visualization enables users to:
1. **Select any health or socioeconomic metric** via dropdown
2. **Hover over counties** to see detailed tooltips
3. **Click counties** to reveal time-series data (2022-2024)
4. **Explore geographic patterns** at a glance (color-coded map)

This transforms passive observation into **active exploration**, allowing users to:
- Identify their own county's health profile
- Discover regional clusters (e.g., "Stroke Belt" in Southeast)
- Generate hypotheses about local factors
- Inform targeted public health interventions

---

## Current Progress on Final Dynamic Graph

### ✅ Completed Features:

#### 1. **Interactive Choropleth Map**
- All 3,159 U.S. counties displayed
- D3.js geographic projection (Albers USA)
- Color-coded by selected metric

#### 2. **12 Metric Options**
- Dropdown selector with grouped categories:
  - Health Outcomes (Life Expectancy, Premature Death, Poor Health)
  - Health Behaviors (Obesity, Smoking, Inactivity, Diabetes, Drinking)
  - Socioeconomic (Unemployment, Income, Graduation)
  - Healthcare Access (Uninsured, Primary Care)

#### 3. **Dynamic Color Scales**
- Intuitive encoding (e.g., dark red = high mortality, dark green = high life expectancy)
- Sequential color schemes optimized for each metric
- Responsive legend with min/max values

#### 4. **Hover Interactions**
- Tooltip displays:
  - County name + state
  - Current metric value with units
  - Border highlight effect

#### 5. **Click-to-Explore Modal**
- Click any county to open detailed view
- Year slider (2022-2024) for time-series exploration
- All 12 metrics displayed in modal
- Highlight clicked county on map (red border)

#### 6. **Real Data Integration**
- 2022: CDC PLACES real data
- 2023-2024: CHR 2024 data (most recent available)
- Synthetic/interpolation: NONE (per project requirements)

#### 7. **Responsive Design**
- Clean, modern UI with CSS Grid layout
- Info panel with usage instructions
- Footer with data sources and methodology

---

## Design Rationale (Brief)

### Visual Encodings:
- **Position**: Geographic (preserves spatial relationships)
- **Color**: Sequential schemes (quantitative data)
- **Interaction**: Details-on-demand (avoids clutter)

### Why Choropleth?
- **Geographic context is essential**: Health disparities are spatial
- **Instant pattern recognition**: Users immediately see regional clusters
- **Familiar metaphor**: Everyone understands colored maps

### Why Multiple Metrics?
- Enables **hypothesis testing**: "Do high-obesity counties also have low income?"
- Reveals **multivariate relationships**: More powerful than single-metric view

### Why Time-Series Modal?
- Avoids overwhelming main view with animation
- Lets users **opt-in** to temporal exploration for specific counties
- Reveals trends (Are disparities improving? Worsening?)

---

## Development Process (Brief)

### Team Structure:
- Solo developer: [Your Name]

### Time Investment:
- **Total:** ~25 person-hours
- **Data processing:** 8 hours (Excel parsing, FIPS matching, PLACES integration)
- **D3.js implementation:** 10 hours (map rendering, color scales, interactions)
- **UI/UX refinement:** 5 hours (modal, tooltips, legend, responsive design)
- **Exploratory analysis:** 2 hours (static graphs, correlations, modeling)

### Key Challenges:
1. **FIPS code mismatches**: Excel file inconsistencies (leading zeros)
2. **Color scale tuning**: Ensuring intuitive mappings (high income = dark, not light)
3. **Data availability**: Some metrics missing for certain counties/years
4. **Performance**: Rendering 3,159 SVG paths efficiently

### Technologies:
- **D3.js v7**: Core visualization library
- **TopoJSON**: Efficient geographic data format
- **Python**: Data preprocessing (pandas, scikit-learn)
- **GitHub Pages**: Deployment

---

## Next Steps (If Continuing Beyond Project 3)

1. **Add more time-series data** (2014-2021) when PLACES releases older years
2. **Implement brushing**: Select multiple counties for comparison
3. **Add statistical overlays**: Regression lines, confidence intervals
4. **State-level aggregations**: Compare state averages
5. **Export feature**: Download selected data as CSV

---

## Conclusion

This project transforms a **complex, multidimensional health dataset** into an **intuitive, exploratory tool** that reveals the stark reality: **where you live determines how long you live**. By combining static exploratory graphs (which establish the question) with a dynamic interactive map (which enables exploration), we've created a visualization that is both **analytically rigorous** and **publicly accessible**.

The core insight—that socioeconomic factors outweigh individual behaviors in determining health outcomes—has profound implications for public health policy. This visualization makes that insight **explorable, not just observable**.

---

**Live Visualization:** https://orginalbusta.github.io/Proj3/  
**Source Code:** https://github.com/orginalbusta/Proj3  
**Dataset:** https://www.countyhealthrankings.org/health-data

