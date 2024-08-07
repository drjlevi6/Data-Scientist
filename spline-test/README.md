# spline_test.ipynb
Machine-learning project to verify that a curve I've generated artificially is a spline. The curve, `S`, is defined in the accompanying Jupyter notebook, `spine_test.ipynb`; there is an accompanying figure, `spline-test-<datetime>.png` that shows `S`, its creation, and that it matches a `scikit-learn` model, specifically created as a spline.

## Background:
Let `[a, b]` be a closed interval, where `a`, `b` are real numbers. Let `[a,b]` be partitioned into a sequence `{x0, x1,...,xn}`, where `x0=a`, `xn=b`, and `x0 < x1 < ... < xn`. A function `S:[a, b] -> R` is a **spline** if it can be decomposed into functions `S1, S2,...Sn: [xi, x(i+1) -> R` such that:

1. Each `Si` is a polynomial;
* `Si(xi) = S(i+1)(xi)`, for i in `{0,...,n}`;
* `Si'(xi) = S(i+1)'(xi)`, for i in `{0,...,n}`.

The idea here is that all of the `Si` must join "smoothly", i.e., there can be no cusps in `S`. (There may be other conditions which I don't know for S to be a spline.)

## Project contains:
* A Jupyter notebook, `spline_test.ipynb`;
* A Python module, `date_time_string.py`, which the notebook depends on;
* An image, `spline-test-<date>-<time>.png`, showing the output of the notebook;
* This README file.

## Dependencies:
* A Python installation (should be platform-independent);
* The packages `numpy`, `pandas`, `matplotlib`, `sklearn`. (I'm using the Anaconda distribution of Python, which includes these; other distributions could also be used.)
* The module `date_time_string.py` (provided);
* An operating system capable of displaying `PNG` files.

## To run this project:
* Move module `date_time_string.py` to a folder in your `$PYTHONPATH`.
* Run `spline_test.ipynb` in your browser of choiuce.

## Results:
The notebook will display three figures:

* **Figure 1** displays two polynomial functions `f, g:[-2,2]-> R` with the properties that:

	1. f(0) = g(0) = 0;
	2. f'(0) = g'(0) = 1.

* **Figure 2** displays a new curve, `S(x)`, constructed piecewise from `f(x)`, `g(x)`.
* **Figure 3** shows that `S` matches perfectly a spline generated by `scikit-learn`, and thus that `S` is itself a spline.

A PNG file will be generated, displayng the output of the notebook.

## Reference:

Wikipedia, [Spline(mathematics)](https://en.wikipedia.org/wiki/Spline_(mathematics)).

## Use, modify, enjoy!
## Creator/Maintainer:

Jonathan Levi, MD [drjlevi6@aol.com](mailto:drjlevi6@aol.com)
