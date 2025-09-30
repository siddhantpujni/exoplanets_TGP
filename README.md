# Exoplanet Transit Analysis - TGP

A collaborative astronomy project for exoplanet transit detection and analysis using photometric data from telescope observations.

## Project Overview

This project facilitates collaborative analysis of large astronomical datasets stored in FITS format. It includes tools and workflows for:

- **Data Reduction**: Flatfielding, bias correction, and calibration
- **Light Curve Analysis**: Transit detection and characterization
- **Photometry**: Color analysis for standard stars
- **Collaborative Documentation**: Integration with Overleaf for LaTeX manuscripts

## Repository Structure

```
exoplanets_TGP/
├── data/
│   ├── raw/              # Raw FITS files from telescope (not tracked in git)
│   ├── reduced/          # Processed data (not tracked in git)
│   ├── calibration/      # Bias, dark, and flat frames (not tracked in git)
│   └── README.md         # Data organization guidelines
├── notebooks/
│   ├── 01_data_reduction.ipynb       # Flatfielding and bias correction
│   ├── 02_light_curve_analysis.ipynb # Transit analysis
│   └── 03_standard_stars.ipynb       # Color photometry
├── src/
│   ├── __init__.py
│   ├── data_reduction.py  # Data processing functions
│   ├── photometry.py      # Aperture photometry tools
│   └── utils.py           # Utility functions
├── docs/
│   ├── setup.md           # Setup instructions
│   └── overleaf.md        # Overleaf integration guide
├── requirements.txt       # Python dependencies
└── README.md
```

## Installation

### Prerequisites

- Python 3.8 or higher
- Git
- Jupyter Notebook/Lab

### Setup

1. Clone the repository:
```bash
git clone https://github.com/siddhantpujni/exoplanets_TGP.git
cd exoplanets_TGP
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Launch Jupyter:
```bash
jupyter notebook
```

## Data Management

### Local Data Storage

FITS files are **not tracked in git** due to their large size. Store your data in:
- `data/raw/`: Raw telescope observations
- `data/calibration/`: Bias, dark, and flat frames
- `data/reduced/`: Processed science frames

See `data/README.md` for detailed organization guidelines.

### Sharing Results

- Share reduced data products (CSV, plots) via git
- Use notebooks to document analysis steps
- Export key findings to Overleaf for manuscript preparation

## Workflow

### 1. Data Reduction
Use `notebooks/01_data_reduction.ipynb` to:
- Apply bias correction
- Perform flatfielding
- Create master calibration frames

### 2. Light Curve Analysis
Use `notebooks/02_light_curve_analysis.ipynb` to:
- Perform aperture photometry
- Create light curves
- Detect and characterize transits

### 3. Standard Star Analysis
Use `notebooks/03_standard_stars.ipynb` to:
- Measure standard star magnitudes
- Calculate color indices
- Perform photometric calibration

## Overleaf Integration

See `docs/overleaf.md` for instructions on:
- Connecting your Overleaf project with GitHub
- Syncing figures and tables from analysis
- Collaborative manuscript writing

## Contributing

For collaborative work:
1. Create a new branch for your analysis
2. Document your work in Jupyter notebooks
3. Commit notebooks with outputs cleared (use `jupyter nbconvert --clear-output`)
4. Create a pull request for team review

## Key Dependencies

- **astropy**: FITS file handling and astronomical calculations
- **numpy**: Numerical computations
- **matplotlib**: Plotting and visualization
- **photutils**: Aperture photometry
- **scipy**: Scientific computing
- **pandas**: Data analysis and manipulation

## Resources

- [Astropy Documentation](https://docs.astropy.org/)
- [Photutils Documentation](https://photutils.readthedocs.io/)
- [FITS Format Specification](https://fits.gsfc.nasa.gov/)

## License

This project is for academic research purposes.

## Contact

For questions or collaboration inquiries, please open an issue on GitHub.