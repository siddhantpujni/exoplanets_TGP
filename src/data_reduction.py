"""
Data Reduction Module
=====================

Functions for basic CCD data reduction including bias correction,
dark subtraction, and flatfielding.
"""

import numpy as np
from astropy.io import fits
from pathlib import Path
import warnings


def load_fits(filepath):
    """
    Load a FITS file and return the data and header.
    
    Parameters
    ----------
    filepath : str or Path
        Path to the FITS file
        
    Returns
    -------
    data : numpy.ndarray
        Image data
    header : astropy.io.fits.Header
        FITS header
    """
    with fits.open(filepath) as hdul:
        data = hdul[0].data.astype(float)
        header = hdul[0].header
    return data, header


def create_master_bias(bias_files, output_path=None):
    """
    Create a master bias frame by median combining individual bias frames.
    
    Parameters
    ----------
    bias_files : list of str
        List of paths to bias FITS files
    output_path : str, optional
        Path to save the master bias. If None, not saved.
        
    Returns
    -------
    master_bias : numpy.ndarray
        Master bias frame
    """
    if len(bias_files) == 0:
        raise ValueError("No bias files provided")
    
    bias_data = []
    for bias_file in bias_files:
        data, _ = load_fits(bias_file)
        bias_data.append(data)
    
    # Median combine
    master_bias = np.median(bias_data, axis=0)
    
    if output_path:
        header = fits.Header()
        header['HISTORY'] = f'Master bias from {len(bias_files)} frames'
        fits.writeto(output_path, master_bias, header, overwrite=True)
    
    return master_bias


def create_master_flat(flat_files, master_bias=None, output_path=None):
    """
    Create a master flat frame by median combining flat frames.
    
    Parameters
    ----------
    flat_files : list of str
        List of paths to flat field FITS files
    master_bias : numpy.ndarray, optional
        Master bias to subtract from flats
    output_path : str, optional
        Path to save the master flat
        
    Returns
    -------
    master_flat : numpy.ndarray
        Normalized master flat frame
    """
    if len(flat_files) == 0:
        raise ValueError("No flat files provided")
    
    flat_data = []
    for flat_file in flat_files:
        data, _ = load_fits(flat_file)
        
        # Subtract bias if provided
        if master_bias is not None:
            data = data - master_bias
        
        # Normalize each flat by its median
        data = data / np.median(data)
        flat_data.append(data)
    
    # Median combine
    master_flat = np.median(flat_data, axis=0)
    
    # Normalize to median of 1
    master_flat = master_flat / np.median(master_flat)
    
    if output_path:
        header = fits.Header()
        header['HISTORY'] = f'Master flat from {len(flat_files)} frames'
        fits.writeto(output_path, master_flat, header, overwrite=True)
    
    return master_flat


def reduce_science_frame(science_file, master_bias=None, master_flat=None, 
                        output_path=None):
    """
    Apply bias subtraction and flat fielding to a science frame.
    
    Parameters
    ----------
    science_file : str
        Path to science FITS file
    master_bias : numpy.ndarray, optional
        Master bias frame
    master_flat : numpy.ndarray, optional
        Master flat frame
    output_path : str, optional
        Path to save reduced frame
        
    Returns
    -------
    reduced : numpy.ndarray
        Reduced science frame
    header : astropy.io.fits.Header
        Original header with reduction history
    """
    data, header = load_fits(science_file)
    
    # Bias correction
    if master_bias is not None:
        data = data - master_bias
        header['HISTORY'] = 'Bias subtracted'
    
    # Flat fielding
    if master_flat is not None:
        data = data / master_flat
        header['HISTORY'] = 'Flat fielded'
    
    if output_path:
        fits.writeto(output_path, data, header, overwrite=True)
    
    return data, header


def batch_reduce(science_files, master_bias=None, master_flat=None, 
                output_dir=None):
    """
    Batch reduce multiple science frames.
    
    Parameters
    ----------
    science_files : list of str
        List of science file paths
    master_bias : numpy.ndarray, optional
        Master bias frame
    master_flat : numpy.ndarray, optional
        Master flat frame
    output_dir : str, optional
        Directory to save reduced frames
        
    Returns
    -------
    reduced_files : list of str
        Paths to reduced files (if output_dir specified)
    """
    reduced_files = []
    
    for sci_file in science_files:
        if output_dir:
            filename = Path(sci_file).name
            output_path = Path(output_dir) / f"reduced_{filename}"
        else:
            output_path = None
        
        reduce_science_frame(sci_file, master_bias, master_flat, output_path)
        
        if output_path:
            reduced_files.append(str(output_path))
    
    return reduced_files
