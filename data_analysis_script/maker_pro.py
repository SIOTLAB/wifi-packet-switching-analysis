import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import json
import os
import matplotlib
matplotlib.rc('font', family='Helvetica Neue')
def maker_combine(da,pdf_name,right):
    label1 = "(b)"
    label2 = "(c)"
    label3 = "(d)"
    y_value_title = 1
    markers=['o', 's', '^', 'D', 'v', '<', '>', 'p']
    fig, axs=plt.subplots(1, 3, figsize=(12, 4), width_ratios=[3,2,1])

    # if pdf_name == "Wired to Wireless (E2W) CPU Utilization and Power Consumption":
    #     custom_colors1=["whitesmoke",'gainsboro','lightcoral',"lightcoral","lightcoral","lightcoral","lightcoral","lightcoral",]
    # else:
    #     custom_colors1=["whitesmoke",'gainsboro','lightcoral',"lightcoral","lightcoral","lightskyblue","lightskyblue","lightskyblue",]            
        
    custom_colors2=["black",'lightskyblue','lightcoral',"whitesmoke","mediumaquamarine","whitesmoke","whitesmoke","whitesmoke"]
    
    k_values = list(da.keys())
    th_list=[np.mean(da[k]['throughput']['Throughput']) for k in k_values]
    # print(th_list)
    x_values=k_values[:-1]
    # n=da[]
    x_values.append(str(int(th_list[-1])))
    # draw for the irqs
    plt.subplot(1,3,1)

    # #draw for the cpus
    
    ax2=axs[0]
    bar_labels = list(da[k_values[0]]["cpu"].keys())
    bar_width = 0.3
    bar_positions = np.arange(len(k_values)*3,step=3)
    num_bars = len(bar_labels)
    legend_handles=[]
    for i, label in enumerate(bar_labels):
        mean_values = []
        values = [da[k]["cpu"][label] for k in k_values]
        # print(values)
        mean_values = [np.median(sublist) for sublist in values]
        if i==0:
            label='Processor'
        ax2.bar(bar_positions + (i+2) * bar_width-0.63, mean_values, bar_width, label=label,color=custom_colors2[i],edgecolor='black',zorder=1)
        marker_style = markers[i % len(markers)]
        ax2.scatter(bar_positions + (i+2) * bar_width - 0.63, mean_values, color='black',facecolors='white', marker=marker_style, zorder=2)
        # ax.errorbar(bar_positions + i * bar_width + bar_width / 2, mean_values,yerr=[np.abs(np.array(mean_values)-np.array(min_values)), np.abs(np.array(max_values)-np.array(mean_values))], 
        #             fmt='none', color='black', capsize=5)
        # for j, mean_value in enumerate(mean_values):
        #     vertical_position = mean_value + i*0.1
            # ax2.text(bar_positions[j] + (i)*bar_width, vertical_position,
            #         f'{int(mean_value)}', ha='center', va='bottom',fontsize=7,fontdict={'family': 'monospace'})

    
        legend_handles.append(Line2D([1], [1], marker=markers[i], color='w', markerfacecolor=custom_colors2[i], markeredgecolor='black', markersize=10, label=label))
    ax2.set_xlabel('Throughput (Mbps)',fontsize=11)
    ax2.set_ylabel('Utilization (%)')#, labelcolor="blue")#color='#00008b')
    ax2.set_xticks(bar_positions + (num_bars - 1) * bar_width / 2)
    ax2.set_xticklabels(x_values,fontsize=11)
    # Display legends
    # ax2.set_title(pdf_name)
    ax2.text(0.5, -0.2, label1, transform=ax2.transAxes, ha='center', va='center')
    # ax2.legend(loc='upper right',fontsize=12, bbox_to_anchor=(0.28, 1.0))
    ax2.legend(handles=legend_handles, loc='upper left', fontsize=11)
    ax2.tick_params(axis='y')
    ax2.grid(True, which='both', linestyle='--', linewidth=0.5, axis='y', color='gray', alpha=0.7, zorder=0)
    # if pdf_name == "E2W_SC":
    #     ax2.set_title('Single Core CPU Utilization', fontsize=12,y=y_value_title)
    # elif pdf_name == "E2W_DC":
    #     ax2.set_title('Dual Core CPU Utilization', fontsize=12,y=y_value_title)
    # elif pdf_name == "W2E_SC":
    #     ax2.set_title('Single Core CPU Utilization', fontsize=12,y=y_value_title)
    # else:
    #     ax2.set_title('Dual Core CPU Utilization', fontsize=12,y=y_value_title)
    #plot for second cpu:
    plt.subplot(1,3,2)

    # #draw for the processor cycles
    
    ax1=axs[1]
    current_script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(current_script_path)
    full_path2= os.path.join(script_directory, f"cpu_cycles.json")
    f2=open(full_path2)
    da2 = json.load(f2)
    da2=da2[pdf_name]
    k_values = list(da.keys())
    th_list=[np.mean(da[k]['throughput']['Throughput']) for k in k_values]
    x_values=k_values[:-1]
    x_values.append(str(int(th_list[-1])))
    # print(x_values)
    bar_labels = list(da[k_values[0]]["cpu"].keys())[1:right]
    num_bars = len(bar_labels)
    ax1.grid(True, which='both', linestyle='--', linewidth=0.2, axis='y', color='gray', alpha=0.7, zorder=0)
    # Plot the first bar plot
    bar_width = 0.6
    print(len(bar_labels))
    # bar1 = ax1.bar(bar_positions + (3) * bar_width-0.63, data1, width=bar_width, color="black" ,edgecolor='k', linewidth=1,label="AVG")
    for i, label in enumerate(bar_labels):
        values = da2[label]
        # print(values)
        # mean_values = [np.median(sublist) for sublist in values]
        ax1.bar(bar_positions + (i) * bar_width, values, bar_width, label=label,color=custom_colors2[i+1],edgecolor='black',zorder=1)

    

    ax1.set_xlabel('Throughput (Mbps)',fontsize=11)
    ax1.set_ylabel('Processor Cycles/Second')#, labelcolor="blue")#color='#00008b')
    ax1.set_xticks(bar_positions + (num_bars - 1) * bar_width / 2)
    ax1.set_xticklabels(x_values,fontsize=11)
    # Display legends
    # ax1.set_title(pdf_name)
    ax1.text(0.5, -0.2, label2, transform=ax1.transAxes, ha='center', va='center')
    ax1.legend(loc='upper right', fontsize=11,bbox_to_anchor=(0.4, 1.0))
    ax1.tick_params(axis='y')
    ax1.grid(True, which='both', linestyle='--', linewidth=0.5, axis='y', color='gray', alpha=0.7, zorder=0)
    # if pdf_name == "E2W_SC":
    #     ax1.set_title('Single Core CPU Cycles', fontsize=11,y=y_value_title)
    # elif pdf_name == "E2W_DC":
    #     ax1.set_title('Dual Core CPU Cycles', fontsize=11,y=y_value_title)
    # elif pdf_name == "W2E_SC":
    #     ax1.set_title('Single Core CPU Cycles', fontsize=11,y=y_value_title)
    # else:
    #     ax1.set_title('Dual Core CPU Cycles', fontsize=11,y=y_value_title)
    #plot for power

    plt.subplot(1,3,3)
    ax=axs[2]
    current_script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(current_script_path)
    full_path3= os.path.join(script_directory, f"power.json")
    f3=open(full_path3)
    data3 = json.load(f3)
    # Create the figure and axis objects
    ax.grid(True, which='both', linestyle='--', linewidth=0.2, axis='y', color='gray', alpha=0.7, zorder=0)
    # Plot the first bar plot
    print(x_values)
    print(data3[pdf_name])
    bar_width = 0.2
    ax.bar(np.arange(3), data3[pdf_name], width=bar_width, color=custom_colors2[4] ,edgecolor='k', linewidth=1)
    # Add markers on top of the bars
    # ax.plot(np.arange(len(labels))- bar_width, data1, 'bo', markerfacecolor='white',markeredgecolor='midnightblue',markersize=10, label='100 Mbps')
    # ax.plot(np.arange(len(labels)), data2, 'rs', markerfacecolor='white',markeredgecolor='#770001',markersize=10, label='500 Mbps')
    # ax.plot(np.arange(len(labels))[:1] + bar_width, data3[:1], 'g^', markerfacecolor='white', markeredgecolor='black', markersize=10, label=third_label)
    # ax.plot(np.arange(len(labels))[1:] + bar_width, data3[1:], 'p', markerfacecolor='white', markeredgecolor='black', markersize=10, label=fourth_label)


    # Set the x-axis labels
    ax.set_xlabel('Throughput (Mbps)',fontsize=11)
    
    ax.set_xticks(np.arange(len(x_values)))
    ax.set_xticklabels(x_values,fontsize=11)
    # Determine current y-limits
    # y_min, y_max = ax.get_ylim()

    # Add labels and title
    ax.set_ylabel('Power Consumption (mW)', fontsize=11)
    # ax.legend(fontsize=11,loc='upper right', bbox_to_anchor=(0.75, 1.0))
    # y_value_title = 0.94              
                       

    # Add labels "(a)" and "(b)" under the subplots
    ax.text(0.5, -0.2, label3, transform=ax.transAxes, ha='center', va='center')
    # if pdf_name == "E2W_SC":
    #     ax.set_title('Power Consumption', fontsize=11,y=y_value_title)
    # elif pdf_name == "E2W_DC":
    #     ax.set_title('Power Consumption', fontsize=11,y=y_value_title)
    # elif pdf_name == "W2E_SC":
    #     ax.set_title('Power Consumption', fontsize=11,y=y_value_title)
    # else:
    #     ax.set_title('Power Consumption', fontsize=11,y=y_value_title)
    # ax2.text(0.5, -0.2, label2, transform=ax2.transAxes, ha='center', va='center')
    # draw for the irqs
    # plt.set_title(pdf_name)
    # plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.2, wspace=0.15)
                            
    current_script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(current_script_path)
    full_path = os.path.join(script_directory, f"{pdf_name}.pdf")
    plt.tight_layout()

    plt.savefig(full_path, format='pdf')
    
    
pdf_names=["W2E_SC","E2W_SC","E2W_DC","W2E_DC"]
for pdf_name in pdf_names:
    current_script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(current_script_path)
    if pdf_name == "E2W_SC":
        full_path1= os.path.join(script_directory, f"Wired (Core 0) to Wireless (Core 0).json")
        f1=open(full_path1)
        data1 = json.load(f1)
        right=2
    elif pdf_name == "E2W_DC":
        full_path1= os.path.join(script_directory, f"Wired (Core 1) to Wireless (Core 0).json")
        f1=open(full_path1)
        data1 = json.load(f1)
        right=3
    elif pdf_name == "W2E_SC":
        full_path1= os.path.join(script_directory, f"Wireless (Core 0) to Wired (Core 0).json")
        f1=open(full_path1)
        data1 = json.load(f1)
        right=2
    else:
        full_path1= os.path.join(script_directory, f"Wireless (Core 0) to Wired (Core 1).json")
        f1=open(full_path1)
        data1 = json.load(f1)
        right=3
    maker_combine(data1,pdf_name,right)