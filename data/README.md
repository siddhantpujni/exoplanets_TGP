# Data Organization Guidelines

## Directory Structure

### `raw/`
Store your original, unmodified FITS files from the telescope here.

**Recommended naming convention:**
```
YYYYMMDD_TARGET_FILTER_EXPTIME_NNN.fits
```

Example:
- `20240315_HAT-P-7_V_120s_001.fits`
- `20240315_HAT-P-7_V_120s_002.fits`

### `calibration/`
Store calibration frames here:

- **Bias frames**: `bias_YYYYMMDD_NNN.fits`
- **Dark frames**: `dark_YYYYMMDD_EXPTIMEs_NNN.fits`
- **Flat frames**: `flat_YYYYMMDD_FILTER_NNN.fits`

Example:
- `bias_20240315_001.fits`
- `dark_20240315_120s_001.fits`
- `flat_20240315_V_001.fits`

### `reduced/`
Store your processed science frames here after applying calibrations.

**Naming convention:**
```
reduced_YYYYMMDD_TARGET_FILTER_EXPTIME_NNN.fits
```

## Data Not Tracked in Git

**Important**: FITS files are NOT tracked in git due to their large size (typically several MB each). 

The `.gitignore` file excludes:
- `*.fits`, `*.fit`, `*.fts` files
- All contents of `data/raw/`, `data/reduced/`, and `data/calibration/`

## Sharing Data

For collaborative analysis:

1. **Store FITS locally**: Keep original data on your local machine or shared storage
2. **Share metadata**: Create CSV files with observation details:
   ```
   filename, object, filter, exptime, airmass, date-obs, ...
   ```
3. **Share results**: Commit extracted photometry tables, light curves (CSV), and plots (PNG/PDF)
4. **Document processing**: Use Jupyter notebooks to document your data reduction pipeline

## Cloud Storage Options

For team data sharing, consider:
- **Google Drive**: For smaller datasets
- **Dropbox**: For medium datasets
- **Institutional servers**: For large datasets
- **Zenodo**: For publishing final datasets with DOI

Add a `data_sources.txt` file documenting where team members can access the shared FITS files.

## Example Metadata File

Create `data/observation_log.csv`:
```csv
filename,object,filter,exptime,airmass,date-obs,notes
20240315_HAT-P-7_V_120s_001.fits,HAT-P-7,V,120,1.15,2024-03-15T22:30:00,Good seeing
20240315_HAT-P-7_V_120s_002.fits,HAT-P-7,V,120,1.16,2024-03-15T22:32:15,Good seeing
```

This allows team members to understand the observations without downloading all FITS files.
