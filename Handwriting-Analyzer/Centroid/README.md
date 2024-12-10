# Centroid
Machine-learning program; part of a project to compute the centroid of handwritten letters

In this exercise, "letters" consist of a single row of pixels, whose (grayscale) values are limited to 0 and 255. The single-coordinate centroid `c-x-rounded` is the target of an array whose columns are the value of the pixels for the given row. The model uses scikit-learn's `train_test_split` and the `LogisticRegression `algorithm to predict the cdntroid's coordinate.

# Usage

Run the attached Jupyter notebook centroid.ipynb in the browser of your choice; the data file `letters-1-row.xlsx` needs to be placed in the same folder as the notebook.

# Results
The dataframe of the notebook's last cell shows the pixels (11) of each row; the coordinate of the target; and the predicted coordinate.

