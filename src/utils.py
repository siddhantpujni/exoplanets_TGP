"""
Utility Functions
=================

Helper functions for data handling and visualization.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from astropy.io import fits


def list_fits_files(directory, pattern="*.fits"):
    """
    List all FITS files in a directory.
    
    Parameters
    ----------
    directory : str
        Path to directory
    pattern : str
        File pattern to match
        
    Returns
    -------
    files : list
        Sorted list of file paths
    """
    path = Path(directory)
    files = sorted(path.glob(pattern))
    return [str(f) for f in files]


def plot_image(data, title="", vmin=None, vmax=None, cmap='gray', 
               show_colorbar=True, ax=None):
    """
    Display an astronomical image with proper scaling.
    
    Parameters
    ----------
    data : numpy.ndarray
        2D image data
    title : str
        Plot title
    vmin, vmax : float
        Display range
    cmap : str
        Colormap name
    show_colorbar : bool
        Whether to show colorbar
    ax : matplotlib.axes.Axes, optional
        Axes to plot on
        
    Returns
    -------
    ax : matplotlib.axes.Axes
        The axes object
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 8))
    
    # Auto scale if not provided
    if vmin is None or vmax is None:
        from astropy.stats import sigma_clipped_stats
        mean, median, std = sigma_clipped_stats(data, sigma=3.0)
        if vmin is None:
            vmin = median - 2*std
        if vmax is None:
            vmax = median + 5*std
    
    im = ax.imshow(data, origin='lower', cmap=cmap, vmin=vmin, vmax=vmax)
    ax.set_title(title)
    ax.set_xlabel('X (pixels)')
    ax.set_ylabel('Y (pixels)')
    
    if show_colorbar:
        plt.colorbar(im, ax=ax, label='Counts')
    
    return ax


def plot_light_curve(times, fluxes, errors=None, title="Light Curve", 
                     xlabel="Time", ylabel="Relative Flux"):
    """
    Plot a light curve.
    
    Parameters
    ----------
    times : array-like
        Time values
    fluxes : array-like
        Flux values
    errors : array-like, optional
        Flux uncertainties
    title : str
        Plot title
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
        
    Returns
    -------
    fig, ax : matplotlib figure and axes
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    if errors is not None:
        ax.errorbar(times, fluxes, yerr=errors, fmt='o', alpha=0.7, 
                   markersize=4, capsize=3)
    else:
        ax.plot(times, fluxes, 'o', alpha=0.7, markersize=4)
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig, ax


def get_fits_header_info(filepath, keywords=None):
    """
    Extract header information from a FITS file.
    
    Parameters
    ----------
    filepath : str
        Path to FITS file
    keywords : list of str, optional
        Specific keywords to extract. If None, returns all.
        
    Returns
    -------
    info : dict
        Dictionary of header information
    """
    with fits.open(filepath) as hdul:
        header = hdul[0].header
        
        if keywords is None:
            info = dict(header)
        else:
            info = {k: header.get(k, None) for k in keywords}
    
    return info


def create_observation_log(file_list, output_csv=None):
    """
    Create an observation log from FITS files.
    
    Parameters
    ----------
    file_list : list of str
        List of FITS file paths
    output_csv : str, optional
        Path to save CSV file
        
    Returns
    -------
    log : pandas.DataFrame
        Observation log
    """
    import pandas as pd
    
    records = []
    keywords = ['OBJECT', 'FILTER', 'EXPTIME', 'AIRMASS', 'DATE-OBS']
    
    for filepath in file_list:
        info = get_fits_header_info(filepath, keywords)
        info['filename'] = Path(filepath).name
        records.append(info)
    
    log = pd.DataFrame(records)
    
    if output_csv:
        log.to_csv(output_csv, index=False)
    
    return log


def estimate_background_level(data, method='median'):
    """
    Estimate the background level of an image.
    
    Parameters
    ----------
    data : numpy.ndarray
        2D image data
    method : str
        Method to use: 'median', 'mean', or 'sigma_clipped'
        
    Returns
    -------
    background : float
        Estimated background level
    """
    from astropy.stats import sigma_clipped_stats
    
    if method == 'median':
        background = np.median(data)
    elif method == 'mean':
        background = np.mean(data)
    elif method == 'sigma_clipped':
        mean, median, std = sigma_clipped_stats(data, sigma=3.0)
        background = median
    else:
        raise ValueError(f"Unknown method: {method}")
    
    return background
