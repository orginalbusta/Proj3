// County Health Rankings Interactive Visualization
// Main JavaScript file using D3.js

// Global variables
let countyData = null;
let geoData = null;
let currentYear = 2024;  // 2024 data now available
let currentMetric = 'life_expectancy';  // Default to life expectancy
let currentState = 'all';
let svg = null;
let projection = null;
let path = null;
let colorScale = null;

// Metric configurations
const metrics = {
    life_expectancy: {
        name: 'Life Expectancy',
        unit: 'years',
        format: d => d ? d.toFixed(1) + ' years' : 'N/A',
        domain: [70, 85],  // High life expectancy = dark green (good/healthy)
        colorScheme: d3.interpolateGreens
    },
    premature_death: {
        name: 'Premature Death Rate',
        unit: 'per 100,000',
        format: d => d ? Math.round(d) : 'N/A',
        domain: [5000, 15000],  // Wider range for better differentiation
        colorScheme: d3.interpolateReds  // High death = dark red (bad)
    },
    adult_obesity: {
        name: 'Adult Obesity',
        unit: '%',
        format: d => d ? d.toFixed(1) + '%' : 'N/A',
        domain: [25, 40],  // Tightened range for better differentiation
        colorScheme: d3.interpolateOranges  // High obesity = dark orange (bad)
    },
    adult_smoking: {
        name: 'Adult Smoking',
        unit: '%',
        format: d => d ? d.toFixed(1) + '%' : 'N/A',
        domain: [10, 30],
        colorScheme: d3.interpolateReds  // High smoking = dark red (bad)
    },
    physical_inactivity: {
        name: 'Physical Inactivity',
        unit: '%',
        format: d => d ? d.toFixed(1) + '%' : 'N/A',
        domain: [15, 35],
        colorScheme: d3.interpolatePurples  // High inactivity = dark purple (bad)
    },
    diabetes: {
        name: 'Diabetes Prevalence',
        unit: '%',
        format: d => d ? d.toFixed(1) + '%' : 'N/A',
        domain: [8, 16],  // Tightened range for better differentiation
        colorScheme: d3.interpolateOrRd  // High diabetes = dark red-orange (bad)
    },
    unemployment: {
        name: 'Unemployment Rate',
        unit: '%',
        format: d => d ? d.toFixed(1) + '%' : 'N/A',
        domain: [2, 12],
        colorScheme: d3.interpolateReds  // High unemployment = dark red (bad)
    },
    poor_health: {
        name: 'Poor or Fair Health',
        unit: '%',
        format: d => d ? d.toFixed(1) + '%' : 'N/A',
        domain: [10, 30],
        colorScheme: d3.interpolateOranges  // High poor health = dark orange (bad)
    },
    excessive_drinking: {
        name: 'Excessive Drinking',
        unit: '%',
        format: d => d ? d.toFixed(1) + '%' : 'N/A',
        domain: [10, 25],
        colorScheme: d3.interpolatePurples  // High drinking = dark purple (bad)
    },
    hs_graduation: {
        name: 'High School Graduation',
        unit: '%',
        format: d => d ? d.toFixed(1) + '%' : 'N/A',
        domain: [70, 95],  // High graduation = dark green (well-educated)
        colorScheme: d3.interpolateGreens
    },
    median_income: {
        name: 'Median Household Income',
        unit: '$',
        format: d => d ? '$' + d.toLocaleString() : 'N/A',
        domain: [30000, 90000],  // High income = dark blue (affluent/good)
        colorScheme: d3.interpolateBlues
    },
    uninsured: {
        name: 'Uninsured Rate',
        unit: '%',
        format: d => d ? d.toFixed(1) + '%' : 'N/A',
        domain: [5, 25],
        colorScheme: d3.interpolateReds  // High uninsured = dark red (bad)
    },
    primary_care_rate: {
        name: 'Primary Care Physicians',
        unit: 'per 100,000 population',
        format: d => d ? d.toFixed(1) + ' per 100k residents' : 'N/A',
        domain: [20, 100],  // High doctors per capita = dark green (well-served)
        colorScheme: d3.interpolateGreens
    }
};

