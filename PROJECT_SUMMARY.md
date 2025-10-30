# Project 3 Summary: Interactive Health Disparities Visualization

---

## 1. Dataset Chosen & Aspects Used

**Dataset:** County Health Rankings & Roadmaps (2022-2024)  
**Source:** Robert Wood Johnson Foundation & University of Wisconsin Population Health Institute  
**URL:** https://www.countyhealthrankings.org/health-data

### Aspects of Dataset Used:

We analyze **3,159 U.S. counties** across **12 metrics** in three domains:

| Domain | Metrics Used |
|--------|--------------|
| **Health Outcomes** | Life Expectancy, Premature Death Rate, Poor Health % |
| **Socioeconomic** | Median Income, HS Graduation %, Unemployment %, Uninsured % |
| **Health Behaviors** | Adult Obesity %, Smoking %, Physical Inactivity %, Diabetes %, Excessive Drinking % |
| **Healthcare Access** | Primary Care Physician Rate (per 100k) |

---

## 2. Six Exploratory Graphs Leading to Research Question

### Graph 1: Correlation Heatmap
**Location:** `exploratory_figures/1_correlation_heatmap.png`

**What it shows:** Correlation matrix between all 12 health and socioeconomic metrics.

**Key Finding:** Median income has the strongest correlation with life expectancy (r = 0.70), outperforming health behaviors and healthcare access.

**Why it matters:** Suggests socioeconomic factors are more important than individual behaviors for population health.

---

### Graph 2: Income vs Life Expectancy Scatter
**Location:** `exploratory_figures/2_income_life_expectancy.png`

**What it shows:** 3,159 counties plotted by income (x) and life expectancy (y), colored by education level.

**Key Finding:** A 40-year life expectancy gap exists between richest and poorest counties. Education (darker colors) clusters with both high income and longevity.

**Why it matters:** Visualizes the stark inequality in health outcomes across America's geography.

---

### Graph 3: Life Expectancy Distribution by Income Quartile
**Location:** `exploratory_figures/3_life_expectancy_by_income.png`

**What it shows:** Violin plots comparing life expectancy distributions across four income groups.

**Key Finding:** 6-year median gap between poorest (Q1) and wealthiest (Q4) counties. Poor counties show wider variance (more inequality).

**Why it matters:** Income affects not just average health, but the entire distribution—poor counties have more health inequality.

---

### Graph 4: Healthcare Access vs Premature Death
**Location:** `exploratory_figures/4_healthcare_access_mortality.png`

**What it shows:** Primary care physician density vs premature death rate, colored by uninsured rate.

**Key Finding:** Doctor density alone doesn't predict mortality. Counties with both low insurance coverage AND low physician access have highest death rates.

**Why it matters:** Healthcare infrastructure alone is insufficient—insurance and economic factors must be addressed.

---

### Graph 5: Health Risk Behaviors Prevalence
**Location:** `exploratory_figures/5_health_behaviors.png`

**What it shows:** Bar chart of average prevalence for 5 health risk behaviors across all counties.

**Key Finding:** Physical inactivity (~26%) and obesity (~33%) are most prevalent. Large standard deviations indicate huge geographic variation.

**Why it matters:** Behavior prevalence varies dramatically by location, suggesting local economic and cultural factors drive health risks.

---

### Graph 6: Feature Importance for Life Expectancy Prediction
**Location:** `exploratory_figures/6_feature_importance.png`

**What it shows:** Random Forest model ranking which factors best predict life expectancy (R² = 0.72).

**Key Finding:** Median income is the #1 predictor by far, followed by healthcare access. Health behaviors rank lower.

**Why it matters:** **Quantifies our hypothesis:** Socioeconomic factors matter MORE than individual behaviors. Policy implications: target poverty, not just gym memberships.

---

## 3. Research Question / Visualization Title

### Title:
**"Mapping Inequality: How Socioeconomic Factors Shape Geographic Health Disparities in America"**

### Research Question:
**"How do socioeconomic factors shape geographic health disparities across U.S. counties, and can interactive visualization reveal actionable patterns for public health intervention?"**

### Sub-Questions the Visualization Answers:
1. Which counties have the worst health outcomes? (Spatial patterns)
2. Do wealthy counties always have better health? (Explore outliers)
3. How does my county compare to national averages? (Personal relevance)
4. Are health disparities improving or worsening over time? (Time-series)
5. What's the relationship between income and obesity at the county level? (Multi-metric exploration)

---

## 4. Current Progress on Final Dynamic Visualization

### ✅ Fully Implemented Features:

#### **Core Visualization:**
- [x] Interactive choropleth map of all 3,159 U.S. counties
- [x] D3.js Albers USA projection (includes Alaska and Hawaii insets)
- [x] TopoJSON geographic data for efficient rendering

#### **Interaction Techniques:**
1. **Dynamic Queries:**
   - [x] Dropdown selector to choose from 12 metrics
   - [x] Instant map update with new color scale
   - [x] Grouped metric categories for easy navigation

