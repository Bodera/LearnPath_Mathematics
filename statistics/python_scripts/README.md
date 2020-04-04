# Basic data work with Python for Statistics

## Tools used

* Python 3
* Conda package and environment manager
* Pandas
* Matplotlib

### Instructions

__1st__ - Preparing the environment:

```bash
$ conda create --name statistics_stuff python=3.7
$ source activate statistics_stuff
$ conda install pandas
$ conda config --add channels conda-forge
$ conda search matplotlib --channel conda-forge
$ conda install matplotlib matplotlib-base mpl_sample_data
$ python3 <file.py>
```

__2nd__ - Know what you can do with Pandas:

* *DataFrame*: abstraction of a spreadsheet.
* *Series*: abstraction of a column.
* *DataFrame.shape*: an attribute (so no need to use parantheses) containing the number of rows and columns *(nrows, ncolumns)*.
* *DataFrame.head()*: a method (so we need to use parantheses) that returns the first *n*, where *n* must be an integer, rows of a DataFrame or Series.

__3rd__ - Seriously, just read the friendly manual.

[!RTFM](https://www.memecreator.org/static/images/memes/4669289.jpg)
