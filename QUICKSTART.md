# Quick Start Guide

## 🚀 Get Your Visualization Running in 5 Minutes

### Step 1: Verify Files ✓

You should already have these files:
```
F:\209r\Proj3\
├── index.html              ✓ Main webpage
├── script.js               ✓ D3.js code
├── styles.css              ✓ Styling
├── data/
│   └── county_health_data.csv  ✓ Sample data
└── README.md              ✓ Documentation
```

### Step 2: Open the Visualization

**Option A: Direct Open (Simplest)**
1. Navigate to `F:\209r\Proj3\`
2. Double-click `index.html`
3. It should open in your default browser

**Option B: Local Server (Recommended)**
```bash
cd F:\209r\Proj3
python -m http.server 8000
```
Then open: http://localhost:8000

### Step 3: Test the Interactions

Try these actions to verify everything works:

1. ✅ **Year Slider**: Drag to change years (2014-2024)
2. ✅ **Metric Dropdown**: Select different health metrics
3. ✅ **State Filter**: Try filtering (currently shows all)
4. ✅ **Hover**: Mouse over map areas for tooltips
5. ✅ **Zoom**: Scroll wheel to zoom in/out
6. ✅ **Pan**: Click and drag to move around
7. ✅ **Reset Button**: Click to return to default view

### Step 4: Replace with Real Data

**When you're ready to use real County Health Rankings data:**

1. **Download data**
   - Visit: https://www.countyhealthrankings.org/health-data
   - Look for "National Data & Documentation"
   - Download CSV files

2. **Place in data folder**
   - Save to `F:\209r\Proj3\data\`
   - Name should be something like `analytic_data_2024.csv`

3. **Convert the data**
   ```bash
   python convert_data.py
   ```
   - Follow the prompts
   - This creates `county_health_data.csv`

4. **Refresh your browser**
   - The visualization will automatically load the new data

---

## 🐛 Troubleshooting

### Problem: Map doesn't appear

**Solution 1**: Check browser console (F12)
- Look for errors
- Most common: Data file not loading

**Solution 2**: Use a local server
```bash
python -m http.server 8000
```

### Problem: Console shows "CORS error"

**Solution**: Must use a local server (Option B above), not direct file open

### Problem: Counties show up as gray

**Possible causes:**
- Using sample data (only 8 counties have data)
- Real data hasn't loaded yet
- FIPS codes don't match between data and map

**Solution**: 
- Sample data is limited by design - this is normal
- Real data will fill in all counties

### Problem: Python script errors

**Solution**: Install dependencies
```bash
pip install pandas
```

---

## 📊 Understanding the Sample Data

The current sample data includes only 8 counties for testing:
- Los Angeles, CA
- San Diego, CA  
- Harris, TX (Houston)
- Dallas, TX
- New York, NY
- Kings, NY (Brooklyn)
- Cook, IL (Chicago)
- DuPage, IL

All other counties appear gray because they're not in the sample data.

**This is intentional** - it lets you test the visualization quickly without downloading large datasets.

---

## 🎯 Next Steps

### For Development & Testing
1. ✅ Basic visualization works
2. ⬜ Download real County Health Rankings data
3. ⬜ Convert and load real data
4. ⬜ Test with full 3000+ counties
5. ⬜ Customize writeup sections
6. ⬜ Add team member names
7. ⬜ Deploy to GitHub Pages

### For GitHub Pages Deployment

1. **Commit your files**
   ```bash
   git add .
   git commit -m "Initial interactive visualization"
   git push origin main
   ```

2. **Enable GitHub Pages**
   - Go to repository Settings on GitHub
   - Navigate to "Pages" section
   - Select "main" branch
   - Choose "/ (root)" folder
   - Click Save

3. **Access your live site**
   - URL: `https://YOUR_USERNAME.github.io/Proj3/`
   - Takes 2-3 minutes to go live
   - Refresh browser if needed

---

## ✨ Tips for Success

### Visual Design
- Test on multiple browsers (Chrome, Firefox, Edge)
- Check mobile responsiveness
- Ensure colors are accessible (colorblind-friendly)

### Data Processing
- Always backup original data files
- Test with small sample before processing full dataset
- Check FIPS codes are 5 digits with leading zeros

### Performance
- Full dataset (3000 counties × 11 years) should load quickly
- If slow, consider filtering to fewer years
- Use browser DevTools to profile performance

### Writeup
- Document your actual design decisions
- Note what alternatives you considered
- Be specific about development time
- Explain interesting patterns you discovered

---

## 📞 Getting Help

### Check These Resources First
1. `README.md` - Comprehensive documentation
2. `DATA_GUIDE.md` - Data download instructions
3. `PRELIMINARY_FINDINGS.md` - Design rationale and recommendations
4. Browser console (F12) - See error messages

### Common D3.js Issues
- **Data not loading**: Check file path and use local server
- **Map not rendering**: Verify TopoJSON is loading
- **Interactions not working**: Check JavaScript console for errors
- **Colors wrong**: Verify color scale domain matches your data

### Project Requirements
- ✅ Use only D3.js (no Vega-Lite/Plotly/Altair)
- ✅ Enable interactive exploration
- ✅ Deploy to GitHub Pages  
- ✅ Include design writeup
- ✅ Document development process

---

## 🎉 You're Ready!

Your visualization is set up and ready to go. The sample data demonstrates all the functionality, and you can swap in real data whenever you're ready.

**Current Status:**
- ✅ Project structure complete
- ✅ Visualization prototype working
- ✅ Sample data loaded
- ✅ All interactions implemented
- ✅ Documentation complete

**Your Next Action:**
1. Open `index.html` and verify it works
2. Download real County Health Rankings data when ready
3. Start exploring and customizing for your team

Good luck with your project! 🚀