// Initialize the visualization
function init() {
    console.log('Initializing visualization...');
    
    // Set up event listeners
    setupEventListeners();
    
    // Load data
    loadData();
}

function setupEventListeners() {
    // Year slider
    d3.select('#year-slider').on('input', function() {
        currentYear = +this.value;
        d3.select('#year-display').text(currentYear);
        updateVisualization();
    });
    
    // Metric selector
    d3.select('#metric-selector').on('change', function() {
        currentMetric = this.value;
        updateVisualization();
    });
    
    // Reset button
    d3.select('#reset-button').on('click', function() {
        resetVisualization();
    });
}

async function loadData() {
    try {
        console.log('Loading data...');
        
        // Load US counties TopoJSON
        const us = await d3.json('https://cdn.jsdelivr.net/npm/us-atlas@3/counties-10m.json');
        geoData = us;
        
        // For now, load sample data (you'll replace this with actual County Health Rankings data)
        // This is a placeholder structure
        countyData = await loadCountyHealthData();
        
        console.log('Data loaded successfully');
        
        // Initialize the map
        initializeMap();
        
        // Draw initial visualization
        updateVisualization();
        
    } catch (error) {
        console.error('Error loading data:', error);
        showError('Error loading data. Please check the console for details.');
    }
}

async function loadCountyHealthData() {
    // TODO: Replace this with actual data loading from your CSV file
    // This is sample data structure for demonstration
    
    // Try to load from local file
    try {
        const data = await d3.csv('data/county_health_data.csv', d => ({
            fips: d.fips,
            county: d.county,
            state: d.state,
            year: +d.year,
            // Health Outcomes
            life_expectancy: +d.life_expectancy || null,
            premature_death: +d.premature_death || null,
            poor_health: +d.poor_health || null,
            // Health Behaviors
            adult_obesity: +d.adult_obesity || null,
            adult_smoking: +d.adult_smoking || null,
            physical_inactivity: +d.physical_inactivity || null,
            diabetes: +d.diabetes || null,
            excessive_drinking: +d.excessive_drinking || null,
            // Socioeconomic
            median_income: +d.median_income || null,
            hs_graduation: +d.hs_graduation || null,
            unemployment: +d.unemployment || null,
            // Clinical Care
            uninsured: +d.uninsured || null,
            primary_care_rate: +d.primary_care_rate || null
        }));
        return data;
    } catch (error) {
        console.warn('Could not load local data file. Using sample data for demonstration.');
        
        // Generate sample data for demonstration
        const sampleData = [];
        const states = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania'];
        
        for (let year = 2014; year <= 2024; year++) {
            for (let i = 0; i < 100; i++) {
                const fips = String(1000 + i).padStart(5, '0');
                sampleData.push({
                    fips: fips,
                    county: `County ${i}`,
                    state: states[i % states.length],
                    year: year,
                    life_expectancy: 70 + Math.random() * 15,
                    premature_death: 2000 + Math.random() * 8000,
                    adult_obesity: 20 + Math.random() * 25,
                    diabetes: 8 + Math.random() * 10,
                    unemployment: 2 + Math.random() * 10,
                    median_income: 30000 + Math.random() * 60000
                });
            }
        }
        
        return sampleData;
    }
}

function initializeMap() {
    // Set up SVG
    svg = d3.select('#map-svg');
    const width = svg.node().getBoundingClientRect().width;
    const height = 600;
    
    // Set up projection
    projection = d3.geoAlbersUsa()
        .scale(width * 1.3)
        .translate([width / 2, height / 2]);
    
    path = d3.geoPath().projection(projection);
    
    // Add zoom behavior
    const zoom = d3.zoom()
        .scaleExtent([1, 8])
        .on('zoom', (event) => {
            svg.selectAll('g').attr('transform', event.transform);
        });
    
    svg.call(zoom);
    
    // Create main group for counties
    svg.append('g').attr('class', 'counties');
    
    // Create group for state boundaries
    svg.append('g').attr('class', 'states');
}

