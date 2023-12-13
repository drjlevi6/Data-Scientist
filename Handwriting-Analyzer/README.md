# Handwriting-Analyzer

## Learns to recognize this writer's individual, handwritten characters and convert to print. (Other writers would have to submit their own handwritten characters for this program to learn.)

## Usage: 

### User submits handwritten characters in rectangular graph paper with cells 1/3" to a a side. By a lengthy process (largely handwritten, needs to be automated) the letters are converted to strings of pixels, and from there to a series of numbers based on the pixels' RGB color; the numbers are converted to pandas dataframes and submitted to scikit-learn for training.

## Depends:

* Python 3
* ImageMagick
* A graphics program that understands the XPM file format
* The bash shell
* Jupyter notebooks
* numpy, pandas, scikit-learn
* And others...?

