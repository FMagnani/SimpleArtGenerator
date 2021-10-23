#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:46:56 2021

@author: FMagnani
GitHub: https://github.com/FMagnani
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%%

# IMPORT DATA

df = pd.read_csv("Data.csv", index_col=0)

data_list = [np.array(df)[:, 0:2]]
for i in [2,4,6,8,10,12]:
    data_list = np.append(data_list, [np.array(df)[:, i:i+2]], axis=0)
    
#%%

# COLOR LISTS AVAILABLE

# The 4 colours are:
#   axis facecolor
#   color line 1 
#   color line 2
#   shadow color
# 
# These combinatinos will be picked at random
colors_list_1 = [
              ('peachpuff', 'k', 'k', 'sienna', 'sienna'),
              ('coral', 'k', 'k', 'brown', 'brown'),
              ('indianred', 'k', 'k', 'peachpuff', 'peachpuff')
              ]    

colors_list_2 = [
              ('black', 'white', 'white', 'fuchsia', 'cyan'),
              ('black', 'white', 'aqua', 'magenta', 'magenta'),
              ('black', 'magenta', 'white', 'white', 'aqua')            
              ]


colors_list_3 = [
              ('darkkhaki', 'saddlebrown', 'darkgreen', 'blue', 'w'),
              ('gold', 'k', 'w', 'r', 'r'),
              ('aqua', 'firebrick', 'forestgreen', 'k', 'k')            
              ]




# SET PARAMETERS

# seed = 7898
fig_facecolor = 'black'
colors_list_selected = colors_list_3

# RUN

# Set seed
# np.random.seed(seed)

# Figure initialization
fig = plt.figure()
fig.set_facecolor(fig_facecolor)

# Subplots intitialization
axes = []
for i in range(16):    
    axes.append(fig.add_subplot(4,4,i+1, projection='polar'))

for i in range(16):
    
    # Select at random two items from the data list
    idx_1 = np.random.choice(range(7), 1)[0]
    idx_2 = np.random.choice(range(7), 1)[0]
    
    # First item is used unchanged
    x = data_list[idx_1]
    
    # Not the second item itself is used, but it's increments 
    y = data_list[idx_2]
    speed = y[:-1]-y[1:]
    
    # Select color palettes from the chosen color list
    idx_c = np.random.choice([0,1,2], 1)[0]
    
    c1 = colors_list_selected[idx_c][0]
    c2 = colors_list_selected[idx_c][1]
    c3 = colors_list_selected[idx_c][2]
    c4 = colors_list_selected[idx_c][3]
    c5 = colors_list_selected[idx_c][4]
    
    # Remove grids and ticks from the graph
    ax = axes[i]
    ax.set_rticks([])  
    ax.set_xticks([])
    ax.grid(False)
    
    # Facecolor
    ax.set_facecolor(c1)  

    # Shadow/Glow
    ax.plot(x[1:,0], speed[:,0], c=c4, marker='+', linewidth=.5, alpha=.1)
    ax.plot(x[1:,0], speed[:,1], c=c5, marker='+', linewidth=.5, alpha=.1)    
    
    # Lines
    ax.plot(x[1:,0], speed[:,0], c=c2, linestyle='-', linewidth=1, alpha=1)
    ax.plot(x[1:,0], speed[:,1], c=c3, linestyle='-', linewidth=1, alpha=1)
    
    # In case you wanna know the combinations employed
    print(idx_1, idx_2)


plt.show()


























