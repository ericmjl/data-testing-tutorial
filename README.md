# data-testing-tutorial

A short tutorial on how to do data testing.

# Environment

## Setup

I recommend using the [Anaconda distribution](https://www.continuum.io/downloads) of Python. To get setup, create a `conda` environment based on the provided [`environment.yml`](./environment.yml) spec file. Run the following commands in your bash terminal.

```bash
$ conda env create -f environment.yml
$ source activate datatest
```

## Checks

To check whether the environment is correctly setup, run the `checkenv.py` script. It should print to your terminal in green text, `All packages found; environment checks passed.`. Otherwise, `conda` or `pip` install the necessary packages stated.

# Authors

- Renee Chu
- [Eric J. Ma](http://www.ericmjl.com)

# Contributors

- Matt Bachmann: @Bachmann1234
- Hugo Bowne-Anderson: @hugobowne

# Credits

- [Divvy Data Set](https://www.divvybikes.com/data)
