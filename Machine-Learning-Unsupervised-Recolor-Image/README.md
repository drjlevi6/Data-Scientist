# Machine-Learning-Unsupervised-Recolor-Image
Scikit-learn exercise: use unsupervised learning function `KMeans` to redraw a multicolor file with just two colors, dark and light.

## Package Contains:
* A Jupyter notebook, `RGB_Cluster_Analysis.ipynb`.
* Two Python modules, `date_time_string.py` and `save_figure_per_user.py` used by the Jupyter nobook.
* A multicolor image file, `function-fx-drawing.png`, used as imput by the Jupyter notebook.
* A second image file, `drawing-small.png`, which can be used instead of the full-sized file for debugging
* Sample two-color outputs of the notebook, `Fig-4-function-fx-recolored-<date>-<time>.png`.
* Other image files `Fig-...png` created by the notebook.
* This README file.

## To Run the Notebook:
* Move `save_figure_per_user.py` and `date_time_string.py` to a folder in your `$PYTHONPATH`.
* Move files `function-fx-drawing.png`, `drawing-small.png` to a location of your choice; change the path `png_path` in cell 2 of the notebook accordingly.
* Edit the variable `dir_path` in cell 2 of the notebook to reflect your location for files.`function-fx-drawing.png`` and `drawing-small.png`.
* Comment out one of the two lines defining the variable `png_path` to reflect the image file you'working with.

You should now be able to run the notebook.