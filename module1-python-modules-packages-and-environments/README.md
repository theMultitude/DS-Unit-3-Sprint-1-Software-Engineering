# Python Modules, Packages, and Environments

Places for your code (and dependencies) to live.

## Learning Objectives

- Understand and follow Python namespaces and imports
- Create a Python package and install dependencies in a dedicated environment

## Before Lecture

Install [Anaconda](https://www.anaconda.com/distribution) on your local machine
if you haven't already, and read the official documentation for
[Python modules](https://docs.python.org/3.7/tutorial/modules.html).

## Live Lecture Task

We're going to start our own Python package the right way - by making an
environment with `pipenv`, installing our dependencies, and making some classes.

## Assignment

Implement at least 3 of the following "helper" utility functions in `lambdata`:

- Check a dataframe for nulls, print/report them in a nice "pretty" format
- Report a confusion matrix, with labels for easier interpretation
- Train/*validate*/test split function for a dataframe
- "Generate more data" function, takes dataframes and makes more rows
- Contingency table + Chi-squared report function: takes two categorical
  variables, outputs a contingency table and corresponding Chi-squared test
- Your idea here!

Many of the above can be done with the right clever calls to `pandas`, `numpy`,
and other libraries - that's fine! Use those as dependencies. There's still
value in a package that encapsulates more complicated libraries and exposes
streamlined functionality with a simplified API.

## Resources and Stretch Goals

Check out the source code for [pandas](https://github.com/pandas-dev/pandas),
and see if you can make sense of it. Try to find the actual logic behind
specific functions you use (e.g. `pd.DataFrame`, `df.replace`, etc.). Reading
source code is challenging, especially from large codebases, but it's a skill
that will help you debug and fix real issues in professional situations.
