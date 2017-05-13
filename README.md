# data-testing-tutorial

A short tutorial on how to do data testing.

# How to use this repository

I suggest having the notebooks open **through GitHub inside your browser**. The Jupyter notebooks are mostly a presentation tool; iterative prototyping can be done using the IPython shell or Python interpreter. Almost all of what we will do involves the Terminal and your favourite plain text editor.

# Pre-Requisite Knowledge

I am assuming you are of the following type of coder:

- You are a data analytics type, who knows how to read/write CSV files with Pandas, and do basic data manipulation (slicing, indexing rows + columns, using the `.apply()` function).
- You are not necessarily a seasoned software developer who has experience running tests.
- You are comfortable with operating in the Terminal environment.
- You are comfortable with Python, and know the context manager syntax (`with ....`), assertions (`assert conditions1 == condition2`), file I/O (`with open(....) as f:...`), and list/dict/tuple comprehensions (`[a for a in container if condition(a)]`).
- You have some rudimentary knowledge of `numpy`, particularly the the `array.min()`, `array.max()`, `array.mean()`, `array.std()`, and `numpy.allclose(a1, a2)` function calls.

# Environment

## `conda` Setup

I recommend using the [Anaconda distribution](https://www.continuum.io/downloads) of Python. This is best supported for Mac OS X and Linux-based systems.

To get setup, create a `conda` environment based on the provided [`environment.yml`](./environment.yml) spec file. Run the following commands in your bash terminal.

```bash
$ bash conda-setup.sh
```

## `pip` setup

The alternative way is to use a virtualenv environment:

```bash
$ bash venv-setup.sh
$ source datatest/bin/activate
```

## Checks

To check whether the environment is correctly setup, run the `checkenv.py` script:

```bash
$ python checkenv.py
```

It should print to your terminal in green text, `All packages found; environment checks passed.`. Otherwise, `conda` or `pip` install the necessary packages stated (they will show up one by one).

# Authors

- Renee Chu
- [Eric J. Ma](http://www.ericmjl.com)

# Contributors

- Matt Bachmann: @Bachmann1234
- Hugo Bowne-Anderson: @hugobowne
- Boston Python tutorial students:
    - @races1986
    - Thao Nguyen: @ThaoNguyen15

# Credits

- [Divvy Data Set](https://www.divvybikes.com/data)
