import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
from scipy.interpolate import make_interp_spline

# Chart 1: Backwardation - 真实的非线性曲线
fig, ax = plt.subplots(figsize=(10, 6))
months = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
x_points = np.array([0, 1, 2, 3, 4, 5])
# 模拟真实市场：开始下降快，后面趋缓
prices_backwardation = np.array([100, 97, 94.5, 92.5, 91, 90])

# 使用样条插值创建平滑曲线
x_smooth = np.linspace(x_points.min(), x_points.max(), 300)
spl = make_interp_spline(x_points, prices_backwardation, k=3)
prices_smooth = spl(x_smooth)

# 绘制平滑曲线
ax.plot(x_smooth, prices_smooth, linewidth=3, color='#e74c3c', label='Backwardation Curve')
# 绘制数据点
ax.scatter(x_points, prices_backwardation, s=100, color='#c0392b', zorder=3, edgecolors='white', linewidths=2)

ax.set_xticks(x_points)
ax.set_xticklabels(months)
ax.set_xlabel('Contract Month', fontsize=13, fontweight='bold')
ax.set_ylabel('Price (USD/barrel)', fontsize=13, fontweight='bold')
ax.set_title('Backwardation: Near-term Premium\nMarket Signal: Immediate Supply Shortage', fontsize=15, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_ylim(85, 105)

# Add annotation
ax.annotate('Buyers pay premium\nfor immediate delivery', 
            xy=(0, 100), xytext=(2, 103),
            fontsize=11,
            bbox=dict(boxstyle='round,pad=0.8', facecolor='yellow', alpha=0.8, edgecolor='black'),
            arrowprops=dict(arrowstyle='->', lw=2, color='black'))

# Add value labels
for i, price in enumerate(prices_backwardation):
    ax.text(i, price - 1.5, f'${price:.1f}', ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('Backwardation.png', dpi=150, bbox_inches='tight')
plt.close()
print('Backwardation chart saved!')

# Chart 2: Contango - 真实的非线性曲线
fig, ax = plt.subplots(figsize=(10, 6))
# 模拟真实市场：开始上升快，后面趋缓
prices_contango = np.array([100, 103, 105.5, 107.5, 109, 110])

# 使用样条插值创建平滑曲线
spl2 = make_interp_spline(x_points, prices_contango, k=3)
prices_smooth2 = spl2(x_smooth)

# 绘制平滑曲线
ax.plot(x_smooth, prices_smooth2, linewidth=3, color='#3498db', label='Contango Curve')
# 绘制数据点
ax.scatter(x_points, prices_contango, s=100, color='#2980b9', zorder=3, edgecolors='white', linewidths=2)

ax.set_xticks(x_points)
ax.set_xticklabels(months)
ax.set_xlabel('Contract Month', fontsize=13, fontweight='bold')
ax.set_ylabel('Price (USD/barrel)', fontsize=13, fontweight='bold')
ax.set_title('Contango: Future Premium\nMarket Signal: Current Supply Surplus', fontsize=15, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_ylim(95, 115)

# Add annotation
ax.annotate('Storage pays off\nFuture prices higher', 
            xy=(5, 110), xytext=(3, 97),
            fontsize=11,
            bbox=dict(boxstyle='round,pad=0.8', facecolor='lightgreen', alpha=0.8, edgecolor='black'),
            arrowprops=dict(arrowstyle='->', lw=2, color='black'))

# Add value labels
for i, price in enumerate(prices_contango):
    ax.text(i, price + 1.5, f'${price:.1f}', ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('Contango.png', dpi=150, bbox_inches='tight')
plt.close()
print('Contango chart saved!')

print('Both charts generated successfully!')
