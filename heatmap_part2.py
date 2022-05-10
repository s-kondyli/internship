import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from skbio.stats.composition import clr, multiplicative_replacement
data = pd.read_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/mOTUs/1179_ordered.csv')
data = data.set_index('Name') #reseting the index
index = data.index # storing the index into a list for the scaled_df for the plot 
columns = data.columns.tolist() # storing the columns into a list for the scaled_df for the plot 
# Log-scaling the data 
data = multiplicative_replacement(data) # replaces all zeros with small-non-zero-values
data = clr(data) # center-log ratio transformation
# Creating the new scaled_df 
scaled_df = pd.DataFrame(data, index=index, columns=columns)
# Plotting the heatmap 
sns.heatmap(scaled_df, cmap='BuPu', linewidth=0.7, yticklabels=True, xticklabels=True) #yticklabels for all taxa to appear
plt.xticks(rotation=0, fontsize=4) # rotation & size of the ticks
plt.yticks(rotation=4, fontsize=6)
plt.ylabel('Taxa')
plt.xlabel('Day related to HCT')
plt.title('Patient 1179 Heatmap')
plt.tight_layout()
plt.savefig('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Plots/Patient_1179_Heatmap.png' , dpi=1200)