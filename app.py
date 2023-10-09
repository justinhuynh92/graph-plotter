import matplotlib.pyplot as plt

# establish x and y axises
left = [1,2,3,4,5]
height = [10,11,23,36,4]

# plot the point
plt.plot(x, y, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12)

plt.ylim(1,8)
plt.xlim(1,8)

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph - Customization')

plt.legend

plt.show()
