import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.rc('font', family='Helvetica Neue')
# Sample 2D arrays
data1 = np.array([2862590, 0, 35305310, 125327860, 24186950, 545651810,16519540,17652650,0,42100978])
data2 = np.array([0, 2997902, 9662661, 319206408, 19903429, 203576569,16517,22670088,1024077,24206204])
data3 = np.array([11505884, 0, 7157315, 181484997, 35971926, 909150155,2951323,3778264,0,159727899])
data4 = np.array([207592, 33096095, 14264536, 691696532, 31702263, 341562974,222420,143772285,119395054,158214757])
data1 = np.insert(data1, 0, np.sum(data1))
data2 = np.insert(data2, 0, np.sum(data2))
data3 = np.insert(data3, 0, np.sum(data3))
data4 = np.insert(data4, 0, np.sum(data4))
# print(data1)
# Set the x-axis labels
x_labels = ['Total \n Cycles','Init \n Ksoftirqd', 'Init \n RX-IRQ', 'RX \n SoftIRQ', 'Poll \n Function', 'IP \n Stack', 'Init \n Xmit','Init \n TX-IRQ','TX \n SoftIRQ','TX \n Qdisc','TX \n Reclaim',]

# Create the figure and axis objects
fig, (ax, ax1) = plt.subplots(2, 1, figsize=(9,7), gridspec_kw={'height_ratios': [1, 1]})

ax.grid(True, which='both', linestyle='--', linewidth=0.5, axis='y', color='gray', alpha=0.7, zorder=0)

bar_width = 0.3

# Plot the first bar plot
bar1 = ax.bar(np.arange(len(x_labels)) - bar_width/2, data1, width=bar_width, color='darkslateblue' ,edgecolor='k', linewidth=1, zorder=4)
bar2 = ax.bar(np.arange(len(x_labels)) + bar_width/2, data2, width=bar_width, color="thistle", edgecolor='k', linewidth=1, zorder=4)

marker_size = 8

# Add markers on top of the bars
ax.plot(np.arange(len(x_labels))- bar_width/2, data1, 'b^', markerfacecolor='white',markeredgecolor='midnightblue',markersize=marker_size, label='Ethernet to Wireless (E2W) \n (500 Mbps)', zorder=5)
ax.plot(np.arange(len(x_labels)) + bar_width/2, data2, 'rs', markerfacecolor='white',markeredgecolor='#770001',markersize=marker_size, label='Wireless to Ethernet (W2E) \n (500 Mbps)', zorder=5)

ax.text(0.5, -0.25, '(a)', transform=ax.transAxes, fontsize=12, ha='center', va='center')
# Set the x-axis labels
ax.set_xticks(np.arange(len(x_labels)))
ax.set_xticklabels(x_labels, fontsize=12)

ax.set_title('Throughput: 500 Mbps', fontsize=12)

# Add labels and title
ax.set_ylabel('Processor Cycles/Second', fontsize=12)
ax.legend(fontsize=12)

# Determine current y-limits
y_min, y_max = ax.get_ylim()

# Extend the y-axis lower limit to create more space
new_y_min = y_min - (y_max - y_min) * 0.05  # Adding 10% padding below
ax.set_ylim(new_y_min, y_max)

# Plot the second bar plot
bar3 = ax1.bar(np.arange(len(x_labels)) -bar_width/2, data3, width=bar_width, color='darkslateblue', edgecolor='k', linewidth=1, zorder=4)
bar4 = ax1.bar(np.arange(len(x_labels)) + bar_width/2, data4, width=bar_width, color="thistle", edgecolor='k', linewidth=1, zorder=4)

# Add markers on top of the bars
ax1.plot(np.arange(len(x_labels))-bar_width/2, data3, 'b^', markerfacecolor='white',markeredgecolor='midnightblue',markersize=marker_size, label='Ethenet to Wireless (E2W) \n (893 Mbps)', zorder=5)
ax1.plot(np.arange(len(x_labels)) + bar_width/2, data4, 'rs', markerfacecolor='white',markeredgecolor='#770001',markersize=marker_size, label='Wireless to Ethernet (W2E) \n (949 Mbps)', zorder=5)

ax1.grid(True, which='both', linestyle='--', linewidth=0.5, axis='y', color='gray', alpha=0.7, zorder=0)

ax1.set_title('Throughput: Maximum', fontsize=12)


ax1.text(0.5, -0.25, '(b)', transform=ax1.transAxes, fontsize=12, ha='center', va='center')
# Set the x-axis labels
ax1.set_xticks(np.arange(len(x_labels)))
ax1.set_xticklabels(x_labels, fontsize=12)

# Add labels and title
ax1.set_ylabel('Processor Cycles/Second', fontsize=12)
ax1.legend(fontsize=12)
# Show the plot

# Determine current y-limits
y_min, y_max = ax1.get_ylim()
# Extend the y-axis lower limit to create more space
new_y_min = y_min - (y_max - y_min) * 0.05  # Adding 10% padding below
ax1.set_ylim(new_y_min, y_max)

current_script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(current_script_path)
full_path = os.path.join(script_directory, "flame_graph.pdf")
plt.tight_layout()

plt.savefig(full_path)