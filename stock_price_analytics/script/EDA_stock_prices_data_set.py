import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ========== 1. Load Cleaned Dataset ==========
df = pd.read_csv(r"d:\codvede\clean data\clean_stock_prices_data_set.csv", parse_dates=['date'])

# Create folder to save figures
output_dir = r"d:\codvede\reports\figures"
os.makedirs(output_dir, exist_ok=True)

# ========== 2. Summary Statistics ==========
print("Summary Statistics:\n")
print(df.describe())

# ========== 3. Distribution of Close Price ==========
plt.figure(figsize=(6,4))
sns.histplot(df['close'], bins=30, kde=True)
plt.title("Distribution of Closing Prices")
plt.xlabel("Close Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "distribution_close.png"))
plt.close()

# ========== 4. Boxplot of Volume ==========
plt.figure(figsize=(6,4))
sns.boxplot(x=df['volume'])
plt.title("Boxplot of Trading Volume")
plt.xlabel("Volume")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "boxplot_volume.png"))
plt.close()

# ========== 5. Scatter Plot: Open vs Close ==========
plt.figure(figsize=(6,4))
plt.scatter(df['open'], df['close'], alpha=0.5)
plt.title("Open vs Close Price")
plt.xlabel("Open Price")
plt.ylabel("Close Price")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "scatter_open_close.png"))
plt.close()

# ========== 6. Correlation Heatmap ==========
plt.figure(figsize=(6,4))
sns.heatmap(df[['open','high','low','close','volume']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "correlation_heatmap.png"))
plt.close()

# ========== 7. Time-Series Plot of Closing Price ==========
plt.figure(figsize=(10,5))
plt.plot(df['date'], df['close'], label='Close Price', color='blue')
plt.title("Stock Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "closing_price_trend.png"))
plt.close()

print(f"\nEDA complete! Figures saved in: {output_dir}")