function updateVisualization() {
    if (!geoData || !countyData) return;
    
    console.log(`Updating visualization: Year=${currentYear}, Metric=${currentMetric}, State=${currentState}`);
    
    // Filter data for current year
    const yearData = countyData.filter(d => d.year === currentYear);
    
    // Create lookup map
    const dataMap = new Map(yearData.map(d => [d.fips, d]));
    
    // Update color scale
    const metricConfig = metrics[currentMetric];
    
    // For metrics where HIGH is BAD (reverse=true), we want high values to be DARK
    // For metrics where HIGH is GOOD (reverse=false), we want high values to be DARK
    // So we always use the domain as-is, D3 interpolators go from light to dark naturally
    colorScale = d3.scaleSequential()
        .domain(metricConfig.domain)
        .interpolator(metricConfig.colorScheme);
    
    // Update counties
    updateCounties(dataMap, metricConfig);
    
    // Update legend
    updateLegend(metricConfig);
    
    // Update insights
    updateInsights(yearData, metricConfig);
}

function updateCounties(dataMap, metricConfig) {
    const counties = topojson.feature(geoData, geoData.objects.counties).features;
    
    const countyElements = svg.select('.counties')
        .selectAll('path')
        .data(counties, d => d.id);
    
    // Enter + Update
    countyElements.enter()
        .append('path')
        .merge(countyElements)
        .attr('class', 'county')
        .attr('d', path)
        .transition()
        .duration(500)
        .attr('fill', d => {
            const countyData = dataMap.get(d.id);
            if (!countyData || !countyData[currentMetric]) {
                return '#ccc';
            }
            return colorScale(countyData[currentMetric]);
        });
    
    // Add event listeners
    svg.selectAll('.county')
        .on('mouseover', function(event, d) {
            d3.select(this)
                .style('stroke', '#333')
                .style('stroke-width', '2px');
            
            showCountyInfo(d, dataMap);
        })
        .on('mouseout', function() {
            d3.select(this)
                .style('stroke', '#fff')
                .style('stroke-width', '0.5px');
        })
        .on('click', function(event, d) {
            // Highlight clicked county
            d3.select(this)
                .style('stroke', '#ff6b6b')
                .style('stroke-width', '3px');
            
            const countyData = dataMap.get(d.id);
            if (countyData) {
                showCountyModal(d.id, countyData.county, countyData.state);
            }
        });
    
    // Update state boundaries
    const states = topojson.mesh(geoData, geoData.objects.states, (a, b) => a !== b);
    
    svg.select('.states')
        .selectAll('path')
        .data([states])
        .join('path')
        .attr('class', 'state-boundary')
        .attr('d', path);
}

function showCountyInfo(countyGeo, dataMap) {
    const countyData = dataMap.get(countyGeo.id);
    const metricConfig = metrics[currentMetric];
    
    let html = '<p><em>No data available</em></p>';
    
    if (countyData) {
        html = `
            <p><strong>${countyData.county}, ${countyData.state}</strong></p>
            <p><strong>${metricConfig.name}:</strong> ${metricConfig.format(countyData[currentMetric])}</p>
            <p><strong>Year:</strong> ${currentYear}</p>
        `;
        
        // Show additional metrics
        if (countyData.life_expectancy && currentMetric !== 'life_expectancy') {
            html += `<p><strong>Life Expectancy:</strong> ${metrics.life_expectancy.format(countyData.life_expectancy)}</p>`;
        }
        if (countyData.median_income && currentMetric !== 'median_income') {
            html += `<p><strong>Median Income:</strong> ${metrics.median_income.format(countyData.median_income)}</p>`;
        }
    }
    
    d3.select('#county-info').html(html);
}

