# Setup Guide

## Installation

### 1. System Requirements

- **Python**: 3.8 or higher
- **Git**: For version control
- **Storage**: Sufficient space for FITS files (typically 1-10 GB per observing run)

### 2. Clone Repository

```bash
git clone https://github.com/siddhantpujni/exoplanets_TGP.git
cd exoplanets_TGP
```

### 3. Create Virtual Environment

**On Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install:
- **astropy**: FITS handling and astronomical utilities
- **photutils**: Source detection and photometry
- **ccdproc**: CCD data reduction
- **numpy, scipy**: Numerical computing
- **matplotlib, seaborn**: Visualization
- **pandas**: Data analysis
- **jupyter**: Interactive notebooks

### 5. Verify Installation

Test that key packages are installed:

```python
python -c "import astropy; import photutils; import ccdproc; print('All packages installed successfully!')"
```

## Data Setup

### 1. Organize Your FITS Files

Place your telescope data in the appropriate directories:

```
data/
├── raw/              # Original observations
├── calibration/      # Bias, darks, flats
└── reduced/          # Processed data (created automatically)
```

### 2. File Naming Convention

Use consistent naming for easy organization:

```
YYYYMMDD_TARGET_FILTER_EXPTIME_NNN.fits
```

Examples:
- `20240315_HAT-P-7_V_120s_001.fits`
- `20240315_HAT-P-7_V_120s_002.fits`

For calibration frames:
- Bias: `bias_YYYYMMDD_NNN.fits`
- Flat: `flat_YYYYMMDD_FILTER_NNN.fits`
- Dark: `dark_YYYYMMDD_EXPTIMEs_NNN.fits`

### 3. Create Observation Log

Document your observations in a CSV file:

```csv
filename,object,filter,exptime,airmass,date-obs,notes
20240315_HAT-P-7_V_120s_001.fits,HAT-P-7,V,120,1.15,2024-03-15T22:30:00,Good seeing
```

## Jupyter Notebook Setup

### 1. Launch Jupyter

```bash
jupyter notebook
```

This will open Jupyter in your web browser.

### 2. Navigate to Notebooks

Browse to the `notebooks/` directory and open:
1. `01_data_reduction.ipynb` - Start here
2. `02_light_curve_analysis.ipynb` - After data reduction
3. `03_standard_stars.ipynb` - For photometric calibration

### 3. Working with Notebooks

**Best Practices:**
- Run cells in order (top to bottom)
- Save frequently (Ctrl+S or Cmd+S)
- Clear outputs before committing: `Cell > All Output > Clear`
- Restart kernel if needed: `Kernel > Restart`

## Troubleshooting

### Import Errors

If you get `ModuleNotFoundError`:
```bash
pip install <missing-package>
```

### FITS File Not Found

Check file paths and ensure FITS files are in correct directories:
```python
from pathlib import Path
print(list(Path('data/raw').glob('*.fits')))
```

### Memory Issues

For large datasets:
- Process files one at a time
- Use `del` to free memory
- Close FITS files after reading

### Slow Performance

- Reduce number of images processed
- Use smaller aperture search regions
- Consider using `dask` for parallel processing

## Collaborative Workflow

### 1. Working with Git

**Create a new branch for your analysis:**
```bash
git checkout -b feature/my-analysis
```

**Commit your changes:**
```bash
git add notebooks/
git commit -m "Add transit analysis for HAT-P-7"
```

**Push to remote:**
```bash
git push origin feature/my-analysis
```

### 2. Notebook Collaboration

**Before committing notebooks:**
- Clear all outputs: `jupyter nbconvert --clear-output --inplace notebook.ipynb`
- This reduces conflicts and keeps repo size small

**When reviewing team members' work:**
- Pull their branch
- Re-run notebook cells to verify results
- Check generated figures and data files

### 3. Sharing Large Data

FITS files are NOT tracked in git. Share data via:
- **Cloud storage**: Google Drive, Dropbox
- **Institutional servers**: Your university's research storage
- **Zenodo**: For publishing final datasets

Document data location in `data/data_sources.txt`

## Additional Resources

### Python Astronomy

- [Astropy Documentation](https://docs.astropy.org/)
- [Photutils Documentation](https://photutils.readthedocs.io/)
- [CCDProc Documentation](https://ccdproc.readthedocs.io/)

### Photometry

- [Aperture Photometry Tutorial](https://photutils.readthedocs.io/en/stable/aperture.html)
- [Source Detection](https://photutils.readthedocs.io/en/stable/detection.html)

### Jupyter

- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
- [JupyterLab](https://jupyterlab.readthedocs.io/)

## Getting Help

1. **Check documentation** in `docs/` directory
2. **Read notebook comments** for guidance
3. **Open an issue** on GitHub for bugs or questions
4. **Ask team members** through your project communication channel
