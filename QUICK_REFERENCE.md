# Project 3 Quick Reference - Team Guide

## 🎯 Assignment Overview

**Goal:** Build an interactive D3.js visualization and deploy it on GitHub Pages  
**Dataset:** County Health Rankings & Roadmaps (2024)  
**Team Size:** 3-4 students  
**Points:** 14 total (12 for meeting requirements + up to 2 bonus)

---

## 📅 Deadlines

| Deadline | Deliverable |
|----------|-------------|
| **Wed 10/29, 11:59 PM** | Team Registration Form |
| **Fri 10/31, 11:59 PM** | Checkpoint Video (< 1 min MP4 with audio) |
| **TBD** | Final Submission |

---

## 🎥 Checkpoint Video Requirements (Due Fri 10/31)

**Format:** MP4 video, max 1 minute, with voiceover (not just text)

**Must Include:**
1. ✅ Team name and member names
2. ✅ Dataset chosen + aspects we plan to use
3. ✅ 5-6 exploratory graphs (static/dynamic)
4. ✅ Title/question we're answering
5. ✅ Current progress on final dynamic graph

### What We Have Ready:

#### 1. Dataset Explanation
- **Dataset:** County Health Rankings & Roadmaps (2024)
- **Coverage:** 3,159 U.S. counties
- **Aspects:** 12 metrics across health outcomes, socioeconomic factors, health behaviors, clinical care
- **Source:** `PROJECT_SUMMARY.md` - Section 1

#### 2. Six Exploratory Graphs
**Location:** `exploratory_figures/` folder

| Graph | File | Key Finding |
|-------|------|-------------|
| 1 | `1_correlation_heatmap.png` | Income strongest predictor (r=0.70) |
| 2 | `2_income_life_expectancy.png` | 40-year life expectancy gap |
| 3 | `3_life_expectancy_by_income.png` | 6-year median gap across quartiles |
| 4 | `4_healthcare_access_mortality.png` | Doctor density alone ≠ better outcomes |
| 5 | `5_health_behaviors.png` | Obesity (33%), inactivity (26%) most common |
| 6 | `6_feature_importance.png` | Income is #1 predictor (ML model, R²=0.72) |

#### 3. Research Question/Title
**Title:** "Mapping Inequality: How Socioeconomic Factors Shape Geographic Health Disparities in America"

**Question:** "How do socioeconomic factors shape geographic health disparities across U.S. counties, and can interactive visualization reveal actionable patterns for public health intervention?"

#### 4. Current Progress
- ✅ Interactive choropleth map (all 3,159 counties)
- ✅ D3.js implementation complete
- ✅ 12 metric dropdown selector
- ✅ Hover tooltips with details
- ✅ Click-to-explore modal
- ✅ Deployed on GitHub Pages
- **Live:** https://orginalbusta.github.io/Proj3/

---

## 📊 Final Deliverables Checklist

### Technical Requirements
- [x] **D3.js only** (no Vega-Lite/Plotly/Altair)
- [x] **GitHub Pages deployment** (repo is public)
- [x] **No server-side support** (static files only)
- [x] **Source code in repo** (unobfuscated)

### Visualization Requirements
- [x] **Interactive exploration** enabled
- [x] **Compelling question** addressed
- [x] **Focused design** (not sprawling)

### Interaction Techniques (need at least a few)
- [x] Dynamic query filters (metric dropdown)
- [x] Details-on-demand (tooltips)
- [x] Multi-view coordination (click modal)
- [ ] Panning/zooming (optional)
- [ ] Brushing (optional)
- [ ] Annotations/highlights (optional)

### Write-Up Requirements
Must include on webpage:
1. [ ] **Design rationale** (visual encodings, interaction techniques, alternatives considered)
2. [ ] **Development process** (work split, time spent, what took longest)

---

## 🎯 Grading Rubric & How We're Doing

### Visual Encodings (4 points max)
**Target:** "Does not violate expressiveness, clear/evocative design choices"

