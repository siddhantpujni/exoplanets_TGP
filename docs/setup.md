# Setup Guide

## Installation

### 2. Install Anaconda/Miniconda

**Download and install:**
- **Anaconda**: Full distribution with GUI (recommended for beginners)
  - Download from: https://www.anaconda.com/products/distribution
- **Miniconda**: Minimal installation (lighter weight)
  - Download from: https://docs.conda.io/en/latest/miniconda.html

**Verify installation:**
```bash
conda --version
```

### 3. Clone Repository

```bash
git clone https://github.com/siddhantpujni/exoplanets_TGP.git
cd exoplanets_TGP
```

### 4. Create Conda Environment

**Open Anaconda Prompt (Windows) or Terminal (Mac/Linux):**

```bash
# Navigate to project directory
cd path/to/exoplanets_TGP

# Create conda environment with Python 3.10 (recommended for astronomy)
conda create -n exoplanets_TGP python=3.10

# Activate environment
conda activate exoplanets_TGP
```
### 5. Install Astronomy Packages

**Install core packages from conda-forge (recommended for astronomy):**

```bash
# Install astronomy and scientific computing packages
conda install -c conda-forge astropy photutils ccdproc numpy scipy matplotlib pandas jupyter seaborn

# Install additional packages if needed
conda install -c conda-forge scikit-image scikit-learn
```

**Install any remaining packages with pip:**

```bash
pip install -r docs/requirements.txt
```

**Why conda-forge?**
- Pre-compiled binaries (faster installation)
- Better dependency resolution for scientific packages
- Astronomy-community maintained packages
- Handles complex C/Fortran dependencies automatically

### 6. Verify Installation

Test that key packages are installed:

```bash
python -c "import astropy; import photutils; import ccdproc; print('All packages installed successfully!')"
```

### 7. Environment Management

**Daily usage:**
```bash
# Activate environment
conda activate exoplanets_TGP

# Work on project...

# Deactivate when done
conda deactivate
```

**Check your environments:**
```bash
conda env list
```

**Remove environment (if needed):**
```bash
conda remove -n exoplanets_TGP --all
```

## Platform-Specific Instructions

### Windows Users

**Use Anaconda Prompt:**
- Search "Anaconda Prompt" in Start Menu
- Or use "Anaconda PowerShell Prompt" for PowerShell interface
- **Do NOT use regular Command Prompt or PowerShell**

**File paths use backslashes:**
```bash
cd c:\Users\YourName\Documents\exoplanets_TGP
```

### Mac/Linux Users

**Use Terminal:**
- Regular Terminal application works fine
- Conda should be available after installation

**File paths use forward slashes:**
```bash
cd /Users/YourName/Documents/exoplanets_TGP
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

**Make sure your conda environment is activated first:**

```bash
# Activate environment
conda activate exoplanets_TGP

# Launch Jupyter Notebook
jupyter notebook
```

This will open Jupyter in your web browser at `http://localhost:8888`

### 2. Navigate to Notebooks

Browse to the `notebooks/` directory and open:
1. `01_data_reduction.ipynb` - Start here for calibration
2. `02_light_curve_analysis.ipynb` - Photometry and transit detection
3. `03_standard_stars.ipynb` - Photometric calibration (optional)

### 3. Working with Notebooks

**Best Practices:**
- **Always activate conda environment first**
- Run cells in order (top to bottom)
- Save frequently (Ctrl+S or Cmd+S)
- Clear outputs before committing: `Cell > All Output > Clear`
- Restart kernel if needed: `Kernel > Restart`

**If kernel won't start:**
```bash
# Make sure Jupyter is installed in your environment
conda install -c conda-forge jupyter

# Or reinstall
conda install -c conda-forge jupyter --force-reinstall
```

## Troubleshooting

### Environment Issues

**"conda not found" error:**
- Restart terminal/Anaconda Prompt
- Verify Anaconda installation
- Check PATH environment variables

**Wrong Python version:**
```bash
# Check which Python you're using
which python    # Mac/Linux
where python    # Windows

# Should show path to conda environment
```

### Package Import Errors

**If you get `ModuleNotFoundError`:**

```bash
# First try conda-forge
conda install -c conda-forge <missing-package>

# If not available, use pip
pip install <missing-package>
```

**Common astronomy package fixes:**
```bash
# If astropy fails to import
conda install -c conda-forge astropy --force-reinstall

# If photutils has issues
conda install -c conda-forge photutils scipy --force-reinstall
```

### FITS File Issues

Check file paths and ensure FITS files are in correct directories:

```python
from pathlib import Path
print("Raw files:", list(Path('data/raw').glob('*.fits')))
print("Calibration files:", list(Path('data/calibration').glob('*.fits')))
```

### Memory Issues

For large datasets:
- Process files one at a time
- Use `del` to free memory after processing
- Close FITS files explicitly: `fits_file.close()`
- Consider using smaller data subsets for testing

### Performance Issues

**Slow installation:**
- Use conda instead of pip when possible
- Add `conda-forge` channel: `conda config --add channels conda-forge`

**Slow analysis:**
- Reduce number of images processed initially
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
git add notebooks/ src/ docs/
git commit -m "Add transit analysis for HAT-P-7"
```

**Push to remote:**
```bash
git push origin feature/my-analysis
```

### 2. Environment Sharing

**Export your environment:**
```bash
# Create environment file for team sharing
conda env export > environment.yml

# Others can recreate with:
conda env create -f environment.yml
```

**Cross-platform environment file:**
```bash
# Create platform-independent file
conda env export --no-builds > environment.yml
```

### 3. Notebook Collaboration

**Before committing notebooks:**
```bash
# Clear all outputs (reduces conflicts and file size)
jupyter nbconvert --clear-output --inplace notebooks/*.ipynb
```

**When reviewing team members' work:**
- Pull their branch
- Activate the same conda environment
- Re-run notebook cells to verify results
- Check generated figures and data files

### 4. Sharing Large Data

FITS files are NOT tracked in git. Share data via:
- **Cloud storage**: Google Drive, Dropbox, OneDrive
- **Institutional servers**: Your university's research storage
- **Zenodo**: For publishing final datasets
- **Google Colab**: For sharing analysis with data

Document data location in `data/data_sources.txt`

## Environment Best Practices

### 1. Keep Environments Separate
- One environment per project
- Don't install everything in `base` environment
- Use descriptive environment names

### 2. Environment Maintenance
```bash
# Update packages periodically
conda update --all

# Clean up unused packages
conda clean --all

# List installed packages
conda list
```

### 3. Backup Your Work
```bash
# Export environment specification
conda env export > environment.yml

# Back up your analysis notebooks regularly
```

## Additional Resources

### Conda Documentation
- [Conda User Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/)
- [Managing Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- [conda-forge](https://conda-forge.org/)

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
3. **Check conda environment**: `conda list` to verify packages
4. **Open an issue** on GitHub for bugs or questions
5. **Ask team members** through your project communication channel
6. **Astronomy Python forums**: [Astropy Discourse](https://community.openastronomy.org/)

## Quick Start Summary

```bash
# 1. Install Anaconda/Miniconda
# 2. Clone repository
git clone https://github.com/siddhantpujni/exoplanets_TGP.git
cd exoplanets_TGP

# 3. Create and activate environment
conda create -n exoplanets_TGP python=3.10
conda activate exoplanets_TGP

# 4. Install packages
conda install -c conda-forge astropy photutils ccdproc numpy scipy matplotlib pandas jupyter

# 5. Launch analysis
jupyter notebook
```