# How to Download Real County Health Rankings Data

## Quick Guide (15 minutes)

### Step 1: Visit the Website

Go to: **https://www.countyhealthrankings.org/health-data/methodology-and-sources/rankings-data-documentation**

### Step 2: Download National Data

Look for one of these options:

**Option A: National Trend Data** (BEST for your project)
- File name usually: `Trends data` or `2024 County Health Rankings Data`
- Contains multiple years of data
- All counties included
- CSV or Excel format

**Option B: Most Recent Year**
- Download the latest year (2024)
- Look for "National Data"
- Contains all states and counties

### Step 3: What You'll Get

The real dataset includes:

- **~3,143 counties** (all US counties)
- **50+ health metrics**
- **Multiple years** of data (2014-2024 depending on file)
- **High completeness**: >90% of counties have data for major metrics

### Step 4: Place the Downloaded File

```
F:\209r\Proj3\
  └── data\
      └── [downloaded_file].csv  <- Put it here
```

### Step 5: Convert to Your Format

```bash
python convert_data.py
```

Follow the prompts - it will:
1. Detect your downloaded file
2. Map the columns
3. Create `county_health_data.csv` with full coverage

### Step 6: Refresh Your Browser

Your visualization will now show **ALL US counties** with real data!

---

## Expected Coverage with Real Data

| Metric | Counties with Data |
|--------|-------------------|
| Life Expectancy | ~3,000 (95%+) |
| Premature Death | ~3,100 (98%+) |
| Adult Obesity | ~3,100 (98%+) |
| Diabetes | ~3,000 (95%+) |
| Unemployment | ~3,100 (98%+) |
| Median Income | ~3,100 (98%+) |

## Why Sample Data Was Needed

Sample data (87 counties) was created so you could:
- ✅ Test the visualization immediately
- ✅ Verify all interactions work
- ✅ Debug any issues
- ✅ Start development without waiting

But for your final project, you'll use the **REAL data with full coverage**.

---

## Alternative: Direct Download Links

If you're having trouble finding the data, try these:

### 2024 Rankings Data
- https://www.countyhealthrankings.org/health-data

### Look for:
- "Download Data" buttons
- "National Data & Documentation" 
- "Rankings Data" section
- "Trend Files" (multi-year data)

---

## Data Quality Assurance

The County Health Rankings dataset is:

✅ **Comprehensive**: Nearly all 3,000+ US counties  
✅ **Reliable**: Used by researchers and policymakers  
✅ **Well-documented**: Includes data dictionary  
✅ **Updated annually**: Fresh data each year  
✅ **Peer-reviewed**: Academic quality standards  

**This dataset is PERFECT for your project!**

---

## Need Help?

If you have trouble finding or downloading the data:
1. Check the official data page
2. Look for "2024 County Health Rankings" files
3. Download CSV or Excel format
4. Contact me and I'll help troubleshoot

The dataset you need definitely exists and has full county coverage! 🎉


