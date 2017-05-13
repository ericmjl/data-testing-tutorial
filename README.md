# data-testing-tutorial

A short tutorial on how to do data testing.

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
