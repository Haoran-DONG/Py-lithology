#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 10:24:42 2025
This script is written in Python to plot lithology patterns.
@author: donghr
"""

import numpy as np



def plot_lithology(ob,ax,num_layer,litho_type):
    '''
    ob only contain rectangle;
    ax is from matplotlib;
    num_layer is how many layer you want to divide;
    litho_type contains: shale, mudstone, siltstone, limestone, dolomite, gypsite, sandstone, halite.
    '''
    x0,y0 = ob.get_xy()
    p_w = ob.get_width()
    p_h = ob.get_height()
    width_layer = 0.8
    # Sublayers
    for i in range(1, num_layer):
        y = y0 + p_h / num_layer * i
        ax.hlines(y, x0, x0 + p_w, colors='k', linestyles='-', linewidth=width_layer,zorder=2)
    sub_layer_heights = []
    sub_layer_mid_heights = []
    for i in range(num_layer):
        sub_bottom = y0 + p_h / num_layer * i
        sub_top = y0 + p_h / num_layer * (i + 1)
        sub_mid = (sub_bottom + sub_top) / 2
        sub_layer_heights.append((sub_bottom, sub_top))
        sub_layer_mid_heights.append(sub_mid)
        ax.hlines(sub_mid, x0, x0 + p_w, colors='k', linestyles='-', linewidth=width_layer,zorder=2)
    # -------------------------------------------------------------------------
    # Lithology patterns
    if litho_type == 'shale':
        # Shale
        width_litho_shale = 0.5
        for i, (bottom, top) in enumerate(sub_layer_heights):
            shale_line_y = np.linspace(bottom, top, 5)
            for y in shale_line_y[[1,3]]:
                ax.hlines(y, x0, x0 + p_w, colors='k', linestyles='-', linewidth=width_litho_shale,zorder=1)
    elif litho_type == 'mudstone':
        # Mudstone
        width_litho_mud = 0.5
        dash_length= 200
        gap_length = 200
        dash_cycle = dash_length + gap_length 
        for i, (bottom, top) in enumerate(sub_layer_heights):
            mud_line_y = np.linspace(bottom, top, 5)
            num_dashes = int(p_w / dash_cycle) + 1
            y1 = mud_line_y[1]
            for j in range(num_dashes):
                start_x = x0 + j * dash_cycle
                end_x = min(start_x + dash_length, x0 + p_w)
                ax.plot([start_x, end_x], [y1, y1], color='k', linewidth=width_litho_mud, zorder=1)
            y3 = mud_line_y[3]
            for j in range(num_dashes-1):
                start_x = x0 + (j + 0.5) * dash_cycle
                end_x = min(start_x + dash_length, x0 + p_w)
                ax.plot([start_x, end_x], [y3, y3], color='k', linewidth=width_litho_mud, zorder=1)
    elif litho_type == 'siltstone':
        # Siltstone
        scatter_spacing= 200
        scatter_offset = 80
        scatter_cycle = scatter_spacing * 2
        for i, (bottom, top) in enumerate(sub_layer_heights):
            silt_line_y = np.linspace(bottom, top, 5)
            num_scatter_groups = int(p_w / scatter_cycle) 
            y1 = silt_line_y[1]
            for j in range(num_scatter_groups):
                group_center = x0 + j * scatter_cycle 
                ax.scatter([group_center + scatter_offset, group_center + 2*scatter_offset], 
                           [y1, y1], marker='.', color='k', s=10, zorder=1)
            y3 = silt_line_y[3]
            for j in range(num_scatter_groups):
                group_center = x0 + (j + 0.5) * scatter_cycle 
                ax.scatter([group_center + scatter_offset, group_center + 2*scatter_offset], 
                           [y3, y3], marker='.', color='k', s=10, zorder=1)
    elif litho_type == 'limestone':
        # Limestone
        width_litho_lime = 0.5
        horizontal_spacing = 200
        horizontal_cycle = horizontal_spacing * 2
        for i, (bottom, top) in enumerate(sub_layer_heights):
            lime_line_y = np.linspace(bottom, top, 5)
            y2 = lime_line_y[2]
            x_max = x0 + p_w
            j = 0
            while True:
                x_pos = x0 + j * horizontal_cycle
                if x_pos > x_max:
                    break
                ax.plot([x_pos, x_pos], [lime_line_y[0], y2], color='k', linewidth=width_litho_lime, zorder=2)
                j += 1
            j = 0
            while True:
                x_pos = x0 + (j + 0.5) * horizontal_cycle
                if x_pos > x_max:
                    break
                ax.plot([x_pos, x_pos], [y2, lime_line_y[4]], color='k', linewidth=width_litho_lime, zorder=2)
                j += 1
    elif litho_type == 'dolomite':
        # Dolomite
        width_litho_dolo = 0.5
        horizontal_spacing = 100
        horizontal_cycle = horizontal_spacing * 2
        dolo_d = 30
        for i, (bottom, top) in enumerate(sub_layer_heights):
            dolo_line_y = np.linspace(bottom, top, 5)
            y2 = dolo_line_y[2]
            x_max = x0 + p_w
            j = 0
            while True:
                x_center = x0 + j * horizontal_cycle
                x_left = x_center - dolo_d
                x_right = x_center + dolo_d
                if x_left >= x0 and x_right <= x_max:
                    ax.plot([x_left, x_right], [dolo_line_y[0], y2], 
                             color='k', linewidth=width_litho_dolo, zorder=2)
                elif x_left > x_max:
                    break   
                j += 1
            j = 0
            while True:
                x_center = x0 + (j + 0.5) * horizontal_cycle
                x_left = x_center - dolo_d
                x_right = x_center + dolo_d
                if x_left >= x0 and x_right <= x_max:
                    ax.plot([x_left, x_right], [y2, dolo_line_y[4]], 
                             color='k', linewidth=width_litho_dolo, zorder=2)
                elif x_left > x_max:
                    break
                j += 1
    elif litho_type == 'gypsite':
        # Gypsite
        width_litho_gyp = 0.5
        for i, (bottom, top) in enumerate(sub_layer_heights):
            gyp_line_y = np.linspace(bottom, top, 5)
            delta_h = gyp_line_y[2] - gyp_line_y[0]
            x_max = x0 + p_w
            j = 0
            while True:
                x_start = x0 + j * delta_h
                x_end = x_start + delta_h
                if x_start > x_max:
                    break
                clip_x_start = max(x_start, x0)
                clip_x_end = min(x_end, x_max)
                y_start = gyp_line_y[2] - (clip_x_start - x_start)
                y_end = gyp_line_y[0] + (x_end - clip_x_end)
                ax.plot([clip_x_start, clip_x_end], [y_start, y_end], 
                         color='k', linewidth=width_litho_gyp, zorder=2)
                j += 1
            j = 0
            while True:
                x_start = x0 + j * delta_h
                x_end = x_start + delta_h
                if x_start > x_max:
                    break
                clip_x_start = max(x_start, x0)
                clip_x_end = min(x_end, x_max)
                y_start = gyp_line_y[4] - (clip_x_start - x_start)
                y_end = gyp_line_y[2] + (x_end - clip_x_end)
                ax.plot([clip_x_start, clip_x_end], [y_start, y_end], 
                         color='k', linewidth=width_litho_gyp, zorder=2)
                j += 1
    elif litho_type == 'sandstone':
        # Sandstone
        for i, (bottom, top) in enumerate(sub_layer_heights):
            sand_line_y = np.linspace(bottom, top, 5)
            delta_h = sand_line_y[1] - sand_line_y[0]
            x_max = x0 + p_w
            j = 1
            while True:
                x_pos = x0 + j * delta_h
                if x_pos >= x_max:
                    break
                ax.scatter(x_pos, sand_line_y[1], color='k', marker='.', s=2, zorder=1)
                j += 1
            j = 1
            while True:
                x_pos = x0 + j * delta_h + delta_h/2
                if x_pos >= x_max-2: # Digital correction
                    break
                ax.scatter(x_pos, sand_line_y[3], color='k', marker='.', s=2, zorder=1)
                j += 1
    elif litho_type == 'halite':
        # Halite
        width_litho_hal = 0.5
        for i, (bottom, top) in enumerate(sub_layer_heights):
            hal_line_y = np.linspace(bottom, top, 5)
            delta_h = hal_line_y[2] - hal_line_y[0]
            x_max = x0 + p_w
            j = 1
            while True:
                x_pos = x0 + j * delta_h
                if x_pos >= x_max:
                    break
                ax.plot([x_pos, x_pos], [hal_line_y[0], hal_line_y[-1]], 
                         color='k', linewidth=width_litho_hal, zorder=2)
                j += 1 