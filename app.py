import matplotlib.pyplot as plt

# establish x and y axises
x = [2, 4, 5 ,6]
y = [2, 3, 6, 7]

# plot the point
plt.plot(x, y, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12)

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph - Two Lines')

plt.legend

plt.show()
