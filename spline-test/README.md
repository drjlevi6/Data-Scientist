# spline_test.ipynb
Machine-learning project to verify that a curve I've artificially is a spline. The curve is defined in the accompanying Jupyter notebook, `spine_test.ipynb`; there is an accompanying figure, `spline-test-<datetime>.png` that shows the curve, its creation, and that it matches a `scikit-learn` model, specifically created as a spline.

## Background:
Let `[a, b]` be a closed interval, where `a`, `b` are real numbers. Let `[a,b]` be partitioned into a sequence `{x0, x1,...,xn}`, where `x0=a`, `xn=b`, and `x0 < x1 < ... <xn`. A function `S:[a, b] -> R` is called a **spline** if it can be decomposed into functions `S1, S2,...Sn: [xi, x(i+1) -> R` such that:

* Each `Si` is a polynomial;
* `Si(xi) = S(i+1)(xi)`, for i in `{0,...,n-`}`;
* `Si'(xi) = S(i+1)'(xi)`, for i in `{0,...,n-`}`.

The idea here is that all of the `Si` must join "smoothly", i.e., there can be no cusps in `S`. (There may be other conditions which I don't know for S to be a spline.)

** 


