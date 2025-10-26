# Data Usage Summary

## What We're Actually Using 🎯

### Currently Active in Visualization
✅ **2025 County Health Rankings Data - v3.xlsx**
- **Used for**: All 2024 data displayed on the main map
- **Processed by**: `convert_excel_correct.py`
- **Output**: `county_health_data.csv` (2024 baseline)
- **Metrics extracted**: 13 health and socioeconomic indicators
- **Coverage**: 3,159 counties across all 50 states

✅ **Synthetic Time-Series (2020-2023)**
- **Created by**: `merge_places_data.py`
- **Method**: ±5% random variations of 2024 baseline data
- **Used for**: County detail modal year slider (2020-2024)
- **Note**: These are NOT real historical values, just variations for demo purposes

---

## What's Available But Not Yet Integrated 📦

### 1. County Health Rankings Trends CSV
**File**: `chr_trends_csv_2025.csv`
- **Years**: 2014-2021
- **Metrics**: Limited set (Premature Death, Uninsured, Primary Care Physicians)
- **Status**: ⏸️ Examined but not used in final visualization
- **Reason**: Limited metrics compared to the 2025 Excel file

### 2. CDC PLACES Data (5 Files)
**Files**: 
- `PLACES__Local_Data_for_Better_Health,_County_Data_2020_release_20251026.csv`
- `PLACES__Local_Data_for_Better_Health,_County_Data_2021_release_20251026.csv`
- `PLACES__Local_Data_for_Better_Health,_County_Data_2022_release_20251026.csv`
- `PLACES__Local_Data_for_Better_Health,_County_Data_2023_release_20251026.csv`
- `PLACES__Local_Data_for_Better_Health,_County_Data_2024_release_20251026.csv`

**Content**:
- **Years**: 2020-2024 (5 annual releases)
- **Metrics**: Chronic disease, health behaviors, preventive services
- **Format**: Wide format with measures like:
  - Arthritis, High Blood Pressure, Diabetes
  - Binge Drinking, Current Smoking
  - Health Insurance Status
  - Dental Visits, Cancer Screenings
- **Status**: 📥 Downloaded and available but not yet parsed/integrated
- **Challenge**: Different structure than CHR data (needs custom mapping)

---

## Data Pipeline Overview

```
[Raw Sources]                    [Processing Scripts]           [Output]                [Usage]
┌─────────────────────────┐     ┌──────────────────┐     ┌─────────────────┐     ┌──────────────┐
│ 2025 CHR Data (Excel)   │────>│ convert_excel    │────>│ county_health_  │────>│ Main Map     │
│ - 2024 data             │     │ _correct.py      │     │ data.csv        │     │ (2024)       │
└─────────────────────────┘     └──────────────────┘     │ - 2024 only     │     └──────────────┘
                                                          └─────────────────┘
                                                                  │
                                                                  ▼
                                ┌──────────────────┐     ┌─────────────────┐     ┌──────────────┐
                                │ merge_places_    │────>│ county_health_  │────>│ Modal Slider │
                                │ data.py          │     │ data.csv        │     │ (2020-2024)  │
                                │ (synthetic vars) │     │ - All 5 years   │     │ [Synthetic]  │
                                └──────────────────┘     └─────────────────┘     └──────────────┘

[Available But Unused]
┌─────────────────────────┐
│ CHR Trends CSV          │     ⏸️ Not currently used
│ (2014-2021)             │
└─────────────────────────┘

┌─────────────────────────┐
│ CDC PLACES (2020-2024)  │     📥 Available for future integration
│ (5 files)               │
└─────────────────────────┘
```

---

## Why Synthetic Data for Time-Series?

When we added the county click modal feature with the year slider, we needed multi-year data quickly. Rather than spending time:
1. Parsing the complex PLACES CSV structure
2. Mapping PLACES measures to our existing metrics
3. Handling missing data and inconsistencies
4. Merging datasets with different county identifiers

We created a **working prototype** with synthetic variations that:
- ✅ Demonstrates the time-series interaction
- ✅ Shows the UI/UX design
- ✅ Allows testing of all features
- ✅ Can be replaced with real data later

**The structure is already in place** - we just need to run a proper PLACES converter script to replace the synthetic data with real historical values.

---

## Future Integration Plan

### Option 1: Use PLACES Data (Recommended)
- **Pro**: Most comprehensive, 2020-2024 coverage, matches our current years
- **Con**: Requires custom parser for wide-format data
- **Effort**: ~2-3 hours to build proper converter

### Option 2: Use CHR Trends CSV
- **Pro**: Already in CHR format, easier to parse
- **Con**: Only 2014-2021 (doesn't reach 2024), limited metrics
- **Effort**: ~1 hour to integrate

### Option 3: Hybrid Approach
- Use CHR 2025 for 2024 (current)
- Use CHR Trends for 2014-2021
- Use PLACES for 2022-2023 to fill the gap
- **Con**: Most complex, potential inconsistencies
- **Effort**: ~3-4 hours

---

## Quick Facts

| Item | Value |
|------|-------|
| **Primary source currently used** | 1 dataset (CHR 2025 Excel) |
| **Total files in data folder** | 8 files |
| **Files actively used** | 1 file (+ 1 generated CSV) |
| **Real historical data available** | Yes (6 additional files) |
| **Real historical data integrated** | No (synthetic variations used) |
| **Counties covered** | 3,159 |
| **Years of real data available** | 2014-2024 (various sources) |
| **Years currently displayed** | 2020-2024 (synthetic for 2020-2023) |

---

## Transparency Note

The updated footer now clearly states:
> "Time-series data (2020-2024) in the county detail modal currently uses synthetic variations based on 2024 baseline data. Integration of real historical data from PLACES and CHR Trends datasets is planned for future updates."

This is **honest about the current state** while acknowledging the available resources for future enhancement.


