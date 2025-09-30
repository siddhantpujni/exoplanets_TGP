# Overleaf Integration Guide

This guide explains how to integrate your data analysis with Overleaf for collaborative manuscript writing.

## Setup Options

### Option 1: Git Integration (Recommended)

Overleaf Professional allows direct Git synchronization with GitHub.

#### Requirements
- Overleaf Professional account (check if your institution provides it)
- GitHub repository access

#### Steps

1. **Create Overleaf Project**
   - Go to [Overleaf.com](https://www.overleaf.com)
   - Create a new project or use existing manuscript

2. **Link with GitHub**
   - In Overleaf project, go to Menu > GitHub
   - Click "Link to GitHub"
   - Authorize Overleaf to access your GitHub account
   - Select `siddhantpujni/exoplanets_TGP` repository

3. **Pull/Push Changes**
   - **From GitHub to Overleaf**: Menu > GitHub > Pull GitHub changes
   - **From Overleaf to GitHub**: Menu > GitHub > Push changes to GitHub

4. **Sync Workflow**
   ```
   Data Analysis (Jupyter) → Generate figures/tables → Commit to GitHub
   → Pull into Overleaf → Write manuscript → Push back to GitHub
   ```

### Option 2: Manual File Transfer

If you don't have Overleaf Professional:

1. **Export from Analysis**
   - Generate figures: `plt.savefig('figure1.pdf', dpi=300, bbox_inches='tight')`
   - Export tables: `df.to_latex('table1.tex', index=False)`

2. **Upload to Overleaf**
   - Manually upload PDFs and TeX files to Overleaf project
   - Keep files organized in subdirectories

3. **Version Control**
   - Maintain filenames with versions: `lightcurve_v2.pdf`
   - Document updates in manuscript comments

## File Organization

### In GitHub Repository

```
exoplanets_TGP/
├── manuscript/              # LaTeX files
│   ├── main.tex
│   ├── sections/
│   │   ├── introduction.tex
│   │   ├── observations.tex
│   │   ├── analysis.tex
│   │   └── conclusions.tex
│   ├── figures/            # Generated plots (PDF/PNG)
│   └── tables/             # Generated LaTeX tables
├── data/
│   ├── lightcurve.csv
│   └── photometric_calibration.csv
└── notebooks/              # Analysis notebooks
```

### In Overleaf Project

```
manuscript/
├── main.tex
├── sections/
├── figures/
├── tables/
├── bibliography.bib
└── journal_style.sty
```

## Exporting Results from Jupyter

### 1. High-Quality Figures

```python
import matplotlib.pyplot as plt

# Create your plot
fig, ax = plt.subplots(figsize=(8, 6))
# ... plotting code ...

# Save as PDF (vector graphics, preferred for publications)
plt.savefig('../manuscript/figures/lightcurve.pdf', 
            dpi=300, bbox_inches='tight', format='pdf')

# Or save as PNG (raster, if required)
plt.savefig('../manuscript/figures/lightcurve.png', 
            dpi=300, bbox_inches='tight')
```

### 2. LaTeX Tables

```python
import pandas as pd

# Your data
df = pd.DataFrame({
    'Star': ['HAT-P-7', 'WASP-10'],
    'V_mag': [10.50, 12.70],
    'Period (days)': [2.2047, 3.0928]
})

# Export to LaTeX
df.to_latex('../manuscript/tables/observations.tex',
           index=False,
           float_format='%.3f',
           caption='Observed Exoplanet Systems',
           label='tab:observations')
```

### 3. Include in LaTeX Document

In your `main.tex`:

```latex
\documentclass{article}
\usepackage{graphicx}
\usepackage{booktabs}

\begin{document}

\section{Results}

Figure \ref{fig:lightcurve} shows the differential light curve.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/lightcurve.pdf}
    \caption{Differential light curve of HAT-P-7 showing transit.}
    \label{fig:lightcurve}
\end{figure}

Table \ref{tab:observations} lists the observed systems.

\input{tables/observations.tex}

\end{document}
```

## Collaborative Writing Workflow

### Step 1: Data Analysis
```bash
# In Jupyter notebook
1. Perform analysis
2. Generate figures and tables
3. Save to manuscript/figures/ and manuscript/tables/
```

### Step 2: Commit Results
```bash
git add manuscript/figures/lightcurve.pdf
git add manuscript/tables/observations.tex
git commit -m "Add transit light curve and observation table"
git push origin main
```

### Step 3: Write in Overleaf
```
1. Pull changes from GitHub (if using Git integration)
2. Reference figures/tables in LaTeX
3. Write text around results
4. Push changes back to GitHub
```

### Step 4: Review and Iterate
```
1. Team reviews on GitHub or Overleaf
2. Make revisions to analysis or text
3. Repeat steps 1-3
```

## Best Practices

### Figure Quality

- **Format**: Use PDF for vector graphics (plots, diagrams)
- **Resolution**: 300 DPI minimum for raster images
- **Font size**: Make readable at publication size (8-10pt)
- **Color**: Use colorblind-friendly palettes
- **Labels**: Clear axis labels with units

### Table Formatting

- Use `booktabs` package for professional tables
- Include units in column headers
- Align decimal points
- Use `siunitx` package for numbers with uncertainties

### Version Control

- **Figures**: Name with descriptive names: `transit_lightcurve.pdf`
- **Tables**: Use consistent naming: `tab_observations.tex`
- **Versions**: Use git tags for manuscript versions: `v1.0-submission`

### File Sizes

- Keep figure files under 1 MB each
- Compress images if needed: `convert -quality 90 input.png output.png`
- Don't commit large FITS files to Git

## Example LaTeX Template

Create `manuscript/main.tex`:

```latex
\documentclass[twocolumn]{aastex631}
% American Astronomical Society journal format

\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{booktabs}

\shorttitle{Exoplanet Transit Analysis}
\shortauthors{Your Team}

\begin{document}

\title{Transit Timing Variations of HAT-P-7b}

\author{First Author}
\affiliation{Your Institution}

\author{Second Author}
\affiliation{Your Institution}

\begin{abstract}
We present photometric observations of the hot Jupiter HAT-P-7b...
\end{abstract}

\keywords{exoplanets --- techniques: photometric --- stars: individual (HAT-P-7)}

\section{Introduction}
\input{sections/introduction}

\section{Observations and Data Reduction}
\input{sections/observations}

\section{Analysis}
\input{sections/analysis}

\section{Results}

Figure \ref{fig:lightcurve} shows our differential light curve.

\begin{figure}[ht]
\centering
\includegraphics[width=\columnwidth]{figures/lightcurve.pdf}
\caption{Differential photometry light curve showing transit.}
\label{fig:lightcurve}
\end{figure}

\section{Discussion}
\input{sections/discussion}

\section{Conclusions}
\input{sections/conclusions}

\acknowledgments
We thank...

\bibliography{bibliography}

\end{document}
```

## Tools and Resources

### LaTeX Packages for Astronomy

- **aastex**: AAS journal format
- **mnras**: MNRAS journal format
- **natbib**: Bibliography management
- **siunitx**: Scientific numbers and units
- **graphicx**: Figure inclusion

### Online Tools

- [Overleaf Templates](https://www.overleaf.com/latex/templates): Journal-specific templates
- [Detexify](http://detexify.kirelabs.org/classify.html): Find LaTeX symbols
- [Tables Generator](https://www.tablesgenerator.com/): Create LaTeX tables

### References

- [AASTeX Guide](https://journals.aas.org/aastex-package-for-manuscript-preparation/)
- [LaTeX for Astronomers](https://www.ast.cam.ac.uk/~vasily/idl/latex/)
- [Writing Astronomy Papers](https://www.astrobetter.com/wiki/Writing+Astronomy+Papers)

## Troubleshooting

### Overleaf-GitHub Sync Issues

- Ensure you have write access to repository
- Check Overleaf is authorized in GitHub settings
- Try manual push/pull if automatic sync fails

### Figure Not Displaying

- Check file path is correct
- Ensure figure file is committed to Git
- Verify file extension matches `\includegraphics` command

### Table Formatting Errors

- Validate LaTeX table syntax
- Check for special characters (%, $, &, _)
- Use `\` to escape special characters

## Contact

For Overleaf-specific help:
- [Overleaf Documentation](https://www.overleaf.com/learn)
- [Contact Overleaf Support](https://www.overleaf.com/contact)

For project collaboration questions, open an issue on GitHub.