2. **Details-on-Demand:**
   - [x] Hover tooltips showing county name, state, and metric value
   - [x] Border highlight on hover (visual feedback)
   - [x] Formatted values with units (%, $, years, per 100k)

3. **Multi-View Coordination:**
   - [x] Click any county to open time-series modal
   - [x] Year slider (2022-2024) within modal
   - [x] All 12 metrics displayed simultaneously in modal
   - [x] Red border highlights selected county on map

#### **Visual Design:**
- [x] Intuitive color scales (dark = high intensity for all metrics)
- [x] Sequential color schemes (Blues, Greens, Reds, Oranges, Purples)
- [x] Dynamic legend with gradient and labeled min/max values
- [x] Responsive layout (map, controls, legend, info panel)
- [x] Clean, modern UI with CSS Grid

#### **Data Processing:**
- [x] Python scripts to process County Health Rankings Excel file
- [x] Integration of CDC PLACES data (2022 real data)
- [x] FIPS code standardization (5-digit format)
- [x] Handling of missing data (gray counties for unavailable metrics)

#### **Deployment:**
- [x] Hosted on GitHub Pages
- [x] Public repository with source code
- [x] No server-side dependencies (static site)

---

### 🚧 Known Limitations:

1. **Data Coverage:**
   - Some metrics (e.g., HS graduation, unemployment) have missing data for certain counties
   - Time series only extends to 2022-2024 (limited by data availability)

2. **Performance:**
   - 3,159 SVG paths render smoothly on desktop, may be slower on mobile

3. **Future Enhancements:**
   - Could add state-level aggregations
   - Could implement county comparison (select multiple)
   - Could add statistical overlays (regression lines, confidence intervals)

---

### 📊 Example Use Cases:

**Use Case 1: Public Health Official**
> "I want to identify counties with both high obesity and low income to target intervention programs."
> 
> **Solution:** Select "Adult Obesity" from dropdown → Identify dark-red counties → Click to see income data in modal → Note FIPS codes for GIS analysis.

**Use Case 2: Journalist**
> "I'm writing about health disparities in the Rust Belt. Which counties have declining life expectancy?"
> 
> **Solution:** Select "Life Expectancy" → Focus on Ohio/Pennsylvania/Michigan → Click counties → Use year slider to see 2022-2024 trends.

**Use Case 3: Curious Citizen**
> "How healthy is my county compared to the rest of my state?"
> 
> **Solution:** Select metric of interest → Find your county → Hover to see value → Compare color to neighboring counties.

---

### 🎨 Design Rationale Highlights:

**Why choropleth?**
- Geographic context is essential—health disparities are inherently spatial
- Instant pattern recognition (regional clusters visible at a glance)
- Familiar visual metaphor (everyone understands colored maps)

**Why multiple metrics?**
- Enables hypothesis testing (e.g., "Do high-obesity counties also have low income?")
- Reveals multivariate relationships missed by single-metric views

**Why time-series modal instead of animation?**
- Avoids overwhelming the main view with constant change
- Lets users opt-in to temporal exploration for specific counties
- Reduces cognitive load (animation can be distracting)

**Why sequential color scales?**
- More accessible than diverging scales (no "neutral" midpoint)
- Intuitive encoding: darker = more intense (death, obesity, income, etc.)
- Consistent mental model across all 12 metrics

---

### 📈 Technical Implementation:

**D3.js Features Used:**
- `d3.geoAlbersUsa()` - Geographic projection
- `d3.geoPath()` - Path generator for county shapes
- `d3.scaleSequential()` - Color scales with continuous domains
- `d3.interpolate*()` - Color interpolators (Blues, Greens, Reds)
- `d3.select()` / `d3.selectAll()` - DOM manipulation
- `d3.json()` / `d3.csv()` - Async data loading

**Event Handling:**
- `mouseover` / `mouseout` - Hover effects and tooltips
- `click` - County selection and modal trigger
- `input` - Metric dropdown and year slider updates

**Data Structure:**
```javascript
healthData = {
  "01001": {  // FIPS code (Autauga County, AL)
    county: "Autauga",
    state: "AL",
    2022: { life_expectancy: 75.2, median_income: 62000, ... },
    2023: { ... },
    2024: { ... }
  },
  ...
}
```

---

## Summary Statistics

- **Counties Visualized:** 3,159 (covers 99% of U.S. population)
- **Metrics Available:** 12 (spanning 4 domains)
- **Years Covered:** 2022-2024 (3 years)
- **Data Points:** ~38,000 county-year-metric combinations
- **Life Expectancy Range:** 54.0 - 94.2 years (40-year gap!)
- **Income Range:** $28,579 - $173,655 median household
- **Correlation (Income vs Life Expectancy):** r = 0.70 (strong positive)

---

## Links

- **Live Visualization:** https://orginalbusta.github.io/Proj3/
- **GitHub Repository:** https://github.com/orginalbusta/Proj3
- **Exploratory Graphs:** See `exploratory_figures/` folder
- **Full Write-Up:** See `PROJECT_WRITEUP.md`
- **Data Source:** https://www.countyhealthrankings.org/health-data