function updateLegend(metricConfig) {
    const legendSvg = d3.select('#legend-svg');
    legendSvg.selectAll('*').remove();
    
    const width = legendSvg.node().getBoundingClientRect().width;
    const height = 100;  // Increased from 80
    const margin = { top: 30, right: 100, bottom: 30, left: 100 };  // Increased top margin
    
    const legendWidth = width - margin.left - margin.right;
    const legendHeight = 20;
    
    const g = legendSvg.append('g')
        .attr('transform', `translate(${margin.left}, ${margin.top})`);
    
    // Create gradient
    const defs = legendSvg.append('defs');
    const gradient = defs.append('linearGradient')
        .attr('id', 'legend-gradient');
    
    const numStops = 10;
    for (let i = 0; i <= numStops; i++) {
        const t = i / numStops;
        const value = metricConfig.domain[0] + t * (metricConfig.domain[1] - metricConfig.domain[0]);
        gradient.append('stop')
            .attr('offset', `${t * 100}%`)
            .attr('stop-color', colorScale(value));
    }
    
    // Draw legend rectangle
    g.append('rect')
        .attr('width', legendWidth)
        .attr('height', legendHeight)
        .style('fill', 'url(#legend-gradient)');
    
    // Add scale
    const legendScale = d3.scaleLinear()
        .domain(metricConfig.domain)
        .range([0, legendWidth]);
    
    const legendAxis = d3.axisBottom(legendScale)
        .ticks(5)
        .tickFormat(d => metricConfig.format(d));
    
    g.append('g')
        .attr('transform', `translate(0, ${legendHeight})`)
        .call(legendAxis);
    
    // Add title
    g.append('text')
        .attr('x', legendWidth / 2)
        .attr('y', -5)
        .attr('text-anchor', 'middle')
        .style('font-weight', 'bold')
        .text(metricConfig.name);
}

function updateInsights(yearData, metricConfig) {
    // Calculate basic statistics
    const values = yearData
        .map(d => d[currentMetric])
        .filter(v => v !== null && !isNaN(v));
    
    if (values.length === 0) {
        d3.select('#insights-content').html('<p>No data available for the selected filters.</p>');
        return;
    }
    
    const mean = d3.mean(values);
    const median = d3.median(values);
    const min = d3.min(values);
    const max = d3.max(values);
    
    const html = `
        <p><strong>${metricConfig.name}</strong> statistics for <strong>${currentYear}</strong>:</p>
        <ul>
            <li><strong>Mean:</strong> ${metricConfig.format(mean)}</li>
            <li><strong>Median:</strong> ${metricConfig.format(median)}</li>
            <li><strong>Range:</strong> ${metricConfig.format(min)} to ${metricConfig.format(max)}</li>
            <li><strong>Counties with data:</strong> ${values.length.toLocaleString()}</li>
        </ul>
        <p>Use the controls above to explore different health metrics, years, and states.</p>
    `;
    
    d3.select('#insights-content').html(html);
}

function resetVisualization() {
    currentYear = 2024;
    currentMetric = 'life_expectancy';
    currentState = 'all';
    
    d3.select('#year-slider').property('value', currentYear);
    d3.select('#year-display').text(currentYear);
    d3.select('#metric-selector').property('value', currentMetric);
    
    // Reset zoom
    svg.transition().duration(750).call(
        d3.zoom().transform,
        d3.zoomIdentity
    );
    
    updateVisualization();
}

function showError(message) {
    d3.select('#map-container').append('div')
        .attr('class', 'error-message')
        .style('color', 'red')
        .style('padding', '20px')
        .style('text-align', 'center')
        .text(message);
}

// ========================================
// COUNTY DETAIL MODAL FUNCTIONALITY
// ========================================

