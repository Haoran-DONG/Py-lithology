#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 10:31:42 2025
This script is written to test plot_lithology.
@author: donghr
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import Functions

df_logging = pd.read_csv('./data/logging-demo.CSV')
#%%
# Plot parameters
width_whole =2400
width_system=400
width_group =2000
width_layer = 1
# Triassic
rect_01_T  =Rectangle((0  , df_logging.Elevation[2])  ,width_system,df_logging.Thickness[0 :2 +1].sum(),facecolor='#8a3ea4'   ,edgecolor='k',linewidth=width_layer)
rect_01_T_1=Rectangle((400, df_logging.Elevation[0])  ,width_group ,df_logging.Thickness[0 :0 +1].sum(),facecolor='w'         ,edgecolor='k',linewidth=width_layer)
rect_01_T_2=Rectangle((400, df_logging.Elevation[1])  ,width_group ,df_logging.Thickness[1 :1 +1].sum(),facecolor='w'         ,edgecolor='k',linewidth=width_layer)
rect_01_T_3=Rectangle((400, df_logging.Elevation[2])  ,width_group ,df_logging.Thickness[2 :2 +1].sum(),facecolor='w'         ,edgecolor='k',linewidth=width_layer)
# Permian
rect_02_P  =Rectangle((0  , df_logging.Elevation[5])  ,width_system,df_logging.Thickness[3 :5 +1].sum(),facecolor='#e84d40'   ,edgecolor='k',linewidth=width_layer)
rect_02_P_1=Rectangle((400, df_logging.Elevation[3])  ,width_group ,df_logging.Thickness[3 :3 +1].sum(),facecolor='w'         ,edgecolor='k',linewidth=width_layer)
rect_02_P_2=Rectangle((400, df_logging.Elevation[5])  ,width_group ,df_logging.Thickness[4 :5 +1].sum(),facecolor='w'         ,edgecolor='k',linewidth=width_layer)
# Silurian
rect_03_S  =Rectangle((0  , df_logging.Elevation[7])  ,width_system,df_logging.Thickness[6 :7 +1].sum(),facecolor='#b3e4c2'   ,edgecolor='k',linewidth=width_layer)
rect_03_S_1=Rectangle((400, df_logging.Elevation[6])  ,width_group ,df_logging.Thickness[6 :6 +1].sum(),facecolor='w'         ,edgecolor='k',linewidth=width_layer)
rect_03_S_2=Rectangle((400, df_logging.Elevation[7])  ,width_group ,df_logging.Thickness[7 :7 +1].sum(),facecolor='w'         ,edgecolor='k',linewidth=width_layer)
# Ordovician
rect_04_O  =Rectangle((0  , df_logging.Elevation[8])  ,width_system,df_logging.Thickness[8 :8 +1].sum(),facecolor='#00a990'   ,edgecolor='k',linewidth=width_layer)
rect_04_O_1=Rectangle((400, df_logging.Elevation[8])  ,width_group ,df_logging.Thickness[8 :8 +1].sum(),facecolor='w'         ,edgecolor='k',linewidth=width_layer)
# Cambrian
rect_05_C  =Rectangle((0  , df_logging.Elevation[10]) ,width_system,df_logging.Thickness[9 :10+1].sum(),facecolor='#83ad6a'   ,edgecolor='k',linewidth=width_layer)
rect_05_C_1=Rectangle((400, df_logging.Elevation[9] ) ,width_group ,df_logging.Thickness[9 :9 +1].sum(),facecolor='w'         ,edgecolor='k',linewidth=width_layer)
rect_05_C_2=Rectangle((400, df_logging.Elevation[10]) ,width_group ,df_logging.Thickness[10:10+1].sum(),facecolor='w'         ,edgecolor='k',linewidth=width_layer)
# Sinian or Ediacaran
rect_06_S  =Rectangle((0  , df_logging.Elevation[12]) ,width_system,df_logging.Thickness[11:12+1].sum(),facecolor='#fdd56e'   ,edgecolor='k',linewidth=width_layer)
rect_06_S_1=Rectangle((400, df_logging.Elevation[11]) ,width_group ,df_logging.Thickness[11:11+1].sum(),facecolor='w'         ,edgecolor='k',linewidth=width_layer)
rect_06_S_2=Rectangle((400, df_logging.Elevation[12]) ,width_group ,df_logging.Thickness[12:12+1].sum(),facecolor='w'         ,edgecolor='k',linewidth=width_layer)
# -----------------------------------------------------------------------------
# Plot
plt.close('all')
fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(111)
# Add patches
# Triassic
ax1.add_patch(rect_01_T)
ax1.add_patch(rect_01_T_1)
ax1.add_patch(rect_01_T_2)
ax1.add_patch(rect_01_T_3)
# Permian
ax1.add_patch(rect_02_P)
ax1.add_patch(rect_02_P_1)
ax1.add_patch(rect_02_P_2)
# Silurian
ax1.add_patch(rect_03_S)
ax1.add_patch(rect_03_S_1)
ax1.add_patch(rect_03_S_2)
# Ordovician
ax1.add_patch(rect_04_O)
ax1.add_patch(rect_04_O_1)
# Cambrian
ax1.add_patch(rect_05_C)
ax1.add_patch(rect_05_C_1)
ax1.add_patch(rect_05_C_2)
# Sinian or Ediacaran
ax1.add_patch(rect_06_S)
ax1.add_patch(rect_06_S_1)
ax1.add_patch(rect_06_S_2)
# -----------------------------------------------------------------------------
# Add lithology patterns
# Triassic
Functions.plot_lithology(rect_01_T_1,ax1,2,'limestone')
Functions.plot_lithology(rect_01_T_2,ax1,2,'mudstone')
Functions.plot_lithology(rect_01_T_3,ax1,2,'limestone')
# Permian
Functions.plot_lithology(rect_02_P_1,ax1,1,'mudstone')
Functions.plot_lithology(rect_02_P_2,ax1,2,'limestone')
# Silurian
Functions.plot_lithology(rect_03_S_1,ax1,1,'siltstone')
Functions.plot_lithology(rect_03_S_2,ax1,3,'shale')
# Ordovician
Functions.plot_lithology(rect_04_O_1,ax1,1,'limestone')
# Cambrian
Functions.plot_lithology(rect_05_C_1,ax1,2,'dolomite')
Functions.plot_lithology(rect_05_C_2,ax1,4,'gypsite')
# Sinian or Ediacaran
Functions.plot_lithology(rect_06_S_1,ax1,4,'sandstone')
Functions.plot_lithology(rect_06_S_2,ax1,3,'halite')
# -----------------------------------------------------------------------------
ax1.set_aspect('equal')
ax1.set_xlim(-100,2500)
ax1.set_ylim(-6200,500)
ax1.set_ylabel('elevation (m)')
plt.savefig('./figs/demo.png',dpi=300)
