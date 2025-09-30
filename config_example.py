"""
Configuration file for exoplanet analysis
==========================================

Copy this file to 'config.py' and customize for your observations.
The config.py file is gitignored so your settings stay local.
"""

# Data Directories
RAW_DATA_DIR = 'data/raw'
CALIBRATION_DIR = 'data/calibration'
REDUCED_DIR = 'data/reduced'

# Calibration Settings
BIAS_PATTERN = 'bias*.fits'
DARK_PATTERN = 'dark*.fits'
FLAT_PATTERN = 'flat*.fits'

# Photometry Settings
APERTURE_RADIUS = 10  # pixels
ANNULUS_INNER = 15    # pixels
ANNULUS_OUTER = 20    # pixels
FWHM = 5.0           # Full-width half-maximum in pixels
DETECTION_THRESHOLD = 5.0  # Detection threshold in sigma

# Target Information
TARGET_NAME = 'HAT-P-7'
TARGET_POSITION = (512, 512)  # (x, y) pixel coordinates

# Comparison Stars
# List of (x, y) positions for comparison stars
COMPARISON_POSITIONS = [
    (600, 500),
    (450, 600),
    (700, 400)
]

# Filters
FILTERS = ['B', 'V', 'R']

# Standard Stars (if using photometric calibration)
STANDARD_STARS = {
    'SA98-193': {
        'ra': 21.0,
        'dec': 0.0,
        'V_mag': 13.150,
        'B_mag': 13.850,
        'R_mag': 12.700,
        'position': (512.5, 512.5)
    },
    'SA98-194': {
        'ra': 21.1,
        'dec': 0.1,
        'V_mag': 13.560,
        'B_mag': 14.320,
        'R_mag': 13.050,
        'position': (612.3, 612.7)
    }
}

# Plot Settings
FIGURE_DPI = 150
FIGURE_FORMAT = 'png'  # 'png' or 'pdf'
PLOT_STYLE = 'seaborn-v0_8'  # matplotlib style

# Output Settings
SAVE_REDUCED_FRAMES = True
SAVE_LIGHT_CURVE = True
LIGHT_CURVE_FILENAME = 'data/lightcurve.csv'
CALIBRATION_FILENAME = 'data/photometric_calibration.csv'

# Analysis Parameters
TIME_UNIT = 'JD'  # 'JD', 'MJD', or 'BJD'
NORMALIZE_LIGHT_CURVE = True

# Advanced Settings
USE_PARALLEL_PROCESSING = False  # Set to True if you have many files
NUM_PROCESSES = 4  # Number of parallel processes

# File Patterns
SCIENCE_FILE_PATTERN = '*.fits'
DATE_FORMAT = '%Y%m%d'

# Notes
# =====
# - Adjust APERTURE_RADIUS based on your seeing conditions
# - FWHM should match your typical star profile
# - Update TARGET_POSITION after visual inspection
# - Add more comparison stars for better differential photometry
# - Set FIGURE_FORMAT to 'pdf' for publication-quality figures
