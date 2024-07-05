import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import json
import os
import matplotlib
matplotlib.rc('font', family='Helvetica Neue')
def maker_combine(da,pdf_name):

    fig, ax0=plt.subplots(1, 1, figsize=(10, 4))

    if pdf_name == "Wired (Core 0) to Wireless (Core 0)" or pdf_name == "Wireless (Core 0) to Wired (Core 0)":
        custom_colors1=["whitesmoke",'gainsboro','lightcoral',"lightcoral","lightcoral","lightcoral","lightcoral","lightcoral",]
    else:
        custom_colors1=["whitesmoke",'gainsboro','lightcoral',"lightcoral","lightcoral","lightskyblue","lightskyblue","lightskyblue",]            
        
    custom_colors2=["black",'lightskyblue','lightcoral',"whitesmoke","mediumaquamarine","whitesmoke","whitesmoke","whitesmoke",]
    
    k_values = list(da.keys())
    th_list=[np.mean(da[k]['throughput']['Throughput']) for k in k_values]
    # print(th_list)
    x_values=k_values[:-1]
    # n=da[]
    x_values.append(str(int(th_list[-1])))
    # draw for the irqs
    # plt.subplot(1,2,1)
    bar_labels = list(da[k_values[0]]["irq"].keys())
    num_bars = len(bar_labels)
    # ax0=axs[0]
    bar_width = 0.3
    bar_positions = np.arange(len(k_values)*3,step=3)
    markers=['o', 's', '^', 'D', 'v', '<', '>', 'p']
    legend_elements=[]
    for i, label in enumerate(bar_labels):
        
        mean_values = []
        values = [da[k]["irq"][label] for k in k_values]
        # print(values)
        if label=="softnet":
            mean_values = [np.max(sublist) for sublist in values]
        else:
            mean_values = [np.median(sublist) for sublist in values]
        print(mean_values)
        ax0.bar(bar_positions + (i+3) * bar_width-0.9, mean_values, bar_width,color=custom_colors1[i],edgecolor='black', zorder=2)
        # ax.errorbar(bar_positions + i * bar_width + bar_width / 2, mean_values,yerr=[np.abs(np.array(mean_values)-np.array(min_values)), np.abs(np.array(max_values)-np.array(mean_values))], 
                    # fmt='none', color='black', capsize=5)
        for j, mean_value in enumerate(mean_values):
            vertical_position = mean_value - 500
            marker_position = bar_positions[j] + (i + 3) * bar_width - 0.9
            ax0.scatter(marker_position, vertical_position, marker=markers[i], facecolors='none', edgecolors='black', s=50, zorder=5)
            ax0.set_xticklabels(x_values, fontsize=11)
        legend_elements.append(Line2D([1], [1], marker=markers[i], color='w', markerfacecolor=custom_colors1[i], markeredgecolor='black', markersize=10, label=label))
    # legend_elements=legend_elements[:]
    # Set labels, title, and legend
    ax0.set_xlabel('Throughput (Mbps)', fontsize=11)
    ax0.set_ylabel('Average Number per Second',fontsize=11)
    # ax0.set_title(pdf_name)
    ax0.set_xticks(bar_positions + (num_bars - 1) * bar_width / 2)
    ax0.legend(handles=legend_elements, loc='upper left', fontsize=11)
    # ax0.legend(prop={'size': 9})
    # ax0.set_ylim(0, 90000)

    ax0.grid(True, which='both', linestyle='--', linewidth=0.5, axis='y', color='gray', alpha=0.7, zorder=0)


    # y_value_title = 0.94
    if pdf_name == "Wired (Core 0) to Wireless (Core 0)":
        # fig.suptitle('Single Core Configuration', fontsize=12,y=y_value_title)
        label1 = "(a)"
        # label2 = "(b)"

    if pdf_name == "Wired (Core 1) to Wireless (Core 0)":
        # fig.suptitle('Dual Core Configuration', fontsize=12,y=y_value_title)
        label1 = "(a)"
        # label2 = "(d)"        
        
    if pdf_name == "Wireless (Core 0) to Wired (Core 0)":
        # fig.suptitle('Single Core Configuration', fontsize=12,y=y_value_title)
        label1 = "(a)"
        # label2 = "(b)"               

    if pdf_name == "Wireless (Core 0) to Wired (Core 1)":
        # fig.suptitle('Dual Core Configuration', fontsize=12,y=y_value_title)
        label1 = "(a)"
        # label2 = "(d)"               
                       

    # Add labels "(a)" and "(b)" under the subplots
    ax0.text(0.5, -0.2, label1, fontsize=11,transform=ax0.transAxes, ha='center', va='center')
    # ax1.text(0.5, -0.2, label2, transform=ax1.transAxes, ha='center', va='center')
    # draw for the irqs
    # plt.suptitle(pdf_name)
    # plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.2, wspace=0.15)
                            
    current_script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(current_script_path)
    full_path = os.path.join(script_directory, f"{pdf_name}.pdf")
    plt.tight_layout()

    plt.savefig(full_path, format='pdf')
    
    
pdf_names=["Wireless (Core 0) to Wired (Core 0)","Wireless (Core 0) to Wired (Core 1)"]
# pdf_names=["Wired (Core 0) to Wireless (Core 0)","Wired (Core 1) to Wireless (Core 0)"]

for pdf_name in pdf_names:
    
    current_script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(current_script_path)
    full_path = os.path.join(script_directory, f"{pdf_name}.json")
        
    f=open(full_path)
    data = json.load(f)
    maker_combine(data,pdf_name)