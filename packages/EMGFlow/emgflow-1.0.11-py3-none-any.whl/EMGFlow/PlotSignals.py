import pandas as pd
import os
import re
import matplotlib.pyplot as plt
import random
import webbrowser
from tqdm import tqdm

from shiny import App, render, ui

import nest_asyncio
nest_asyncio.apply()

from SignalFilterer import ConvertMapFiles, MapFilesFuse, EMG2PSD

#
# =============================================================================
#

"""
A collection of functions for plotting subject data
"""

#
# =============================================================================
#

def PlotSpectrum(in_path, out_path, sampling_rate, cols=None, p=None, expression=None, file_ext='csv'):
    """
    Generate plots of the PSDs of each column of Signals in a directory

    Parameters
    ----------
    in_path : str
        Filepath to a directory to read Signal files.
    out_path : str
        Filepath to an output directory.
    sampling_rate : float
        Sampling rate of the Signals.
    cols : list, optional
        List of columns of the Signal to plot. The default is None, in which case every column except
        'time' is plotted.
    p : float, optional
        Random sampling probability. If given a percentage, will have that probability to plot
        each Signal. The default is None, in which case all Signals are plotted.
    expression : str, optional
        A regular expression. If provided, will only generate plots for files whose names match the regular
        expression. The default is None.
    file_ext : str, optional
        File extension for files to read. Only reads files with this extension. The default is 'csv'.

    Returns
    -------
    None.

    """
    
    # Convert out path to absolute
    if not os.path.isabs(out_path):
        out_path = os.path.abspath(out_path) + '\\'
    
    filedirs = ConvertMapFiles(in_path, file_ext=file_ext, expression=expression)
    
    # Make plots
    for file in tqdm(filedirs):
        if (file[-len(file_ext):] == file_ext) and ((expression is None) or (re.match(expression, file))):
            
            # Randomly create signal plots if requested
            if (p is None) or (random.random() < p):
                
                # Read file
                data = pd.read_csv(filedirs[file])
                
                # If no columns selected, apply filter to all columns except time
                if cols is None:
                    cols = list(data.columns)
                    if 'Time' in cols:
                        cols.remove('Time')
                
                # Create plot
                fig, axs = plt.subplots(1, len(cols), figsize=(15*len(cols),15))
                
                # Plot each column
                for i in range(len(cols)):
                    col = cols[i]
                    psd = EMG2PSD(data[col], sr=sampling_rate)
                    axs[i].plot(psd['Frequency'], psd['Power'])
                    axs[i].set_ylabel('Power magnitude')
                    axs[i].set_xlabel('Frequency')
                    axs[i].set_title(col)
                
                # Set title and save figure
                fig.suptitle(file + ' Power Spectrum Density')
                fig.savefig(out_path + file[:-len(file_ext)] + 'jpg')
    return

#
# =============================================================================
#

def PlotCompareSignals(in_path1, in_path2, out_path, sampling_rate, cols=None, expression=None, file_ext='csv'):
    """
    Generate plots of the PSDs comparing different processing stages.

    Parameters
    ----------
    in_path1 : str
        Filepath to a directory containing the first set of Signals for comparison.
    in_path2 : TYPE
        Filepath to a directory containing the second set of Signals for comparison.
    out_path : str
        Filepath to an output directory.
    sampling_rate : float
        Sampling rate of the Signals.
    cols : list, optional
        List of columns of the Signal to plot. The default is None, in which case every column except
        'time' is plotted.
    expression : str, optional
        A regular expression. If provided, will only generate plots for files whose names match the regular
        expression. The default is None.
    file_ext : str, optional
        File extension for files to read. Only reads files with this extension. The default is 'csv'.

    Returns
    -------
    None.

    """
    
    # Convert out path to absolute
    if not os.path.isabs(out_path):
        out_path = os.path.abspath(out_path) + '\\'
    
    # Get dictionary of file locations
    filedirs1 = ConvertMapFiles(in_path1, file_ext=file_ext, expression=expression)
    filedirs2 = ConvertMapFiles(in_path2, file_ext=file_ext, expression=expression)
    
    # Make plots
    for file in tqdm(filedirs1):
        if (file[-len(file_ext):] == file_ext) and ((expression is None) or (re.match(expression, file))):
            
            # Read file
            data1 = pd.read_csv(filedirs1[file])
            data2 = pd.read_csv(filedirs2[file])
            
            # If no columns selected, apply filter to all columns except time
            if cols is None:
                cols = list(data1.columns)
                if 'Time' in cols:
                    cols.remove('Time')
            
            # Create plot
            fig, axs = plt.subplots(2, len(cols), figsize=(15*len(cols),30))
            
            # Plot each column
            for i in range(len(cols)):
                col = cols[i]
                
                psd1 = EMG2PSD(data1[col], sr=sampling_rate)
                axs[0,i].plot(psd1['Frequency'], psd1['Power'])
                axs[0,i].set_ylabel('Power magnitude')
                axs[0,i].set_title(col)
                
                psd2 = EMG2PSD(data2[col], sr=sampling_rate)
                axs[1,i].plot(psd2['Frequency'], psd2['Power'])
                axs[1,i].set_ylabel('Power magnitude')
                axs[1,i].set_xlabel('Frequency')
            
            # Set title and save figure
            fig.suptitle(file + ' Power Spectrum Density')
            fig.savefig(out_path + file[:-len(file_ext)] + 'jpg')
    
    return

#
# =============================================================================
#

# Creates a shiny app object that can be ran
def GenPlotDash(in_paths, sampling_rate, col, units, names, expression=None, file_ext='csv'):
    # Convert file paths to directories
    filedirs = []
    for path in in_paths:
        filedirs.append(ConvertMapFiles(path))
        
    # Convert file directories to data frame
    df = MapFilesFuse(filedirs, names)
    
    # Set style
    plt.style.use('fivethirtyeight')
    
    # Get colours
    colours = plt.rcParams['axes.prop_cycle'].by_key()['color']
    
    # Create shiny dashboard
    
    # =============
    # UI definition
    # =============
    app_ui = ui.page_fluid(
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.input_select('sig_type', 'Signal Displayed:', choices=['All']+names),
                ui.input_select('file_type', 'File:', choices=df['File'])
            ),
            ui.panel_main(
                ui.output_plot('plt_signal'),
            ),
        ),
    )
    
    legnames = names.copy()
    legnames.reverse()
    
    # =================
    # Server definition
    # =================
    def server(input, output, session):
        @render.plot
        def plt_signal():
            filename = input.file_type()
            column = input.sig_type()
            
            # Plot data
            fig, ax = plt.subplots()
            if column == 'All':
                # Read/plot each file
                for file_loc in reversed(list(df.loc[filename])[1:]):
                    sigDF = pd.read_csv(file_loc)
                    ax.plot(sigDF['Time'], sigDF[col], alpha=0.5)
                # Set legend for multiple plots
                ax.legend(legnames)
            else:
                # Read/plot single file
                file_location = df.loc[filename][column]
                sigDF = pd.read_csv(file_location)
                # Get colour data
                i = (names.index(column) + 1) % len(colours)
                # Plot file
                ax.plot(sigDF['Time'], sigDF[col], color=colours[len(names) - i], alpha=0.5)
                
            
            ax.set_ylabel('Voltage (mV)')
            ax.set_xlabel('Time (s)')
            ax.set_title(column + ' filter: ' + filename)
            
            return fig
    
    app = App(app_ui, server)
    webbrowser.open('http://127.0.0.1:8000')
    app.run()
    return