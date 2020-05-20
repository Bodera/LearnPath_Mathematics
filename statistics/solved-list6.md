# Linear regression

The minimum squares method.

- Formula for `m`

```txt
m =
      n * ∑xᵢyᵢ - (∑xᵢ) * (∑yᵢ)
    ——————————————————————————————
            n * ∑xᵢ² - (∑xᵢ)²
```

- Formula for `b`

```txt
b =
      ∑yᵢ            ∑xᵢ
    ———————  - m * ———————
       n              n
```

- Formula for `correlation index`

```txt
r =
            n * ∑xᵢyᵢ - (∑xᵢ) * (∑yᵢ)
    —————————————————————————————————————————
        √n*∑xᵢ²-(∑xᵢ)² * √n*∑yᵢ²-(∑yᵢ)²
```

## Summary

- [__Question No. 1__](https://github.com/Bodera/learnPath_Mathematics/blob/master/statistics/solved-list2.md#question-no-1)
- [__Question No. 2__](https://github.com/Bodera/learnPath_Mathematics/blob/master/statistics/solved-list2.md#question-no-2)
- [__Question No. 3__](https://github.com/Bodera/learnPath_Mathematics/blob/master/statistics/solved-list2.md#question-no-3)
- [__Question No. 4__](https://github.com/Bodera/learnPath_Mathematics/blob/master/statistics/solved-list2.md#question-no-4)
- [__Question No. 5__](https://github.com/Bodera/learnPath_Mathematics/blob/master/statistics/solved-list2.md#question-no-5)
- [__Question No. 6__](https://github.com/Bodera/learnPath_Mathematics/blob/master/statistics/solved-list2.md#question-no-6)
- [__Question No. 7__](https://github.com/Bodera/learnPath_Mathematics/blob/master/statistics/solved-list2.md#question-no-7)
- [__Question No. 8__](https://github.com/Bodera/learnPath_Mathematics/blob/master/statistics/solved-list2.md#question-no-8)
- [__Question No. 9__](https://github.com/Bodera/learnPath_Mathematics/blob/master/statistics/solved-list2.md#question-no-9)

### Question No. 1

Determine, by the method of least squares, the equation of the line closest to the points (xᵢ, yᵢ) for the function `y = mx + b` given by the table:

|       |    |    |    |   |   |
|-------|----|----|----|---|---|
| __x__ | -2 | -1 |  0 | 1 | 2 |
| __y__ |  0 |  0 | -1 | 0 | 7 |

#### Procedures for the solution of question No. 1

__1st step__: Calculate the value of `m` and `b`.

Collect the necessary variables:

```txt
n = 5
∑xᵢyᵢ = 14
∑xᵢ = 0
∑yᵢ = 6
∑xᵢ² = 10
(∑xᵢ)² = 0
```

![Question1-calculating-m](https://latex.codecogs.com/svg.latex?\frac{5\cdot14-0\cdot6}{5\cdot10-0})

The value of `m` is __1.4__.

![Question1-calculating-b](https://latex.codecogs.com/svg.latex?\frac{6}{5}-\left(-1.4\right)\cdot\frac{0}{5})

The value of `b` is __1.2__.

__3rd step__: Provide the line equation.

```txt
y = 1.4x + 1.2
```

### Question No. 2

Use the minimum squares method to determine the linear fit (*y = b + mx*) to the table:

|       |    |     |    |     |    |     |    |
|-------|----|-----|----|-----|----|-----|----|
| __x__ |  1 | 1.5 |  2 | 2.5 |  3 | 3.5 | 4  |
| __y__ | 25 |  31 | 27 |  28 | 36 | 35  | 34 |

#### Procedures for the solution of question No. 2

__1st step__: Calculate the value of `m` and `b`.

Collect the necessary variables:

```txt
n = 7
∑xᵢyᵢ = 562
∑xᵢ = 17.5
∑yᵢ = 216
∑xᵢ² = 50.75
(∑xᵢ)² = 306.25
```

![Question2-calculating-m](https://latex.codecogs.com/svg.latex?\frac{7\cdot562-17.5\cdot216}{7\cdot50.75-306.25})

The value of `m` is __3.1428__.

![Question2-calculating-b](https://latex.codecogs.com/svg.latex?\frac{216}{7}-3.1428\cdot\frac{17.5}{7})

The value of `b` is __23__.

__3rd step__: Provide the line equation.

```txt
y = 23 + 3.1428x
```

### Question No. 3

Using the minimum squares method in a convenient way, approximate the points in the table below using a function of the type `b + mx`:

|       |   |   |   |   |
|-------|---|---|---|---|
| __x__ | 0 | 1 | 2 | 3 |
| __y__ | 1 | 2 | 4 | 8 |

#### Procedures for the solution of question No. 3

__1st step__: Calculate the value of `m` and `b`.

Collect the necessary variables:

```txt
n = 4
∑xᵢyᵢ = 34
∑xᵢ = 6
∑yᵢ = 15
∑xᵢ² = 14
(∑xᵢ)² = 36
```

![Question3-calculating-m](https://latex.codecogs.com/svg.latex?\frac{4\cdot34-6\cdot15}{4\cdot14-36})

The value of `m` is __2.3__.

![Question3-calculating-b](https://latex.codecogs.com/svg.latex?\frac{15}{4}-2.3\cdot\frac{6}{4})

The value of `b` is __0.3__.

__3rd step__: Provide the line equation.

```txt
y = 0.3 + 2.3x
```

### Question No. 4

The table below shows the pulp production (in tons) of a gift paper industry:

|            |      |      |      |      |      |      |      |      |      |
|:----------:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|  __Years__ | 2000 | 2001 | 2002 | 2003 | 2004 | 2005 | 2006 | 2007 | 2008 |
| __Amount__ |  34  |  36  |  36  |  38  |  41  |  42  |  43  |  44  |  46  |

Determine an estimate for 2009 production.

#### Procedures for the solution of question No. 4

__1st step__: Calculate the value of `m` and `b`.

Collect the necessary variables:

```txt
n = 9
∑xᵢyᵢ = 721530
∑xᵢ = 18036
∑yᵢ = 360
∑xᵢ² = 36144204
(∑xᵢ)² = 325297296
```

![Question4-calculating-m](https://latex.codecogs.com/svg.latex?\frac{9\cdot721530-18036\cdot360}{9\cdot36144204-325297296})

The value of `m` is __1.5__.

![Question4-calculating-b](https://latex.codecogs.com/svg.latex?\frac{360}{9}-1.5\cdot\frac{18036}{9})

The value of `b` is __-2966__.

__3rd step__: Provide the line equation.

```txt
y = 1.5x + (-2966)
```

__4th step__: Estimate the amount for the year of 2009.

```txt
x = 2009

y = 1.5 * 2009 - 2966
y = 47.5 tons
```

### Question No. 5

The table below shows the variation in the UPC value, relative to some months.

|            |       |       |       |        |           |         |          |
|:----------:|:-----:|:-----:|:-----:|:------:|:---------:|:-------:|:--------:|
| __Months__ |  May  |  June |  July | August | September | October | November |
|  __Value__ | 10.32 | 10.32 | 11.34 |  11.34 |   11.34   |  12.22  |   12.22  |

Determine an estimate for the month of December.

#### Procedures for the solution of question No. 5

__1st step__: Calculate the value of `m` and `b`.

Collect the necessary variables:

```txt
n = 7
∑xᵢyᵢ = 642.3
∑xᵢ = 56
∑yᵢ = 79.1
∑xᵢ² = 476
(∑xᵢ)² = 3136
```

![Question5-calculating-m](https://latex.codecogs.com/svg.latex?\frac{7\cdot642.3-56\cdot79.1}{7\cdot476-3136})

The value of `m` is __0.3392__.

![Question5-calculating-b](https://latex.codecogs.com/svg.latex?\frac{79.1}{7}-0.3392\cdot\frac{56}{7})

The value of `b` is __8.5864__.

__3rd step__: Provide the line equation.

```txt
y = 0.3392x + 8.5864
```

__4th step__: Estimate the value for the month of december.

```txt
x = 12

y = 0.3392 * 12 + 8.5864
y = 12.65
```

### Question No. 6

A group of customs officials made an assessment of the apparent weight of some containers. With the real weight and the average of the apparent weights, given by the group, the table was obtained:

|                     |    |    |    |    |    |    |     |
|:-------------------:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|
|   __Real weight__   | 18 | 30 | 42 | 62 | 73 | 97 | 120 |
| __Apparent weight__ | 10 | 23 | 33 | 60 | 91 | 98 | 159 |

Based on the table above, what is the correlation index?

#### Procedures for the solution of question No. 6

__1st step__: Calculate the value of `r`.

Collect the necessary variables:

```txt
n = 7
∑xᵢyᵢ = 41205
∑xᵢ = 442
∑yᵢ = 474
∑xᵢ² = 35970
(∑xᵢ)² = 195364
∑yᵢ² = 48484
(∑yᵢ)² = 224676
```

![Question6-calculating-r](https://latex.codecogs.com/svg.latex?\frac{7\cdot41205-442\cdot474}{\sqrt{7\cdot35970-195364}\cdot\sqrt{7\cdot48484-224676}})

The value of `r` is __0.9810__.

0.9 < |0.9810| < 1, means that is an almost perfect correlation between __x__ and __y__.

### Question No. 7

Consider the results of two alpha and beta quality tests, performed on a batch of beauty products from the Beleza Pura brand:

|           |    |    |    |    |    |    |    |    |    |
|:---------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|----|----|
| __Alpha__ | 11 | 14 | 19 | 22 | 28 | 30 | 31 | 34 | 34 |
|  __Beta__ | 13 | 14 | 18 | 15 | 22 | 17 | 24 | 22 | 25 |

Based on the table above, what is the correlation index?

#### Procedures for the solution of question No. 7

__1st step__: Calculate the value of `r`.

Collect the necessary variables:

```txt
n = 9
∑xᵢyᵢ = 4479
∑xᵢ = 223
∑yᵢ = 170
∑xᵢ² = 6119
(∑xᵢ)² = 49729
∑yᵢ² = 3372
(∑yᵢ)² = 28900
```

![Question7-calculating-r](https://latex.codecogs.com/svg.latex?\frac{9\cdot4479-223\cdot170}{\sqrt{9\cdot6119-49729}\cdot\sqrt{9\cdot3372-28900}})

The value of `r` is __0.8632__.

0.7 < |0.8632| < 0.9, means that is a high correlation between __x__ and __y__.

### Question No. 8

#### Procedures for the solution of question No. 8

### Question No. 9

#### Procedures for the solution of question No. 9
