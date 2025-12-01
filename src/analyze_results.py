import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# === CONFIG ===
PYTHON_CSV = "output/result.csv"
RUST_CSV = "output/result_rust.csv"
OUTPUT_DIR = "output/"

# Create output directory if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === LOAD DATA ===
df_py = pd.read_csv(PYTHON_CSV)
df_rust = pd.read_csv(RUST_CSV)

# Standardize column names for merging
df_py = df_py.rename(columns={
	'Mean Time (seconds)': 'Time (seconds)',
	'Std Dev': 'StdDev'
})
df_rust = df_rust.rename(columns={
	'Mean Time (seconds)': 'Time (seconds)',
	'Std Dev': 'StdDev'
})

# Combine both dataframes
df = pd.concat([df_py, df_rust], ignore_index=True)
df['Time (seconds)'] = df['Time (seconds)'].astype(float)
df['StdDev'] = df['StdDev'].astype(float)

# === BASIC OVERVIEW ===
print("\n=== RAW DATA PREVIEW ===")
print(df.head())

print("\n=== SUMMARY STATS ===")
summary_stats = df.groupby(['Implementation', 'Function'])['Time (seconds)'].describe()
print(summary_stats)

# === AVERAGE TIME PER FUNCTION ===
avg_time = df.groupby(['Implementation', 'Function'])['Time (seconds)'].mean().reset_index()
print("\n=== AVERAGE EXECUTION TIMES ===")
print(avg_time)

# === PIVOT TABLE FOR COMPARISON ===
pivot = avg_time.pivot(index='Function', columns='Implementation', values='Time (seconds)')
print("\n=== PIVOT TABLE ===")
print(pivot)

# === PERFORMANCE RATIO (Python ÷ Rust) ===
pivot['Speedup (Python ÷ Rust)'] = pivot['Python'] / pivot['Rust']
print("\n=== RELATIVE PERFORMANCE (Python ÷ Rust) ===")
print(pivot)

# === STABILITY (STANDARD DEVIATION) ===
std_df = df.groupby(['Implementation', 'Function'])['Time (seconds)'].std().reset_index()
std_pivot = std_df.pivot(index='Function', columns='Implementation', values='Time (seconds)')
pivot['Rust StdDev'] = std_pivot['Rust']
pivot['Python StdDev'] = std_pivot['Python']

print("\n=== PERFORMANCE + STABILITY ===")
print(pivot)

# === VISUALIZATION SETUP ===
sns.set_theme(style="whitegrid")

# === 1. BAR PLOT: AVERAGE TIME PER FUNCTION ===
plt.figure(figsize=(8, 5))
sns.barplot(data=avg_time, x='Function', y='Time (seconds)', hue='Implementation')
plt.title('Average Execution Time per Function')
plt.ylabel('Time (seconds)')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "average_execution_time.png"), dpi=300)
plt.close()

# === 2. BOX PLOT: DISTRIBUTION (SPREAD) ===
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Function', y='Time (seconds)', hue='Implementation')
plt.title('Distribution of Execution Times per Function')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "execution_time_distribution.png"), dpi=300)
plt.close()

# === 3. HEATMAP: PERFORMANCE RATIO ===
plt.figure(figsize=(6, 3))
sns.heatmap(pivot[['Speedup (Python ÷ Rust)']].T, annot=True, cmap="coolwarm", fmt=".2f")
plt.title('Python-to-Rust Speed Ratio')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "python_to_rust_speed_ratio.png"), dpi=300)
plt.close()

# === 4. OPTIONAL: STABILITY BAR CHART ===
std_long = std_df.pivot(index='Function', columns='Implementation', values='Time (seconds)').reset_index()
std_long = std_long.melt(id_vars='Function', var_name='Implementation', value_name='StdDev')

plt.figure(figsize=(8, 5))
sns.barplot(data=std_long, x='Function', y='StdDev', hue='Implementation')
plt.title('Execution Time Stability (Standard Deviation)')
plt.ylabel('StdDev (seconds)')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "execution_time_stability.png"), dpi=300)
plt.close()

# === OVERALL AVERAGE ===
overall = df.groupby('Implementation')['Time (seconds)'].mean()
print("\n=== OVERALL AVERAGE TIME ===")
print(overall)
speedup = overall['Python'] / overall['Rust']
print(f"\nRust overall speedup vs Python: {speedup:.2f}× faster (approx)\n")

# === SAVE SUMMARY CSV ===
pivot.to_csv(os.path.join(OUTPUT_DIR, "summary_results.csv"), index=True)
summary_stats.to_csv(os.path.join(OUTPUT_DIR, "detailed_statistics.csv"))

print(f"\n✅ All charts and summaries saved in: {OUTPUT_DIR}\n")
