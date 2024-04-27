# <p align="center">FMatx</p>

[中文](README.md) | English

FMatx, as **f**(ull accuraty) **mat**(rix), is a library written in
pure python determined to resolve Linear algebra and Linear programming
problems in a fast and easy way with keeping high quality.

## Features

- Implemented in Pure Python with no third parties requires
- Use simple global context manager to handle actions
- Support more than API for users including determinant, RREF, linear programming (also ilp), simplex method, and more

## Installation

Stable version:

	pip install -U fmatx

Development version:

	pip install -U git+https://github.com/hibays/fmatx.git

**Prerequisites**: FMatx requires Python 3.8 or newer

## Basic usage

Import basic core class.

	>>> from fmatx import Mat

Import global context manager.

	>>> from fmatx import mst

## Matrix Create

	>>> Mat([9, 7, 3]) # vectors
	
	>>> Mat().tolist()
	[]
	
	>>> Mat(3).tolist()
	[[], [], []]
	
	>>> Mat([[1, 2], [3, 4]])
	Mat(
	┌ 1 2 ┐
	└ 1 2 ┘)
	
	>>> Mat([(1, 2), (3, 4)])
	Mat(
	┌ 1 2 ┐
	└ 1 2 ┘)
	
	>>> Mat(((1, 2), (3, 4))) # to use it all elements have to be tuple
	Mat(
	┌ 1 2 ┐
	└ 1 2 ┘)

Convenient advanced functions are available for creating various standard
matrices, see `zeros`, `ones`, `diag`, `eye`, `randmat` and
`hilbert`.

	>>> eye(5)
	Mat(
	┌ 1  0  0  0  0 ┐
	│ 0  1  0  0  0 │
	│ 0  0  1  0  0 │
	│ 0  0  0  1  0 │
	└ 0  0  0  0  1 ┘)

## Matrix operators

	>>> a = Mat([[1, 2, 2,  2], [2, 4, 6,  8], [3, 6, 8, 10]])
	>>> a
	Mat(
	┌ 1  2  2   2 ┐
	│ 2  4  6   8 │
	└ 3  6  8  10 ┘)
	>>> 6*a/5 + 1 - 4 # full accuraty calculation
	Mat(
	┌ -9/5  -3/5  -3/5  -3/5 ┐
	│ -3/5   9/5  21/5  33/5 │
	└  3/5  21/5  33/5     9 ┘)

also calculates between matrix and matrix

	>>> a + a
	Mat(
	┌ 2   4   4   4 ┐
	│ 4   8  12  16 │
	└ 6  12  16  20 ┘)

You can raise powers of square matrices.

	>>> A = Mat([[7, 9], [8, 5]])
    >>> A**2
    Mat(
	┌ 121  108 ┐
	└  96   97 ┘)

Negative powers will calculate the inverse.

    >>> A**-1
    Mat(
	┌ -5/37   9/37 ┐
	└  8/37  -7/37 ┘)
    >>> A * A**-1
    Mat(
	┌ 1  0 ┐
	└ 0  1 ┘)

Matrix transposition is straightforward.
Also conjugate transposition via Mat.H.

    >>> A = ones(2, 3)
    >>> A
	Mat(
	┌ 1  1  1 ┐
	└ 1  1  1 ┘)
    >>> A.T
    Mat(
	┌ 1  1 ┐
	│ 1  1 │
	└ 1  1 ┘)
	>>> A.H
    Mat(
	┌ 1  1 ┐
	│ 1  1 │
	└ 1  1 ┘)

## Linear Algebra

RREF return tuple(rref of matrix, pivot_cols)

	>>> a.rref()
	(Mat(
	┌ 1  2  0  -2 ┐
	│ 0  0  1   2 │
	└ 0  0  0   0 ┘), (0, 2))

To compute determinant.

	>>> a.det()
	0

Note:
[Bareiss algorithm](https://en.wikipedia.org/wiki/Bareiss%20algorithm)
is used to compute determinant internally.
So following operation is ok.

	>>> mst.accuracy_protect = None # don't use full accuracy to compute
		
	>>> Mat(
	... [[ 67,  68,  -3,  71],
	...  [ 75,  27, -21,  30],
	...  [104, -34,  46, 163],
	...  [165, 110, 144,  25]])
	Mat(
	┌  67   68   -3   71 ┐
	│  75   27  -21   30 │
	│ 104  -34   46  163 │
	└ 165  110  144   25 ┘)
	
	>>> _.det()
	139971819.0

To compute Nullspace and column space.

	>>> a.nullspace()
	[Mat(
	┌ -2 ┐
	│  1 │
	│  0 │
	└  0 ┘), Mat(
	┌  2 ┐
	│  0 │
	│ -2 │
	└  1 ┘)]
	
	>>> a.columnspace()
	[Mat(
	┌ 1 ┐
	│ 0 │
	└ 0 ┘), Mat(
	┌ 0 ┐
	│ 1 │
	└ 0 ┘)]

To compute Rank (using Gauss Method).

	>>> a.rank()
	2

## Linear Programming (Also ILP)

It provided several methods that can solve **LP**, **MLP**,
and **ILP** problems in full accuracy.

Example 1: solving following LP question using simplex method.

	max z = 2x + y
		subject to
			 5y <= 15
		6x + 2y <= 24
		 x +  y <= 5
			x,y >= 0

	>>> C = Mat([2, 1])
	>>> A = Mat([[0, 5], [6, 2], [1, 1]])
	>>> b = Mat([15, 24, 5])
	
	>>> C.simplex(A, b, maximize=True)
	(Rational(17, 2), {1: Rational(7, 2), 2: Rational(3, 2)})

Example 2: solving following ILP question using branch and bound method.

	max z = 2x + y
		subject to
			 5y <= 15
		6x + 2y <= 24
		 x +  y <= 5
			x,y >= 0
			x,y ∈ Integers
			
	>>> C = Mat([2, 1])
	>>> A = Mat([[0, 5], [6, 2], [1, 1]])
	>>> b = Mat([15, 24, 5])
	
	>>> C.branch_bound(A, b, maximize=True)
	(Rational(8, 1), {1: Rational(4, 1), 2: Rational(0, 1)})

## Context manager

## Testing

> Note: To run testsuite, you must ensure your python had [mpmath](https://mpmath.org/) and [SymPy](https://sympy.org/) installed.

	python -m pytest ./testing -v