let selectedCountyFips = null;
let modalYear = 2024;

function showCountyModal(fips, countyName, stateName) {
    selectedCountyFips = fips;
    modalYear = 2024; // Reset to latest year
    
    // Update modal header
    d3.select('#modal-county-name').text(countyName);
    d3.select('#modal-county-state').text(stateName);
    
    // Reset year slider
    d3.select('#modal-year-slider').property('value', modalYear);
    d3.select('#modal-year-display').text(modalYear);
    
    // Update metrics
    updateModalMetrics();
    
    // Show modal
    d3.select('#county-modal').style('display', 'block');
}

function hideCountyModal() {
    d3.select('#county-modal').style('display', 'none');
    
    // Remove highlight from all counties
    svg.selectAll('.county')
        .style('stroke', '#fff')
        .style('stroke-width', '0.5px');
    
    selectedCountyFips = null;
}

function updateModalMetrics() {
    if (!selectedCountyFips || !countyData) return;
    
    // Find data for the selected county and year
    const countyYearData = countyData.find(d => 
        d.fips === selectedCountyFips && d.year === modalYear
    );
    
    if (!countyYearData) {
        d3.select('#modal-metrics-container').html('<p style="color: #999; text-align: center;">No data available for this year</p>');
        return;
    }
    
    // Build metrics display
    const metricsToShow = [
        { key: 'life_expectancy', label: 'Life Expectancy', icon: '💚' },
        { key: 'premature_death', label: 'Premature Death Rate', icon: '💔' },
        { key: 'adult_obesity', label: 'Adult Obesity', icon: '🍔' },
        { key: 'adult_smoking', label: 'Adult Smoking', icon: '🚬' },
        { key: 'physical_inactivity', label: 'Physical Inactivity', icon: '🛋️' },
        { key: 'diabetes', label: 'Diabetes', icon: '🩺' },
        { key: 'excessive_drinking', label: 'Excessive Drinking', icon: '🍺' },
        { key: 'poor_health', label: 'Poor Health', icon: '🤒' },
        { key: 'median_income', label: 'Median Household Income', icon: '💰' },
        { key: 'hs_graduation', label: 'High School Graduation', icon: '🎓' },
        { key: 'unemployment', label: 'Unemployment', icon: '💼' },
        { key: 'primary_care_rate', label: 'Primary Care Physicians', icon: '👨‍⚕️' },
        { key: 'uninsured', label: 'Uninsured', icon: '🏥' }
    ];
    
    const container = d3.select('#modal-metrics-container');
    container.html('');
    
    metricsToShow.forEach(metric => {
        const value = countyYearData[metric.key];
        const metricConfig = metrics[metric.key];
        
        if (!metricConfig) return;
        
        const row = container.append('div').attr('class', 'metric-row');
        
        row.append('div')
            .attr('class', 'metric-name')
            .html(`${metric.icon} ${metric.label}`);
        
        row.append('div')
            .attr('class', value != null ? 'metric-value' : 'metric-value na')
            .text(value != null ? metricConfig.format(value) : 'N/A');
    });
}

// Set up modal event listeners
function setupModalListeners() {
    // Close button
    d3.select('.modal-close').on('click', hideCountyModal);
    
    // Click outside modal to close
    d3.select('#county-modal').on('click', function(event) {
        if (event.target.id === 'county-modal') {
            hideCountyModal();
        }
    });
    
    // Year slider
    d3.select('#modal-year-slider').on('input', function() {
        modalYear = +this.value;
        d3.select('#modal-year-display').text(modalYear);
        updateModalMetrics();
    });
    
    // Escape key to close
    d3.select('body').on('keydown', function(event) {
        if (event.key === 'Escape') {
            hideCountyModal();
        }
    });
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        init();
        setupModalListeners();
    });
} else {
    init();
    setupModalListeners();
}

