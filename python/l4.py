import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Две функции с twinx()
x = np.linspace(0, 5, 100)
y1 = np.sin(2 * np.pi * x)
y2 = np.exp(-x)

fig1, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(x, y1, 'g-', label='y1 = sin(2πx)')
ax2.plot(x, y2, 'b--', label='y2 = exp(-x)')

ax1.set_xlabel('x')
ax1.set_ylabel('y1', color='g')
ax2.set_ylabel('y2', color='b')
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
ax1.annotate('Peak', xy=(0.25, 1), xytext=(1, 1.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.title('Two functions with different Y axes')
plt.savefig('two_functions.png')
plt.savefig('two_functions.pdf')
plt.show()

# 2. Точечная диаграмма для 3 кластеров
np.random.seed(42)
x1 = np.random.normal(2, 0.5, 50)
y1 = np.random.normal(2, 0.5, 50)
x2 = np.random.normal(4, 0.5, 50)
y2 = np.random.normal(4, 0.5, 50)
x3 = np.random.normal(6, 0.5, 50)
y3 = np.random.normal(6, 0.5, 50)

plt.figure()
plt.scatter(x1, y1, c='r', label='Cluster 1')
plt.scatter(x2, y2, c='g', label='Cluster 2')
plt.scatter(x3, y3, c='b', label='Cluster 3')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Scatter Plot of Clusters')
plt.savefig('scatter_clusters.png')
plt.savefig('scatter_clusters.pdf')
plt.show()

# 3. Круговая диаграмма
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [15, 30, 45, 10, 25]

plt.figure()
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('User Preferences')
plt.savefig('pie_chart.png')
plt.savefig('pie_chart.pdf')
plt.show()

# 4. Тепловая карта
data = np.random.rand(10, 10)
plt.figure()
sns.heatmap(data, annot=True, fmt=".2f", cmap="coolwarm")
plt.title('Heatmap of Random Data')
plt.savefig('heatmap.png')
plt.savefig('heatmap.pdf')
plt.show()

# 5. Горизонтальная столбчатая диаграмма
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 30, 25]

plt.figure()
plt.barh(categories, values, color='skyblue')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Chart')
plt.savefig('bar_chart.png')
plt.savefig('bar_chart.pdf')
plt.show()

# 6. Трёхмерный график поверхности
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, cmap='viridis')
fig.colorbar(surf)
plt.title('3D Surface Plot')
plt.savefig('3d_surface.png')
plt.savefig('3d_surface.pdf')
plt.show()
