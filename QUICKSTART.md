# Quick Start Guide

Get up and running with exoplanet data analysis in minutes!

## 1. Install Dependencies (5 minutes)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

## 2. Organize Your Data (2 minutes)

Place your FITS files in these directories:

```bash
data/
├── raw/              # Your telescope observations
├── calibration/      # Bias, darks, and flats
└── reduced/          # Will be created automatically
```

Example files:
- `data/raw/20240315_HAT-P-7_V_120s_001.fits`
- `data/calibration/bias_20240315_001.fits`
- `data/calibration/flat_20240315_V_001.fits`

## 3. Start Jupyter (1 minute)

```bash
jupyter notebook
```

Your browser will open at `http://localhost:8888`

## 4. Run Analysis (30 minutes)

Open and run notebooks in order:

### Step 1: Data Reduction
**Notebook:** `01_data_reduction.ipynb`

Creates master calibration frames and processes your data:
- Master bias from bias frames
- Master flat from flat frames  
- Applies corrections to science images
- Outputs to `data/reduced/`

**Time:** ~10 minutes

### Step 2: Light Curve Analysis
**Notebook:** `02_light_curve_analysis.ipynb`

Extracts photometry and creates light curves:
- Detects stars in your images
- Performs aperture photometry
- Creates differential light curve
- Saves to `data/lightcurve.csv`

**Time:** ~15 minutes

### Step 3: Standard Star Calibration
**Notebook:** `03_standard_stars.ipynb`

Calibrates your photometry using standard stars:
- Measures standard star magnitudes
- Calculates zero points
- Determines color transformations
- Saves calibration to CSV

**Time:** ~10 minutes

## 5. View Results

Your analysis outputs:

- **Figures**: PNG/PDF plots for inspection
- **Data**: CSV files with photometry and light curves
- **Calibration**: Photometric zero points and transformations

Example outputs in `data/`:
- `lightcurve.csv` - Differential photometry
- `lightcurve.png` - Light curve plot
- `photometric_calibration.csv` - Zero points
- `color_magnitude_diagram.png` - CMD plot

## Common Workflows

### Quick Transit Analysis

```python
# In Jupyter notebook
import sys
sys.path.append('..')
from src.photometry import extract_light_curve

# Extract light curve
lc = extract_light_curve(
    file_list=['data/reduced/frame001.fits', ...],
    target_position=(512, 512),
    comparison_positions=[(600, 500), (450, 600)]
)

# Plot
import matplotlib.pyplot as plt
plt.plot(lc['time'], lc['relative_flux'], 'o')
plt.xlabel('Time')
plt.ylabel('Relative Flux')
plt.show()
```

### Batch Process All Data

```python
from src.data_reduction import batch_reduce, create_master_bias, create_master_flat
from src.utils import list_fits_files

# Create master calibrations
bias_files = list_fits_files('data/calibration', 'bias*.fits')
master_bias = create_master_bias(bias_files)

flat_files = list_fits_files('data/calibration', 'flat*.fits')
master_flat = create_master_flat(flat_files, master_bias)

# Reduce all science frames
science_files = list_fits_files('data/raw')
batch_reduce(science_files, master_bias, master_flat, 'data/reduced')
```

## Troubleshooting

### No FITS files found?

Check your paths:
```python
from pathlib import Path
print(list(Path('data/raw').glob('*.fits')))
```

### Module import errors?

Ensure you're in the right directory and virtual environment is activated:
```bash
pwd  # Should show: .../exoplanets_TGP
which python  # Should show venv path
```

### Notebooks won't run?

1. Check kernel is running (top right in Jupyter)
2. Restart kernel: Kernel > Restart
3. Run cells in order from top

## Next Steps

1. **Read full documentation**: See `docs/setup.md`
2. **Customize analysis**: Modify notebook parameters for your data
3. **Export for publication**: See `docs/overleaf.md`
4. **Collaborate**: Commit results and share with team

## Example Dataset Structure

Here's what your project looks like with data:

```
exoplanets_TGP/
├── data/
│   ├── raw/
│   │   ├── 20240315_HAT-P-7_V_120s_001.fits
│   │   ├── 20240315_HAT-P-7_V_120s_002.fits
│   │   └── ...
│   ├── calibration/
│   │   ├── bias_20240315_001.fits
│   │   ├── flat_20240315_V_001.fits
│   │   └── master_bias.fits (created)
│   ├── reduced/
│   │   ├── reduced_20240315_HAT-P-7_V_120s_001.fits (created)
│   │   └── ...
│   ├── lightcurve.csv (created)
│   └── lightcurve.png (created)
└── notebooks/ (your analysis)
```

## Getting Help

- **Setup issues**: Read `docs/setup.md`
- **Overleaf integration**: Read `docs/overleaf.md`  
- **Code questions**: Check function docstrings in `src/`
- **Team questions**: Open a GitHub issue

## Tips for Success

1. **Start small**: Process a few files first to test workflow
2. **Save often**: Jupyter auto-saves, but use Ctrl+S frequently
3. **Document**: Add markdown cells to notebooks explaining your choices
4. **Version control**: Commit results regularly to GitHub
5. **Collaborate**: Clear notebook outputs before committing

Happy analyzing! 🔭✨
