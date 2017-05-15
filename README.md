# Best Testing Practices for Data Science

A short tutorial for data scientists on how to write tests for your code and your data.

## How to use this repository

The tutorial notes are typed up in Jupyter notebooks, and static HTML versions are available under the [`docs`](./docs/) folder. For the non-bonus material, I suggest working through the notes in order. With the exception of the Projects, the bonus material can be tackled in any order.

## Feedback

If you've taken a version of this tutorial, please leave feedback [here](https://ericma1.typeform.com/to/Ua0LBs).

## Pre-Requisite Knowledge

I am assuming you are of the following type of coder:

- You are a data analytics type, who knows how to read/write CSV files with Pandas, and do basic data manipulation (slicing, indexing rows + columns, using the `.apply()` function).
- You are not necessarily a seasoned software developer who has experience running tests.
- You are comfortable with operating in the Terminal environment.
- You are comfortable with Python, and know:
    - the context manager syntax (`with ....`),
    - assertions (`assert conditions1 == condition2`),
    - file I/O (`with open(....) as f:...`),
    - list/dict/tuple comprehensions (`[a for a in container if condition(a)]`),
    - checking types & attributes (`isinstance(obj, type) or hasattr(obj, attr)`).
- You have some rudimentary knowledge of `numpy`, particularly the the `array.min()`, `array.max()`, `array.mean()`, `array.std()`, and `numpy.allclose(a1, a2)` function calls.

# Environment Setup

## `conda` setup

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

- [Eric J. Ma](http://www.ericmjl.com)

# Contributors

Special thanks goes to individuals who have contributed in ways big and small to the improvement of the material.

- Renee Chu
- Matt Bachmann: @Bachmann1234
- Hugo Bowne-Anderson: @hugobowne
- Boston Python tutorial attendees:
    - @races1986
    - Thao Nguyen: @ThaoNguyen15
    - @ChrisMuir

# Data Credits

- [Divvy Data Set](https://www.divvybikes.com/data)
- [Analyze Boston](https://data.boston.gov/)
- Mia T. Lieberman for the sanitization dataset.
