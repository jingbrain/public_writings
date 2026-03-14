import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

# Historical data points (Year, Spread in USD)
# 2010-2026 key data points to show the story
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026])
spread = np.array([0, 8, 15, 20, 25, 8, 3, 2, 4, 6, -40, 3, 5, 4, 3, 2, -2])

# Create smooth curve using spline interpolation
years_smooth = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, spread, k=3)
spread_smooth = spl(years_smooth)

# Create figure with high resolution
fig, ax = plt.subplots(figsize=(14, 8), dpi=300)

# Plot main line (solid blue)
ax.plot(years_smooth, spread_smooth, color='#1f77b4', linewidth=2.5, label='Brent - WTI Spread')

# Add horizontal zero line (dashed red)
ax.axhline(y=0, color='red', linestyle='--', linewidth=1.5, label='Spread = 0', alpha=0.7)

# Add shaded region for positive spread
ax.fill_between(years_smooth, 0, spread_smooth, where=(spread_smooth >= 0), 
                alpha=0.1, color='blue', interpolate=True)

# Add annotations for key events
# 1. Shale boom + US export ban (2013-2014 peak)
ax.annotate('Shale boom + US export ban', 
            xy=(2013, 20), xytext=(2013, 32),
            fontsize=11, fontweight='bold', color='#2c3e50',
            ha='center',
            arrowprops=dict(arrowstyle='->', color='#34495e', lw=1.5),
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#ecf0f1', edgecolor='#34495e', alpha=0.9))

# 2. COVID-19 negative price event (2020)
ax.annotate('COVID-19 negative price event', 
            xy=(2020, -40), xytext=(2019, -55),
            fontsize=11, fontweight='bold', color='#c0392b',
            ha='center',
            arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5),
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fadbd8', edgecolor='#e74c3c', alpha=0.9))

# 3. Hormuz crisis (2026)
ax.annotate('Hormuz crisis – buyers\nshifting to US oil', 
            xy=(2026, -2), xytext=(2024.5, -25),
            fontsize=11, fontweight='bold', color='#16a085',
            ha='center',
            arrowprops=dict(arrowstyle='->', color='#1abc9c', lw=1.5),
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#d5f4e6', edgecolor='#1abc9c', alpha=0.9))

# Set title at the very top
ax.set_title('Brent - WTI Historical Spread (2010–2026)', 
             fontsize=18, fontweight='bold', color='black', pad=20)

# Set axis labels
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Spread (USD per barrel)', fontsize=14, fontweight='bold')

# Set x-axis ticks (every year)
ax.set_xticks(range(2010, 2027, 2))
ax.set_xlim(2009.5, 2026.5)

# Set y-axis range
ax.set_ylim(-60, 40)

# Add grid for better readability
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

# Add legend
ax.legend(loc='upper right', fontsize=11, framealpha=0.9)

# Improve layout
plt.tight_layout()

# Save the chart
plt.savefig('Brent_WTI_Spread_2010_2026.png', dpi=300, bbox_inches='tight', facecolor='white')
print("Chart saved as: Brent_WTI_Spread_2010_2026.png")

# Display the chart
plt.show()
