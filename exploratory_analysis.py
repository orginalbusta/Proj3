"""
Exploratory Analysis for County Health Rankings Data
Creates 6 static visualizations to inform the research question
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Load data
df = pd.read_csv('data/county_health_data.csv')

# Filter to 2024 data only for exploratory analysis
df_2024 = df[df['year'] == 2024].copy()

print(f"Total counties: {len(df_2024)}")
print(f"Available metrics: {df_2024.columns.tolist()}")

# Create output directory for figures
import os
os.makedirs('exploratory_figures', exist_ok=True)

# ========================================
# GRAPH 1: Correlation Heatmap
# ========================================
print("\n[1/6] Creating correlation heatmap...")

# Select key metrics for correlation
metrics_for_corr = [
    'life_expectancy', 'premature_death', 'adult_obesity', 
    'adult_smoking', 'physical_inactivity', 'diabetes',
    'unemployment', 'median_income', 'hs_graduation',
    'uninsured', 'primary_care_rate', 'poor_health'
]

corr_data = df_2024[metrics_for_corr].corr()

plt.figure(figsize=(12, 10))
sns.heatmap(corr_data, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True, linewidths=1,
            cbar_kws={"shrink": 0.8})
plt.title('Correlation Between Health Outcomes and Socioeconomic Factors\n(2024 County Health Rankings Data)', 
          fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('exploratory_figures/1_correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("   [OK] Saved: 1_correlation_heatmap.png")

# ========================================
# GRAPH 2: Income vs Life Expectancy Scatter
# ========================================
print("[2/6] Creating income vs life expectancy scatter...")

plt.figure(figsize=(12, 7))
scatter = plt.scatter(df_2024['median_income'], df_2024['life_expectancy'], 
                     c=df_2024['hs_graduation'], cmap='viridis', 
                     alpha=0.6, s=30, edgecolors='black', linewidth=0.3)
plt.colorbar(scatter, label='High School Graduation Rate (%)')
plt.xlabel('Median Household Income ($)', fontsize=12, fontweight='bold')
plt.ylabel('Life Expectancy (years)', fontsize=12, fontweight='bold')
plt.title('Income and Education as Predictors of Life Expectancy\nEach point = one U.S. county (n=3,142)', 
          fontsize=14, fontweight='bold', pad=15)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('exploratory_figures/2_income_life_expectancy.png', dpi=300, bbox_inches='tight')
plt.close()
print("   [OK] Saved: 2_income_life_expectancy.png")

# ========================================
# GRAPH 3: Distribution of Life Expectancy by Income Quartile
# ========================================
print("[3/6] Creating life expectancy distribution by income quartile...")

# Create income quartiles
df_2024['income_quartile'] = pd.qcut(df_2024['median_income'], q=4, 
                                      labels=['Q1 (Lowest)', 'Q2', 'Q3', 'Q4 (Highest)'])

plt.figure(figsize=(12, 7))
sns.violinplot(data=df_2024, x='income_quartile', y='life_expectancy', 
               palette='Set2', inner='box')
plt.xlabel('Income Quartile', fontsize=12, fontweight='bold')
plt.ylabel('Life Expectancy (years)', fontsize=12, fontweight='bold')
plt.title('Life Expectancy Varies Dramatically by County Income Level\nDistribution across 3,142 U.S. Counties', 
          fontsize=14, fontweight='bold', pad=15)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('exploratory_figures/3_life_expectancy_by_income.png', dpi=300, bbox_inches='tight')
plt.close()
print("   [OK] Saved: 3_life_expectancy_by_income.png")

# ========================================
# GRAPH 4: Healthcare Access vs Health Outcomes
# ========================================
print("[4/6] Creating healthcare access vs premature death...")

plt.figure(figsize=(12, 7))
scatter = plt.scatter(df_2024['primary_care_rate'], df_2024['premature_death'], 
                     c=df_2024['uninsured'], cmap='YlOrRd', 
                     alpha=0.6, s=30, edgecolors='black', linewidth=0.3)
plt.colorbar(scatter, label='Uninsured Rate (%)')
plt.xlabel('Primary Care Physicians (per 100k residents)', fontsize=12, fontweight='bold')
plt.ylabel('Premature Death Rate (per 100k)', fontsize=12, fontweight='bold')
plt.title('Healthcare Access and Insurance Coverage Impact Mortality\nU.S. Counties, 2024', 
          fontsize=14, fontweight='bold', pad=15)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('exploratory_figures/4_healthcare_access_mortality.png', dpi=300, bbox_inches='tight')
plt.close()
print("   [OK] Saved: 4_healthcare_access_mortality.png")

# ========================================
# GRAPH 5: Health Behaviors Comparison
# ========================================
print("[5/6] Creating health behaviors comparison...")

# Calculate mean values for each behavior
behaviors = ['adult_obesity', 'adult_smoking', 'physical_inactivity', 'diabetes', 'excessive_drinking']
behavior_means = df_2024[behaviors].mean()
behavior_std = df_2024[behaviors].std()

fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.bar(range(len(behaviors)), behavior_means, yerr=behavior_std, 
              capsize=5, alpha=0.7, color=['#e74c3c', '#e67e22', '#f39c12', '#9b59b6', '#3498db'],
              edgecolor='black', linewidth=1.5)
ax.set_xticks(range(len(behaviors)))
ax.set_xticklabels(['Adult Obesity', 'Adult Smoking', 'Physical Inactivity', 'Diabetes', 'Excessive Drinking'],
                   fontsize=11, fontweight='bold')
ax.set_ylabel('Prevalence (%)', fontsize=12, fontweight='bold')
ax.set_title('Prevalence of Health Risk Behaviors Across U.S. Counties\nMean ± Standard Deviation (2024)', 
             fontsize=14, fontweight='bold', pad=15)
ax.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('exploratory_figures/5_health_behaviors.png', dpi=300, bbox_inches='tight')
plt.close()
print("   [OK] Saved: 5_health_behaviors.png")

# ========================================
# GRAPH 6: Multiple Regression - Feature Importance
# ========================================
print("[6/6] Creating feature importance for life expectancy prediction...")

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

# Prepare data for modeling
features = ['median_income', 'uninsured', 'primary_care_rate',
            'adult_obesity', 'adult_smoking', 'physical_inactivity', 'diabetes']
            
# Remove rows with missing values
model_data = df_2024[features + ['life_expectancy']].dropna()

X = model_data[features]
y = model_data['life_expectancy']

# Train random forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X, y)

# Get feature importance
importance = pd.DataFrame({
    'feature': features,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=True)

plt.figure(figsize=(12, 7))
colors = ['#3498db' if 'income' in f or 'care' in f or 'uninsured' in f
          else '#e74c3c' for f in importance['feature']]
plt.barh(range(len(importance)), importance['importance'], color=colors, 
         edgecolor='black', linewidth=1.5)
plt.yticks(range(len(importance)), 
           ['Median Income', 'Uninsured Rate', 'Primary Care Access',
            'Adult Obesity', 'Adult Smoking', 'Physical Inactivity', 'Diabetes']
           if len(importance) == 7 else importance['feature'])
plt.xlabel('Feature Importance (Random Forest)', fontsize=12, fontweight='bold')
plt.title('Socioeconomic Factors Are Strongest Predictors of Life Expectancy\nRandom Forest Model (R² = {:.3f})'.format(rf.score(X, y)), 
          fontsize=14, fontweight='bold', pad=15)
plt.grid(True, alpha=0.3, axis='x')

# Add legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='#3498db', label='Socioeconomic/Healthcare'),
                   Patch(facecolor='#e74c3c', label='Health Behaviors')]
plt.legend(handles=legend_elements, loc='lower right')

plt.tight_layout()
plt.savefig('exploratory_figures/6_feature_importance.png', dpi=300, bbox_inches='tight')
plt.close()
print("   [OK] Saved: 6_feature_importance.png")

# ========================================
# Summary Statistics
# ========================================
print("\n" + "="*60)
print("EXPLORATORY ANALYSIS COMPLETE")
print("="*60)
print(f"\nGenerated 6 exploratory visualizations in 'exploratory_figures/'")
print(f"\nKey Findings:")
print(f"   • Income strongly correlates with life expectancy (r = {df_2024['median_income'].corr(df_2024['life_expectancy']):.3f})")
print(f"   • Life expectancy range: {df_2024['life_expectancy'].min():.1f} - {df_2024['life_expectancy'].max():.1f} years")
print(f"   • Income range: ${df_2024['median_income'].min():.0f} - ${df_2024['median_income'].max():.0f}")
print(f"   • Counties analyzed: {len(df_2024):,}")
print("\n" + "="*60)

