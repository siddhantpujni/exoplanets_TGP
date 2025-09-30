"""
Photometry Module
=================

Functions for aperture photometry and light curve analysis.
"""

import numpy as np
from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from photutils.detection import DAOStarFinder
from photutils.aperture import CircularAperture, aperture_photometry
from photutils.background import Background2D, MedianBackground
import pandas as pd


def find_sources(data, fwhm=5.0, threshold=5.0):
    """
    Detect sources in an image using DAOStarFinder.
    
    Parameters
    ----------
    data : numpy.ndarray
        2D image data
    fwhm : float
        Full-width half-maximum of stars in pixels
    threshold : float
        Detection threshold in units of background sigma
        
    Returns
    -------
    sources : astropy.table.Table
        Table of detected sources with positions and properties
    """
    # Estimate background
    mean, median, std = sigma_clipped_stats(data, sigma=3.0)
    
    # Find sources
    daofind = DAOStarFinder(fwhm=fwhm, threshold=threshold*std)
    sources = daofind(data - median)
    
    return sources


def measure_aperture_photometry(data, positions, aperture_radius=10, 
                                annulus_inner=15, annulus_outer=20):
    """
    Perform aperture photometry on sources.
    
    Parameters
    ----------
    data : numpy.ndarray
        2D image data
    positions : array-like
        Array of (x, y) positions
    aperture_radius : float
        Radius of photometry aperture in pixels
    annulus_inner : float
        Inner radius of background annulus
    annulus_outer : float
        Outer radius of background annulus
        
    Returns
    -------
    phot_table : astropy.table.Table
        Photometry results including flux, magnitude, and background
    """
    from photutils.aperture import CircularAnnulus
    
    # Create apertures
    apertures = CircularAperture(positions, r=aperture_radius)
    annulus = CircularAnnulus(positions, r_in=annulus_inner, r_out=annulus_outer)
    
    # Perform photometry
    phot_table = aperture_photometry(data, apertures)
    bkg_phot = aperture_photometry(data, annulus)
    
    # Calculate background per pixel
    annulus_area = annulus.area
    aperture_area = apertures.area
    
    bkg_mean = bkg_phot['aperture_sum'] / annulus_area
    bkg_sum = bkg_mean * aperture_area
    
    # Subtract background
    final_sum = phot_table['aperture_sum'] - bkg_sum
    phot_table['background'] = bkg_mean
    phot_table['aper_bkg'] = bkg_sum
    phot_table['aper_sum_bkgsub'] = final_sum
    
    # Calculate instrumental magnitude
    phot_table['mag_inst'] = -2.5 * np.log10(final_sum)
    
    return phot_table


def extract_light_curve(file_list, target_position, comparison_positions=None,
                       aperture_radius=10):
    """
    Extract a differential light curve from a series of images.
    
    Parameters
    ----------
    file_list : list of str
        List of FITS file paths
    target_position : tuple
        (x, y) position of target star
    comparison_positions : list of tuples, optional
        List of (x, y) positions of comparison stars
    aperture_radius : float
        Aperture radius in pixels
        
    Returns
    -------
    lightcurve : pandas.DataFrame
        Light curve data with times and relative fluxes
    """
    times = []
    target_flux = []
    comp_flux = []
    
    for filepath in file_list:
        data, header = fits.getdata(filepath, header=True)
        
        # Get observation time from header
        if 'JD' in header:
            time = header['JD']
        elif 'MJD' in header:
            time = header['MJD']
        elif 'DATE-OBS' in header:
            from astropy.time import Time
            time = Time(header['DATE-OBS']).jd
        else:
            time = 0.0
        
        # Measure target
        phot = measure_aperture_photometry(data, [target_position], 
                                          aperture_radius=aperture_radius)
        target_f = phot['aper_sum_bkgsub'][0]
        
        # Measure comparison stars if provided
        if comparison_positions:
            comp_phot = measure_aperture_photometry(data, comparison_positions,
                                                   aperture_radius=aperture_radius)
            comp_f = np.sum(comp_phot['aper_sum_bkgsub'])
        else:
            comp_f = 1.0
        
        times.append(time)
        target_flux.append(target_f)
        comp_flux.append(comp_f)
    
    # Create differential light curve
    times = np.array(times)
    target_flux = np.array(target_flux)
    comp_flux = np.array(comp_flux)
    
    relative_flux = target_flux / comp_flux
    # Normalize to median
    relative_flux = relative_flux / np.median(relative_flux)
    
    lightcurve = pd.DataFrame({
        'time': times,
        'target_flux': target_flux,
        'comparison_flux': comp_flux,
        'relative_flux': relative_flux
    })
    
    return lightcurve


def calculate_color_index(flux_filter1, flux_filter2, zeropoint1=0, zeropoint2=0):
    """
    Calculate color index from two filter measurements.
    
    Parameters
    ----------
    flux_filter1 : float or array
        Flux in first filter (e.g., B)
    flux_filter2 : float or array
        Flux in second filter (e.g., V)
    zeropoint1 : float
        Zero point for filter 1
    zeropoint2 : float
        Zero point for filter 2
        
    Returns
    -------
    color : float or array
        Color index (e.g., B-V)
    """
    mag1 = -2.5 * np.log10(flux_filter1) + zeropoint1
    mag2 = -2.5 * np.log10(flux_filter2) + zeropoint2
    
    color = mag1 - mag2
    
    return color
