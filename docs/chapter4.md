# Part 4: Checking Data Assumptions

Summary of section: Participants will write tests that check the assumptions that they may have about the data that they received. Applied to pre-data analysis, especially with streams of data coming in.

1. Write tests for column data types: `int`, `float`, `str`, `object`.
1. Write tests that check that there are no unexpected empty data cells: finding `NaN` with `pandas`.
1. Write tests that check for value correctness (e.g. cannot have negative numbers where log10 transform expected).
1. Write tests that check textual data for correct lengths (e.g. biological sequence data should fall within some expected range of lengths).
1. Write tests that check for potential outlier data points (e.g. use of Q-test).
1. Write tests that check for normality of data (e.g. use of scipy's K-S test, use of K-L divergence).
