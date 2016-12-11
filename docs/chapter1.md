<link rel="stylesheet" type="text/css" href="css/dtt.css">
<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">


# Why Data Testing

With every line of code that we write, we make assumptions about them.

With every piece of data that we receive, we likewise make assumptions about them.

This is a "book" dedicated to helping you uncover those assumptions, express them as code, and automatically execute them to make your data analysis workflow and pipelines more robust.

## Things to check in doing data science

Like any good scientist, before you go on to analyze the data you have on hand, you should probably check for a few basic things:

1. **Data types.** Are your data categorical, ordinal, or continuous? If they are categorical or ordinal, are they encoded as strings or as integers? If they are continuous, is it continuous in terms of having a long list of integers, or continuous floating point numbers?
1. **Data structure.** Do you have a set of definitions for what each column means?
1. **Data completeness.** Are you expecting that every column of data that you have will have a value from each row?
1. **Data integrity.** Do you have a stray comma present somewhere in a CSV file? Do you have a string present in a column that should only be comprised of floats?

## Things to check when writing code

Like any good software engineer, any code that you write, particularly those encapsulated in functions, should be accompanied by a suite of tests written for them. This will help you check for:

1. **Function correctness.** Does the function transform the input into the output in ways that are expected?
1. **Boundary cases.** Are there edge cases that cause your functions to fail?
1. **Counter-examples.** Are there logically incoherent combinations of parameter values that may cause downstream problems?
1. **Code coverage.** Have you written at least one test for every single line call in a function, done for every function?
