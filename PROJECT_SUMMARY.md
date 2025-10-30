# Exploring Health Inequality Across America

---

## The Dataset

**County Health Rankings & Roadmaps (2024)**  
**Source:** Robert Wood Johnson Foundation & University of Wisconsin Population Health Institute  
**URL:** https://www.countyhealthrankings.org/health-data

This dataset covers **3,159 U.S. counties** with comprehensive health and socioeconomic data. I focused on **12 key metrics** across different aspects of community health:

| Category | Metrics |
|----------|---------|
| **Health Outcomes** | Life Expectancy, Premature Death Rate, Poor Health % |
| **Socioeconomic** | Median Income, HS Graduation %, Uninsured % |
| **Health Behaviors** | Adult Obesity %, Smoking %, Physical Inactivity %, Diabetes %, Excessive Drinking % |
| **Healthcare Access** | Primary Care Physician Rate (per 100k residents) |

---

## Exploratory Visualizations

### Graph 1: Correlation Heatmap
![Correlation Heatmap](exploratory_figures/1_correlation_heatmap.png)

**What it shows:** How different health and socioeconomic factors relate to each other.

**Key Finding:** Median income has the strongest correlation with life expectancy (r = 0.70). Health behaviors and healthcare access show weaker direct correlations.

**Why it matters:** Economic factors appear more important than individual health choices for predicting how long people live.

---

### Graph 2: Income vs Life Expectancy Scatter
![Income vs Life Expectancy](exploratory_figures/2_income_life_expectancy.png)

**What it shows:** All 3,159 U.S. counties plotted by median income and life expectancy, colored by high school graduation rates.

**Key Finding:** A stunning **40-year life expectancy gap** exists between the richest and poorest counties (54 to 94 years). Education levels (darker colors) cluster with both high income and longevity.

**Why it matters:** Where you live—and your community's wealth—dramatically affects how long you'll live.

---

### Graph 3: Life Expectancy by Income Level
![Life Expectancy by Income Quartile](exploratory_figures/3_life_expectancy_by_income.png)

**What it shows:** Life expectancy distributions across four income groups (poorest to wealthiest counties).

**Key Finding:** A systematic **6-year median gap** between the poorest and wealthiest counties. Poor counties also show wider variance, meaning more inequality within those communities.

**Why it matters:** Income affects not just the average, but creates broader health disparities in poorer areas.

---

### Graph 4: Healthcare Access vs Premature Death
![Healthcare Access vs Mortality](exploratory_figures/4_healthcare_access_mortality.png)

**What it shows:** Relationship between doctor availability and premature death rates, colored by uninsured percentage.

**Key Finding:** Doctor density alone doesn't strongly predict mortality. The counties with highest death rates tend to have both low doctor availability AND high uninsured rates.

**Why it matters:** Healthcare infrastructure requires both providers and insurance coverage to make a difference.

---

### Graph 5: Health Risk Behaviors
![Health Behaviors](exploratory_figures/5_health_behaviors.png)

**What it shows:** Average prevalence of major health risk behaviors across all counties.

**Key Finding:** Physical inactivity (~26%) and obesity (~33%) are most prevalent. The large error bars show huge variation between counties.

**Why it matters:** Health behaviors vary dramatically by location, likely driven by local economic and cultural factors.

---

### Graph 6: What Predicts Life Expectancy?
![Feature Importance](exploratory_figures/6_feature_importance.png)

**What it shows:** A machine learning model (Random Forest) ranking which factors best predict life expectancy. The model explains 72% of the variance.

**Key Finding:** **Median income is by far the strongest predictor**, followed by healthcare access measures. Individual health behaviors rank lower.

**Why it matters:** This quantifies what the other graphs suggest—economic factors drive population health more than personal health choices.

---

## The Big Question

**"How do socioeconomic factors shape geographic health disparities across America?"**

### What the Static Graphs Show:
- Health inequality is severe (40-year life expectancy gap)
- Income is the dominant factor, not just individual behaviors
- Patterns are complex with high local variation
- National averages hide dramatic county-to-county differences

### What They Can't Show:
- Which specific counties are outliers and why
- How regions compare (California vs Alabama?)
- Local patterns within states
- Easy filtering and comparison

---

## The Interactive Solution

I built an interactive choropleth map that lets you:
- **Select any metric** from the 12 available
- **Hover over counties** for detailed information
- **Click counties** to explore multiple metrics at once
- **See geographic patterns** instantly with color coding

This transforms static observation into active exploration.

**Live visualization:** https://orginalbusta.github.io/Proj3/

---

## How to Use It

**Example 1: "How healthy is my county?"**
- Find your county on the map
- Select different metrics to see how it compares
- Click your county to see all 12 metrics at once

**Example 2: "Where are health disparities worst?"**
- Select "Life Expectancy"
- Look for the lightest-colored counties
- Compare with "Median Income" to see the connection

**Example 3: "Does wealth equal health everywhere?"**
- Select "Median Income" to see wealthy counties (dark blue)
- Switch to "Premature Death" to see mortality
- Find outliers—wealthy counties with poor health outcomes

---

## Key Findings

### The Numbers:
- **Counties analyzed:** 3,159 (covers 99% of U.S. population)
- **Life expectancy range:** 54.0 - 94.2 years (40-year gap!)
- **Income range:** $28,579 - $173,655 median household
- **Income-longevity correlation:** r = 0.70 (very strong)

### The Insight:
Where you live—specifically, your community's economic resources—is a stronger predictor of health outcomes than individual choices like diet and exercise. This suggests that addressing health inequality requires economic policy, not just health education.

---

## Design Choices

**Why a choropleth map?**
- Geographic context is essential—health disparities are inherently spatial
- Regional patterns emerge immediately
- Everyone understands colored maps

**Why multiple metrics?**
- Enables comparison (e.g., "Do high-obesity counties also have low income?")
- Reveals relationships between economic and health factors

**Why click-to-explore instead of animation?**
- Less overwhelming than constant change
- Lets you dig deeper into counties you care about
- More information density without clutter

**Why sequential color scales?**
- More intuitive than diverging scales for this data
- Consistent logic: darker = more intense (whether good or bad)

---

## Links

- **Interactive Map:** https://orginalbusta.github.io/Proj3/
- **Source Code:** https://github.com/orginalbusta/Proj3
- **Data Source:** https://www.countyhealthrankings.org/health-data
