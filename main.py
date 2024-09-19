import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data setup
data = {
    'Table': ['calendar', 'calendar_defined_period', 'contour_adm', 'geo_name', 'id_geo_name', 'interchange2geo_name', 'mention_panneau', 'obstacle', 'obstacle_polygon'],
    'Nbre_Old': [12739, 933, 674935, 7846138, 7846138, 52516, 2898105, 6529829, 41280],
    'Nbre_New': [12697, 885, 674920, 7845663, 7845663, 52505, 2897053, 6526311, 40464],
    'Δ_Nbre': [-42, -48, -15, -4749, -4749, -11, -1052, -35181, -816],
    'Δ_Percent': [-0.33, -5.14, 0, -0.01, -0.01, -0.02, -0.04, -0.05, -1.98]
}

# Load data into DataFrame
df = pd.DataFrame(data)

# Set up visualizations
sns.set(style="whitegrid")

# Plot 1: Bar Plot of Changes in Number of Records
plt.figure(figsize=(12, 6))
bar_plot = sns.barplot(x='Table', y='Δ_Nbre', data=df, hue='Table', palette="viridis")
plt.xticks(rotation=90)
plt.title('Change in Number of Records Between Releases')
plt.xlabel('Table')
plt.ylabel('Change in Number of Records')
plt.legend(title='Table', bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside the plot area
plt.tight_layout()
plt.savefig('plots/bar-plot1.png')

# Plot 2: Bar Plot of Percentage Change
plt.figure(figsize=(12, 6))
percent_bar_plot = sns.barplot(x='Table', y='Δ_Percent', data=df, hue='Table', palette="viridis")
plt.xticks(rotation=90)
plt.title('Percentage Change in Number of Records Between Releases')
plt.xlabel('Table')
plt.ylabel('Percentage Change')
plt.legend(title='Table', bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside the plot area
plt.tight_layout()
plt.savefig('plots/bar-plot2.png')

# Plot 3: Scatter Plot of Old vs New Record Counts
plt.figure(figsize=(12, 6))
scatter_plot = sns.scatterplot(x='Nbre_Old', y='Nbre_New', data=df, hue='Δ_Nbre', palette='coolwarm', s=100, legend=False)
plt.plot([df['Nbre_Old'].min(), df['Nbre_Old'].max()], [df['Nbre_Old'].min(), df['Nbre_Old'].max()], 'k--')
plt.title('Old vs New Record Counts')
plt.xlabel('Number of Records (Old)')
plt.ylabel('Number of Records (New)')
plt.tight_layout()
plt.savefig('plots/scatter-plot.png')
