import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib
matplotlib.rc('font', family='Helvetica Neue')
# Data for the first legend
# data1 = [7061061, 
#          25065572, 4837389,109130362,
#          3303908, 3530530,84201955,
#          0,0,0,0]

# # Data for the second legend
# data2 = [42008839,
#         79281613, 43007645,350170288,
#         3980769,3018425,125976699,
#         19777081,55350330,22436933,277170849]

# # Labels for the x-ax0is
# labels = ["ETH\nRX\nSoftIRQ", 'ETH\npoll\nfunction', "ETH\nIP\nstack","ETH\nXmit",
#           "TX IRQ \n Init","TX \n SoftIRQ","TX \n Reclaim",
#           "IWL\nRX\nSoftirq","IWL \n Poll \n Function","IWL \n IP stack",
#           "IWL \n Xmit"]
data1 =[58204525,146450507,0,2525642921]
data2 =[53920079,53920079,188694334,615519267]
labels = ["Dev \n Xmit","Enable \n BH","Qdisc \n Process","Direct \n Xmit"]
data3 =[262376874,934629910,0,15300546236]
data4 =[256914217,682217914,1104198626,1338912900]
# Width of each bar
bar_width = 0.35

# Positions of the bars on the x-ax0is
r = np.arange(len(data1))
label1 = "(a)"
label2 = "(b)"
# Create the bar graph
# fig, ax0 = plt.subplots(figsize=(8, 4))
fig, acs = plt.subplots(1, 2, figsize=(12, 4), width_ratios=[1,1])
plt.subplot(1,2,1)
ax0=acs[0]
ax0.grid(True, which='both', linestyle='--', linewidth=0.5, axis='y', color='gray', alpha=0.7, zorder=0)
# Plot the first legend's data
# bar1 = ax0.bar(r, data1, color='lightsteelblue', width=bar_width, edgecolor='black', label='Dual Core')

# # Plot the second legend's data on top of the first legend's data
# bar2 = ax0.bar(r, data2, color="#fdc1c5", width=bar_width, edgecolor='black', label='Single Core')
# Plot the first bar plot
bar1 = ax0.bar(np.arange(len(labels)) - bar_width/2, data1, width=bar_width, color='darkslateblue' ,edgecolor='k', linewidth=1, zorder=4)
bar2 = ax0.bar(np.arange(len(labels)) + bar_width/2, data2, width=bar_width, color="thistle", edgecolor='k', linewidth=1, zorder=4)

marker_size = 8

# Add markers on top of the bars
ax0.plot(np.arange(len(labels))- bar_width/2, data1, 'b^', markerfacecolor='white',markeredgecolor='black',markersize=marker_size,  label='Ethernet to Wireless (E2W) (500 Mbps)', zorder=5)
ax0.plot(np.arange(len(labels)) + bar_width/2, data2, 'rs', markerfacecolor='white',markeredgecolor='black',markersize=marker_size, label='Wireless to Ethernet (W2E) (500 Mbps)', zorder=5)
# Add labels and title
ax0.set_xlabel('Init Xmit Sub-Stages',fontsize=12)
ax0.set_ylabel('Processor Cycles/Second',fontsize=14)
# ax0.set_title('Stacked Bar Graph')
ax0.set_xticks(r)
ax0.set_xticklabels(labels,fontsize=13)
ax0.text(0.5, -0.35, label1, transform=ax0.transAxes,fontsize=12, ha='center', va='center')
# Add a legend
ax0.legend(fontsize=13)
ax0.set_title('Throughput: 500 Mbps', fontsize=14)
plt.subplot(1,2,2)
ax=acs[1]
ax.grid(True, which='both', linestyle='--', linewidth=0.5, axis='y', color='gray', alpha=0.7, zorder=0)
# Plot the first legend's data
# bar1 = ax.bar(r, data1, color='lightsteelblue', width=bar_width, edgecolor='black', label='Dual Core')

# # Plot the second legend's data on top of the first legend's data
# bar2 = ax.bar(r, data2, color="#fdc1c5", width=bar_width, edgecolor='black', label='Single Core')
# Plot the first bar plot
bar1 = ax.bar(np.arange(len(labels)) - bar_width/2, data3, width=bar_width, color='darkslateblue' ,edgecolor='k', linewidth=1, zorder=4)
bar2 = ax.bar(np.arange(len(labels)) + bar_width/2, data4, width=bar_width, color="thistle", edgecolor='k', linewidth=1, zorder=4)

marker_size = 8

# Add markers on top of the bars
ax.plot(np.arange(len(labels))- bar_width/2, data3, 'b^', markerfacecolor='white',markeredgecolor='black',markersize=marker_size,  label='Ethernet to Wireless (E2W) (894 Mbps)', zorder=5)
ax.plot(np.arange(len(labels)) + bar_width/2, data4, 'rs', markerfacecolor='white',markeredgecolor='black',markersize=marker_size, label='Wireless to Ethernet (W2E) (949 Mbps)', zorder=5)
# Add labels and title
ax.set_xlabel('Init Xmit Sub-Stages',fontsize=12)
ax.set_ylabel('Processor Cycles/Second',fontsize=14)
# ax.set_title('Stacked Bar Graph')
ax.set_xticks(r)
ax.set_xticklabels(labels,fontsize=13)
ax.text(0.5, -0.35, label2, transform=ax.transAxes,fontsize=12, ha='center', va='center')
# Add a legend
ax.legend(fontsize=13)
ax.set_title('Throughput: Maximum', fontsize=14)
# Display the graph
plt.tight_layout()
current_script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(current_script_path)
full_path = os.path.join(script_directory, "diff_graph.pdf")
plt.tight_layout()

plt.savefig(full_path)