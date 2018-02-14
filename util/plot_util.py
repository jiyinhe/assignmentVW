"""
This script provides utility functions to make plots.
"""
import matplotlib.pyplot as plt
import numpy as np

def bar_plot(X, Y, bottoms=None, barwidth=1.0, 
    figsize=None,labels=None, title=None, 
    xticks=None, xtick_labels=None, rotation=None,
    ylabel=None, xlabel=None, ylim=None, xlim=None,
    ):
    """
    X: numpy array
    Y: numpy array, must have the same dimension as X
    bottoms: numpy array, must have the same dimension as X
    figsize: (width, hight)
    labels: array-like, it must be the same length as X.shape[1]
    title: string
    xticks: array-like, must be the same length as X.shape[1]
    xtick_labels: array-like, must be the same length as xticks 
    rotation: rotation of xtick labels
    ylabel: string, 
    xlabel: string,
    ylim: (min, max),
    xlim: (min, max),
    """
    fig, ax = plt.subplots(figsize=figsize)
    bars = []
    if bottoms is None:
        bottoms = np.zeros(X.shape)

    for i in range(X.shape[0]):
        bar = ax.bar(X[i], Y[i], width=barwidth, bottom=bottoms[i])
        bars.append(bar)
    if title:
        ax.set_title(title)
    if labels:
        ax.legend(labels)
    if xticks:
        ax.set_xticks(xticks)
    if xtick_labels:
        ax.set_xticklabels(xtick_labels, rotation=rotation)
    if ylabel:
        ax.set_ylabel(ylabel)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylim:
        ax.set_ylim(ylim)
    if xlim:
        ax.set_xlim(xlim)
    return ax, bars
 

def add_line(X, Y, ax, ylim=None, ylabel=None):
    """
    Adding a line plot to an existing plot
    X: array-like
    Y: array-like
    ax: the axis to add the line to 
    ylim: sometimes the added line needs a second y-axis, which may need to set a
        different limit.
    ylabel: for twin axis
    """
    line, = ax.plot(X, Y)
    if ylim:
        ax.set_ylim(ylim)
    if ylabel:
        ax.set_ylabel(ylabel)
    return line


    
