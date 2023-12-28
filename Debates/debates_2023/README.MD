# Debates_2023

### This is an abstract version of the debates earlier this year between the Republican Presidential candidates. In this version, the candidates' rankings are adjusted randomly and plotted; the shifts in rank are visually rounded using sigmoid curves (the actual goal of this program.)

### In this version, a user-defined number of (anonymous) "candidates" undergo a user-defined number of "debates"; after each "debate" the candidates receive new rankings as above and their progress is plotted using the Plotly graphics package. (No candidate is dropped during the process.)

## Contents:

### This folder is actually a Python package (see instructions for running it below.) In addition, there are items outside of the Python structure (which will be moved to their own folder in the future): a Finder folder icon ("debates-screenshots", macOS) customized to show two "debates", and a Jupyter notebook, debates.ipynb.

## Requires:

### A Macintosh computer. (Perhaps it could be run on Linux or Windows platforms with suitable adjustments.)

## Installing the Package:

* Download` it to a location in your computer's `PYTHONPATH`;
* Create symlinks of all the .py files in the same `PYTHONPATH`;

## Running the Package:

* Edit line 6 of `__main__.py:` change `n_candidates`and `n_debates`to suit your preferences. (This will be changed in a future revision.)
* Using `Terminal.app` (or a corresponding app in other platforms) run `python -m Debates_2023` . The package will import additional Python modules as needed, and display a graph of the candidates' rankings in your default browser.

### That should be all. Have fun!