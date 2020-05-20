# Measures of Skewness and Kurtosis

## Summary

- [__Question No. 1__](https://github.com/Bodera/learnPath_Mathematics/blob/master/statistics/solved-list2.md#question-no-1)
- [__Question No. 2__](https://github.com/Bodera/learnPath_Mathematics/blob/master/statistics/solved-list2.md#question-no-2)
- [__Question No. 3__](https://github.com/Bodera/learnPath_Mathematics/blob/master/statistics/solved-list2.md#question-no-3)
- [__Question No. 4__](https://github.com/Bodera/learnPath_Mathematics/blob/master/statistics/solved-list2.md#question-no-4)

### Question No. 1

Consider the table that shows the number of absences in the month of academics in the UCDB Engineering class and calculate the asymmetry coefficient and classify the distribution (table without class interval).

| Absences | Academics |
|:--------:|:---------:|
|     2    |     2     |
|     4    |     4     |
|     6    |     5     |
|     8    |     6     |
|    10    |     7     |
|    12    |     4     |
|    14    |     2     |
|          |     30    |

#### Procedures for the solution of question No. 1

__1st step__: Calculate the arithmetic average, mode and standart deviation of the distribution.

- Arithmetic average for tabular data

```txt
x̅ =
      ∑(fᵢ*x^ᵢ)
    ————————————
        ∑ fᵢ
fᵢ: relative frequency of xᵢ
MD: mid-range of xᵢ
∑(fᵢ*MD): summation of the product of fᵢ and x^ᵢ, for all instances of xᵢ
∑ fᵢ: summation of fᵢ, for all instances of xᵢ
```

| Absences | Academics | fᵢ*MD |
|:--------:|:---------:|:-----:|
|     2    |     2     |   4   |
|     4    |     4     |   16  |
|     6    |     5     |   30  |
|     8    |     6     |   48  |
|    10    |     7     |   70  |
|    12    |     4     |   48  |
|    14    |     2     |   28  |
|          |     30    |  244  |

```txt
244 ÷ 30
= 8.13
```

The arithmetic average is __8.13__.

- Mode

```txt
Modal class = 10 (higher frequency)
```

The mode is __10__.

- Standart deviation for tabular data

```txt
s = √ ( ∑((x^ᵢ - x̅)² * fᵢ) ÷ (n-1))

fᵢ: relative frequency of the x^ᵢ class
x^ᵢ: midpoint of each class
x̅: arithmetic mean of the tabular data
n: sum of all relative frequencies
```

![Question-1-std-dev-formula](https://latex.codecogs.com/svg.latex?\sqrt{\frac{\left(\left(2-8.13\right)^{2}\cdot2&plus;\left(4-8.13\right)^{2}\cdot4&plus;\left(6-8.13\right)^{2}\cdot5&plus;\left(8-8.13\right)^{2}\cdot6&plus;\left(10-8.13\right)^{2}\cdot7&plus;\left(12-8.13\right)^{2}\cdot4&plus;\left(14-8.13\right)^{2}\cdot2\right)}{30-1}})

The standart deviation is __3.3190__.

__2nd step__: Calculate the asymmetry coefficient.

![Question-1-asymmetry-coef-formula](https://latex.codecogs.com/svg.latex?\frac{\left(8.13-10\right)}{3.3190})

Asymmetry coefficient = __-0.5634__.

Asymmetry coefficient < 0, so the distribution is asymmetric negative, to the left.

Moderate asymmetry because: 0.15 < |AS| < 1

__3rd step__: Calculate the coefficient of kurtosis.

Discover Q₁, Q₃, P₁₀ and P₉₀.

```txt
Q₁ = (1*30) ÷ 4 = 7.5

Q₃ = (3*30) ÷ 4 = 22.5

P₁₀ = (10*30) ÷ 100 = 3

P₉₀ = (90*30) ÷ 100 = 27
```

As the table doesn't have class interval we have:

```txt
Q₁ class = 6 (where the 7.5º data is)
Q₁ = 6

Q₃ class = 10 (where the 22.5º data is)
Q₃ = 10

P₁₀ class = 4 (where the 3º data is)
P₁₀ = 4

P₉₀ class = 12 (where the 27º data is)
P₉₀ = 12
```

Now apply the formula:

![Question-1-kurtosis-coef-formula](https://latex.codecogs.com/svg.latex?\frac{\left(10-6\right)}{2\left(12-4\right)})

Coefficient of Kurtosis = __0.25__.

0.25 < 0.263, so the distribution has a leptokurtic curve.

### Question No. 2

Consider the table that shows the number of absences in the year of employees of a company. Calculate the asymmetry coefficient and classify the distribution (table with class interval).

| Absences | Employees |
|:--------:|:---------:|
|  2\|--4  |     6     |
|  4\|--6  |     9     |
|  6\|--8  |     11    |
|  8\|--10 |     16    |
| 10\|--12 |     13    |
| 12\|--14 |     10    |
| 14\|--12 |     5     |
|          |     70    |

#### Procedures for the solution of question No. 2

__1st step__: Calculate the arithmetic average, mode and standart deviation of the distribution.

- Arithmetic average for tabular data

```txt
x̅ =
      ∑(fᵢ*x^ᵢ)
    ————————————
        ∑ fᵢ
fᵢ: relative frequency of xᵢ
MD: mid-range of xᵢ
∑(fᵢ*MD): summation of the product of fᵢ and x^ᵢ, for all instances of xᵢ
∑ fᵢ: summation of fᵢ, for all instances of xᵢ
```

| MD | Absences | Employees | fᵢ*MD |
|:--:|:--------:|:---------:|:-----:|
|  3 |  2\|--4  |     6     |   18  |
|  5 |  4\|--6  |     9     |   45  |
|  7 |  6\|--8  |     11    |   77  |
|  9 |  8\|--10 |     16    |  144  |
| 11 | 10\|--12 |     13    |  143  |
| 13 | 12\|--14 |     10    |  130  |
| 15 | 14\|--16 |     5     |   75  |
|    |          |     70    |  632  |

```txt
632 ÷ 70
= 9.02
```

The arithmetic average is __9.02__.

- Mode

```txt
Mo = Lim inf + h * (Δ₁ ÷ (Δ₁ + Δ₂))

Lim inf: lower limit of the modal class
h: amplitude of the modal class (any lower limit subtracted from the immediately lower limit)
Δ₁: relative frequency of the modal class subtracted from the relative frequency immediately preceding
Δ₂: relative frequency of the modal class subtracted from the relative frequency immediately afterwards
```

knowing this, the mode can now be calculate:

```txt
modal class: 8|--10 (more number of frequencies)

Mo = 8 + 2 * (5 ÷ (5 + 3))
Mo = 8 + 2 * (5 ÷ 8)
Mo = 8 + 2 * 0.625
Mo = 8 + 1.25
Mo = 9.25
```

The mode is __9.25__.

- Standart deviation for tabular data

```txt
s = √ ( ∑((x^ᵢ - x̅)² * fᵢ) ÷ (n-1))

fᵢ: relative frequency of the x^ᵢ class
x^ᵢ: midpoint of each class
x̅: arithmetic mean of the tabular data
n: sum of all relative frequencies
```

![Question-1-std-dev-formula](https://latex.codecogs.com/svg.latex?\sqrt{\frac{\left(\left(3-9.02\right)^{2}\cdot6&plus;\left(5-9.02\right)^{2}\cdot9&plus;\left(7-9.02\right)^{2}\cdot11&plus;\left(9-9.02\right)^{2}\cdot16&plus;\left(11-9.02\right)^{2}\cdot13&plus;\left(13-9.02\right)^{2}\cdot10&plus;\left(15-9.02\right)^{2}\cdot5\right)}{70-1}})

The standart deviation is __3.3963__.

__2nd step__: Calculate the asymmetry coefficient.

![Question-1-asymmetry-coef-formula](https://latex.codecogs.com/svg.latex?\frac{\left(9.02-9.25\right)}{3.3963})

Asymmetry coefficient = __-0.0677__.

Asymmetry coefficient < 0, so the distribution is asymmetric negative, to the left.

Weak asymmetry because: 0 < |AS| < 0.15

__3rd step__: Calculate the coefficient of kurtosis.

Discover Q₁, Q₃, P₁₀ and P₉₀.

```txt
Q₁ = (1*70) ÷ 4 = 17.5

Q₃ = (3*70) ÷ 4 = 52.5

P₁₀ = (10*70) ÷ 100 = 7

P₉₀ = (90*70) ÷ 100 = 63
```

As the table have class interval we have:

```txt
Q₁ class = 6|--8
Q₁ = 6 + 2 * ((17.5 - 15) ÷ 11)
Q₁ = 6.45

Q₃ class = 10|--12
Q₃ = 10 + 2 * ((52.5 - 42) ÷ 13)
Q₃ = 11.6153

P₁₀ class = 4|--6
P₁₀ = 4 + 2 * ((7 - 6) ÷ 9)
P₁₀ = 4.22

P₉₀ class = 12|--14
P₉₀ = 12 + 2 * ((63 - 55) ÷ 10)
P₉₀ = 13.6
```

Now apply the formula:

![Question-1-kurtosis-coef-formula](https://latex.codecogs.com/svg.latex?\frac{\left(11.6153-6.45\right)}{2\left(13.6-4.22\right)})

Coefficient of Kurtosis = __0.2753__.

0.2753 > 0.263, so the distribution has a platykurtic curve.
