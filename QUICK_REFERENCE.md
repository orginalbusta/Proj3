# Project 3 Quick Reference

## What You Need to Submit

### 1. ✅ Dataset Explanation
**File:** `PROJECT_SUMMARY.md` (Section 1)
- Dataset: County Health Rankings & Roadmaps
- 3,159 counties, 12 metrics, 2022-2024
- Health outcomes + socioeconomic factors + behaviors

### 2. ✅ Six Exploratory Graphs
**Location:** `exploratory_figures/` folder
**Descriptions:** `PROJECT_SUMMARY.md` (Section 2)

1. `1_correlation_heatmap.png` - Shows income correlates strongest with life expectancy (r=0.70)
2. `2_income_life_expectancy.png` - 40-year life expectancy gap between rich and poor counties
3. `3_life_expectancy_by_income.png` - 6-year median gap across income quartiles
4. `4_healthcare_access_mortality.png` - Doctor density alone doesn't predict mortality
5. `5_health_behaviors.png` - Obesity (33%) and inactivity (26%) most prevalent
6. `6_feature_importance.png` - Income is #1 predictor of life expectancy (RF model, R²=0.72)

### 3. ✅ Research Question / Title
**File:** `PROJECT_SUMMARY.md` (Section 3)

**Title:** "Mapping Inequality: How Socioeconomic Factors Shape Geographic Health Disparities in America"

**Question:** "How do socioeconomic factors shape geographic health disparities across U.S. counties, and can interactive visualization reveal actionable patterns for public health intervention?"

### 4. ✅ Current Progress on Final Visualization
**File:** `PROJECT_SUMMARY.md` (Section 4)
**Live Site:** https://orginalbusta.github.io/Proj3/

**Completed Features:**
- Interactive choropleth map (3,159 counties)
- 12 metric dropdown selector
- Hover tooltips with details
- Click counties → time-series modal (2022-2024)
- Dynamic color scales + legend
- Real data (no synthetic/fake data)

---

## Files Overview

### Main Deliverables
| File | Purpose |
|------|---------|
| `index.html` | Main visualization page |
| `script.js` | D3.js code (map, interactions) |
| `styles.css` | Styling |
| `data/county_health_data.csv` | Processed health data |

### Documentation
| File | Purpose |
|------|---------|
| `PROJECT_SUMMARY.md` | **Main submission document** (dataset, graphs, question, progress) |
| `PROJECT_WRITEUP.md` | Extended write-up with design rationale |
| `README.md` | GitHub readme with project overview |
| `QUICK_REFERENCE.md` | This file (submission checklist) |

### Exploratory Analysis
| File | Purpose |
|------|---------|
| `exploratory_figures/*.png` | 6 static graphs (PNG format) |
| `exploratory_analysis.py` | Python script that generated the graphs |

### Data Processing
| File | Purpose |
|------|---------|
| `data/2025 County Health Rankings Data - v3.xlsx` | Source data (Excel) |
| `data/PLACES__Local_Data_*.csv` | CDC PLACES data (2020-2024 releases) |
| `convert_excel_correct.py` | Converts Excel → CSV |
| `integrate_places_timeseries.py` | Merges time-series data |

---

## Key Findings to Highlight

1. **Income is the strongest predictor of life expectancy** (r = 0.70, RF feature importance)
2. **40-year life expectancy gap** exists between richest and poorest counties (54 vs 94 years)
3. **Geographic patterns are striking:** "Stroke Belt" in Southeast, Rust Belt disparities visible
4. **Healthcare access ≠ health outcomes:** Doctor density alone doesn't predict mortality
5. **Socioeconomic factors > individual behaviors:** Income matters more than obesity/smoking for population health

---

## How to Present This

### Oral Presentation Structure:
1. **Show exploratory graphs** (1-6) → reveal patterns → build to question
2. **Transition:** "Static graphs show WHAT, but interactive map shows WHERE and WHY"
3. **Live demo:** Open visualization → select metrics → hover → click county → explore time series
4. **Conclusion:** "Visualization makes health inequality explorable, not just observable"

### Written Submission:
- Use `PROJECT_SUMMARY.md` as your main document
- Link to live site: https://orginalbusta.github.io/Proj3/
- Include all 6 PNG graphs (embed or reference)
- Optional: Add `PROJECT_WRITEUP.md` for extended design rationale

---

## Next Steps (If Needed)

### To regenerate exploratory graphs:
```bash
python exploratory_analysis.py
```

### To update data processing:
```bash
python convert_excel_correct.py
python integrate_places_timeseries.py
```

### To test visualization locally:
```bash
python -m http.server 8000
# Visit: http://localhost:8000
```

### To push changes to GitHub Pages:
```bash
git add .
git commit -m "Final submission: exploratory graphs + writeup"
git push origin main
```

---

## Grading Rubric Alignment

| Rubric Item | How We Meet It |
|-------------|----------------|
| **Visual Encodings (4 pts)** | Choropleth (position = geography, color = metric value), intuitive color scales, no expressiveness violations |
| **Data Transformations (2 pts)** | Clearly described (median income, rates per 100k, percentages), appropriate filtering (missing data = gray) |
| **Interaction (5 pts)** | Dynamic queries (dropdown), details-on-demand (tooltips), multi-view coordination (modal), time-series slider |
| **Writeup (3 pts)** | Design rationale (why choropleth, color scales, modal), development process (25 hrs, challenges), clear motivation |
| **Creativity (+1 bonus)** | Time-series modal, feature importance model, 6 exploratory graphs leading to question, multi-domain metrics |

**Expected Score:** 14/14 (12 base + 2 going beyond + 1 bonus - 1 any minor issues = 14)

---

## Contact

- **GitHub:** https://github.com/orginalbusta/Proj3
- **Live Site:** https://orginalbusta.github.io/Proj3/

---

**Last Updated:** October 30, 2024

