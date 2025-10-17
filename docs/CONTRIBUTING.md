# Contributing Guide

Thank you for contributing to the Exoplanet Transit Analysis project! This guide will help you collaborate effectively with the team.

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/siddhantpujni/exoplanets_TGP.git
   cd exoplanets_TGP
   ```

2. **Set up your environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Create a branch for your work**
   ```bash
   git checkout -b analysis/your-target-name
   ```

## Workflow

### For Data Analysis

1. **Organize your data** in the appropriate directories
2. **Run notebooks** and document your analysis
3. **Save outputs** (CSV files, plots) to `data/`
4. **Clear notebook outputs** before committing
5. **Commit your changes** with descriptive messages
6. **Push and create a pull request**

### For Code Changes

1. **Write or modify** functions in `src/`
2. **Test your changes** to ensure they work
3. **Update documentation** if needed
4. **Commit with clear messages** describing what changed
5. **Push and create a pull request**

## Best Practices

### Git Workflow

```bash
# Start new work
git checkout main
git pull origin main
git checkout -b feature/my-analysis

# Make changes
# ... edit files ...

# Commit changes
git add notebooks/my_analysis.ipynb
git commit -m "Add transit analysis for WASP-10"

# Push to remote
git push origin feature/my-analysis

# Create pull request on GitHub
```

### Jupyter Notebooks

**Before committing notebooks:**

```bash
# Clear all outputs (prevents merge conflicts)
jupyter nbconvert --clear-output --inplace notebooks/*.ipynb

# Or clear from Jupyter UI: Cell > All Output > Clear
```

**Why?** Notebook outputs contain binary data that causes merge conflicts and increases repo size.

**Commit only:**
- Notebook structure and code cells
- Markdown documentation
- Not: cell outputs, plots, or execution counts

**Share results via:**
- Exported plots (PNG/PDF) in `data/`
- Data tables (CSV) in `data/`
- Summary in pull request description

### Code Style

Follow these conventions for consistency:

**Python:**
- Use 4 spaces for indentation
- Follow PEP 8 style guide
- Add docstrings to functions
- Use descriptive variable names
- Comment complex logic

**Example:**
```python
def calculate_transit_depth(flux_in_transit, flux_out_transit):
    """
    Calculate the transit depth from flux measurements.
    
    Parameters
    ----------
    flux_in_transit : float
        Average flux during transit
    flux_out_transit : float
        Average flux outside transit
        
    Returns
    -------
    depth : float
        Transit depth as a fraction
    """
    depth = (flux_out_transit - flux_in_transit) / flux_out_transit
    return depth
```

### File Organization

```
exoplanets_TGP/
├── data/               # Data and results (CSV, plots)
│   ├── raw/           # Original FITS (not in git)
│   ├── reduced/       # Processed FITS (not in git)
│   ├── calibration/   # Calibration frames (not in git)
│   └── *.csv, *.png   # Analysis results (in git)
├── notebooks/         # Jupyter notebooks
├── src/               # Python modules
├── docs/              # Documentation
└── tests/             # Tests (if any)
```

### Commit Messages

Write clear, descriptive commit messages:

**Good:**
```
Add light curve extraction for HAT-P-7
Calculate B-V colors for standard stars
Fix aperture photometry background subtraction
Update README with installation instructions
```

**Not so good:**
```
Update
Fix bug
Changes
asdf
```

**Format:**
```
Short summary (50 chars or less)

More detailed explanation if needed. Explain what
changed and why, not how (code shows how).

- Bullet points are fine
- Reference issues: Fixes #123
```

### Pull Requests

When creating a pull request:

1. **Title**: Clear description of changes
2. **Description**: 
   - What did you do?
   - What results did you find?
   - Any figures or tables to highlight?
   - Any issues encountered?

**Example PR description:**
```markdown
## Transit Analysis of HAT-P-7

### Changes
- Added notebook for HAT-P-7 transit analysis
- Extracted differential light curve
- Detected transit with depth ~2.1%

### Results
- Transit duration: 3.2 hours
- Ingress/egress: ~20 minutes each
- Good agreement with literature

### Figures
![Light curve](data/HAT-P-7_lightcurve.png)

### Next Steps
- Fit transit model for precise parameters
- Check for timing variations
```

## Collaboration Guidelines

### Communication

- **GitHub Issues**: For bugs, questions, and feature requests
- **Pull Request Reviews**: For discussing analysis and code
- **Project Board**: For tracking tasks and progress

### Data Sharing

**DO commit:**
- Notebooks (with outputs cleared)
- Analysis results (CSV, plots)
- Documentation
- Code changes

**DON'T commit:**
- Large FITS files
- Personal notes or temporary files
- Binary data (except plots)
- Local configuration (`config.py`)

**For large data:**
- Share via Google Drive, Dropbox, or institutional storage
- Document location in `data/data_sources.txt`
- Create metadata files (CSV) describing the data

### Code Review

When reviewing pull requests:

1. **Check the science**: Do results make sense?
2. **Verify code**: Does it run without errors?
3. **Review documentation**: Are changes explained?
4. **Test locally**: Pull branch and run notebooks
5. **Provide feedback**: Constructive comments

**Example review comments:**
- "Nice work! The light curve looks clean."
- "Could you add a comment explaining the sigma clipping?"
- "Have you tried a larger aperture? Might improve S/N."
- "The transit depth seems shallow, did you check saturation?"

## Adding New Features

### New Analysis Functions

1. Add to appropriate module in `src/`
2. Include docstring with parameters and returns
3. Add example usage in docstring
4. Test function works correctly
5. Update module `__init__.py` if needed

### New Notebooks

1. Copy structure from existing notebooks
2. Use descriptive title and sections
3. Add markdown explanations
4. Include example outputs (can be cleared later)
5. Save as `.ipynb` in `notebooks/`

### New Documentation

1. Add markdown file to `docs/`
2. Link from README or other docs
3. Use clear headings and examples
4. Include code snippets where helpful

## Getting Help

- **Setup issues**: See `docs/setup.md`
- **Analysis questions**: Ask in GitHub Issues
- **Code problems**: Create Issue with error message
- **Collaboration**: Discuss in pull requests

## Questions?

Open an issue on GitHub with the `question` label, and the team will help!

## License

By contributing, you agree that your contributions will be licensed under the same terms as the project.