**Our Implementation:**
- ✅ Position = geographic location (preserves spatial meaning)
- ✅ Color = sequential scale for quantitative data
- ✅ No overplotting (counties don't overlap)
- ✅ Intuitive color schemes (dark = intense)

**Expected Score:** 4/4

---

### Data Transformations (2 points max)
**Target:** "Appropriate transformations, clearly described"

**Our Implementation:**
- ✅ Rates per 100k for comparability
- ✅ Percentages for prevalence
- ✅ Missing data handled (gray counties)
- ⚠️ Need to describe transformations in write-up

**Expected Score:** 2/2

---

### Interaction (5 points max)
**Target:** "Polished, bug-free, guides discovery of patterns"

**Our Implementation:**
- ✅ Dynamic queries (metric selector)
- ✅ Details-on-demand (hover tooltips)
- ✅ Multi-view coordination (click modal)
- ✅ Mostly bug-free
- ✅ Enables pattern discovery

**Expected Score:** 5/5

---

### Writeup (3 points max)
**Target:** "Clear motivation, design rationale, development process"

**Status:**
- ✅ Motivation is clear (health inequality)
- ✅ Design decisions documented
- ⚠️ Need to add development process section
- ⚠️ Need to add to main page or link prominently

**Expected Score:** 2-3/3

---

### Creativity Bonus (+1 possible)
**Target:** "Exceeds requirements, original insights, engaging"

**Our Strengths:**
- ✅ 6 exploratory graphs with ML model
- ✅ Feature importance analysis
- ✅ Multi-domain metrics (12 total)
- ✅ Clean, modern UI

**Expected Score:** +1 bonus

---

## 🎬 Suggested Video Script (60 seconds)

**[0-10s] Team Intro**
> "Hi, we're [Team Name]: [Names]. For Project 3, we're building an interactive health inequality visualization."

**[10-20s] Dataset**
> "We're using County Health Rankings 2024—3,159 counties with 12 metrics covering health outcomes, socioeconomic factors, behaviors, and clinical care."

**[20-40s] Exploratory Graphs**
> "We created 6 exploratory graphs [show images]. Key finding: income is the strongest predictor of life expectancy—a 40-year gap exists between richest and poorest counties. Our machine learning model confirms income matters more than individual health behaviors."

**[40-50s] Question**
> "Our question: How do socioeconomic factors shape geographic health disparities, and can interactive visualization reveal actionable patterns?"

**[50-60s] Progress**
> "We've completed the interactive D3.js map—click any county to explore. Live at [URL]. Next step: add comprehensive write-up."

---

## ✅ What's Complete

### Code
- `index.html` - Main page structure
- `script.js` - D3.js visualization logic
- `styles.css` - Styling
- `data/county_health_data.csv` - Processed dataset

### Analysis
- `exploratory_analysis.py` - Script that generated graphs
- `exploratory_figures/*.png` - 6 static visualizations

### Documentation
- `PROJECT_SUMMARY.md` - Overview (use for video)
- `PROJECT_WRITEUP.md` - Extended narrative
- `README.md` - GitHub landing page

---

## 🚧 What's Needed for Final Submission

### 1. Add Write-Up to Main Page
**Requirements:**
- Design rationale (why choropleth? why these colors? alternatives?)
- Development process (who did what? time spent? challenges?)

**Where to add:** 
- Option A: Add to `index.html` footer (below data source)
- Option B: Create separate `WRITEUP.html` and link prominently

**Template sections:**
```
Design Rationale:
- Why choropleth map? (geographic patterns essential)
- Why sequential colors? (intuitive for quantitative data)
- Why click modal vs animation? (less overwhelming)
- Alternatives considered? (scatter plot matrix, time series)

Development Process:
- [Member 1]: Data processing, exploratory analysis
- [Member 2]: D3.js implementation, interactions
- [Member 3]: UI/UX design, documentation
- Total time: ~[X] person-hours
- Biggest challenge: [FIPS code matching / color scale tuning / etc]
```

### 2. Test for Bugs
- [ ] Test all 12 metrics (any broken?)
- [ ] Test modal on various counties
- [ ] Test on different browsers
- [ ] Check mobile responsiveness

### 3. Polish
- [ ] Consistent formatting
- [ ] Proofread all text
- [ ] Verify all links work
- [ ] Add favicon (optional but nice)

---

## 📂 Repository Structure

```
Proj3/
├── index.html                    # Main page
├── script.js                     # D3.js code
├── styles.css                    # Styling
├── data/
│   ├── county_health_data.csv    # Main dataset
│   └── 2025 County Health Rankings Data - v3.xlsx  # Source
├── exploratory_figures/          # 6 PNG graphs for video
│   ├── 1_correlation_heatmap.png
│   ├── 2_income_life_expectancy.png
│   ├── 3_life_expectancy_by_income.png
│   ├── 4_healthcare_access_mortality.png
│   ├── 5_health_behaviors.png
│   └── 6_feature_importance.png
├── exploratory_analysis.py       # Script to generate graphs
├── convert_excel_correct.py      # Data processing
├── PROJECT_SUMMARY.md            # Main reference doc
├── PROJECT_WRITEUP.md            # Extended write-up
├── README.md                     # GitHub readme
└── QUICK_REFERENCE.md            # This file
```

---

## 🔗 Important Links

- **GitHub Repo:** https://github.com/orginalbusta/Proj3
- **Live Site:** https://orginalbusta.github.io/Proj3/
- **Data Source:** https://www.countyhealthrankings.org/health-data

---

## 💡 Tips for Success

### For the Video:
- Screen record while speaking (show graphs + live site)
- Keep it under 60 seconds (45-50s is ideal)
- Show the live visualization in action
- Be enthusiastic about the findings!

### For Final Submission:
- Proofread everything (typos = unprofessional)
- Test on a friend (is it intuitive?)
- Check the rubric one more time
- Submit early (don't wait until 11:59 PM!)

### Common Pitfalls to Avoid:
- ❌ Write-up missing or too brief
- ❌ Design decisions not explained
- ❌ Broken interactions on some browsers
- ❌ Unclear what question is being answered
- ❌ Repo not public
- ❌ Source code missing

---

## 🤝 Team Workflow Suggestions

### Division of Labor:
1. **Person A:** Create checkpoint video (screen record + voiceover)
2. **Person B:** Draft write-up sections (design rationale)
3. **Person C:** Test for bugs, polish UI
4. **Everyone:** Review and approve before submission

### Git Workflow:
```bash
# Pull latest changes before working
git pull origin main

# Make your changes, then:
git add .
git commit -m "Descriptive message"
git push origin main
```

---

## 📊 Expected Final Score

| Component | Points | Our Status |
|-----------|--------|------------|
| Visual Encodings | 4/4 | ✅ Strong |
| Data Transformations | 2/2 | ✅ Good |
| Interaction | 5/5 | ✅ Excellent |
| Writeup | 2-3/3 | ⚠️ In progress |
| **Subtotal** | **13-14/14** | |
| Creativity Bonus | +1 | ✅ Likely |
| **Total** | **14-15/14** | 🎯 |

**Target:** 14/14 (full points + bonus)

---

**Last Updated:** October 30, 2024  
**Status:** Checkpoint ready, final write-up needed

