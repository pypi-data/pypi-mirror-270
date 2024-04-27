# <p align="center">FMatx</p>

中文 | [English](README.md)

FMatx，作为 **f**(ull accuraty) **mat**(rix) 的缩写，是一个用纯Python编写的库，旨在以快速、简便且高质量的方式解决线性代数和线性规划问题。

## 功能

- 用纯Python编写，无需第三方依赖
- 使用简单的全局上下文管理器来处理操作
- 提供多种API供用户使用，包括行列式、行最简形式（RREF）、线性规划（也包括整数线性规划）、单纯形法等

## 安装

稳定版:

	pip install -U fmatx

开发版:

	pip install -U git+https://gitee.com/hibays/fmatx.git

**前提条件**：FMatx 需要 Python 3.8 或更高版本

## 基本用法

导入基本核心类：

	>>> from fmatx import Mat

导入全局上下文管理器：

	>>> from fmatx import mst

## 矩阵创建

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

还提供方便的高级函数来创建各种标准矩阵，如 `zeros`, `ones`, `diag`, `eye`, `randmat` 和
`hilbert`.

	>>> eye(5)
	Mat(
	┌ 1  0  0  0  0 ┐
	│ 0  1  0  0  0 │
	│ 0  0  1  0  0 │
	│ 0  0  0  1  0 │
	└ 0  0  0  0  1 ┘)

## 矩阵运算

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

也支持矩阵与矩阵之间的计算

	>>> a + a
	Mat(
	┌ 2   4   4   4 ┐
	│ 4   8  12  16 │
	└ 6  12  16  20 ┘)

你可以对方阵进行幂运算。

	>>> A = Mat([[7, 9], [8, 5]])
    >>> A**2
    Mat(
	┌ 121  108 ┐
	└  96   97 ┘)

负幂次将计算矩阵的逆。

    >>> A**-1
    Mat(
	┌ -5/37   9/37 ┐
	└  8/37  -7/37 ┘)
    >>> A * A**-1
    Mat(
	┌ 1  0 ┐
	└ 0  1 ┘)

矩阵转置很简单。
通过Mat.H进行共轭转置。

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

## 线性代数

简化的行阶梯形矩阵（内部使用 Gauss-Jordan 消元法）return tuple(rref of matrix, pivot_cols)

	>>> a.rref()
	(Mat(
	┌ 1  2  0  -2 ┐
	│ 0  0  1   2 │
	└ 0  0  0   0 ┘), (0, 2))

计算行列式。

	>>> a.det()
	0

注意：
[Bareiss algorithm](https://en.wikipedia.org/wiki/Bareiss%20algorithm)
用于内部计算行列式。
所以以下操作是可行的。

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

计算零空间和列空间。

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

计算秩（使用高斯消元法）。

	>>> a.rank()
	2

## 线性规划

它提供了几种方法，可以在全精度下解决LP、MLP和ILP问题。

示例1：使用单纯形法求解以下LP问题。

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

示例2：使用分支定界法求解以下ILP问题。

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

## 上下文管理器

## 测试

> 注意：要运行测试套件，您必须确保您的python环境已经安装了 [mpmath](https://mpmath.org/) 和 [SymPy](https://sympy.org/)。

	python -m pytest ./testing -v
