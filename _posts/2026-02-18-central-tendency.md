# Measures of Central Tendency (Mean, Median & Mode)

## Mean (Average)

* Definition:

    The *Mean*, also called *Arithmetic Mean* or *Arithmetic Average*, is the average of a set of numbers. It is calculated by dividing the sum of all values, by the total number of values.

* Characteristics:

    * Sensitive to outliers.
    * Notated as $\mu$ (Greek mu) for populations, and $\bar{X}$ (X bar) for samples.
    * Calculated in the same way for populations and samples.

* Formula:

    $\mu=\frac{\sum_{i=1}^{N}{X_i}}{N}$

## Median (Middle Value)

* Definition:

    The *Median* is the middle value in an ascending list of values, separating the higher half form the lower half, if the number of values in the list is odd.
    If the number of values if even, the Median is the average between the two middle values.

* Characteristics:

    * Robust to outliers.
    * Useful for skewed distributions.
    * Same for populations and samples.

* Formulas:

    For odd data: $Median=\frac{N+1}{2}^{th}observation$

    For even data: $Median=\frac{\frac{N}{2}^{th}+(\frac{N}{2}+1)^{th}}{2}$

## Mode

* Definition:

    The *Mode* is the value that occurs most often in a data set. If each value occurs only once, then there is no mode. There can be multiple modes but generally, more than three kind of defeat the purpose of finding the mode.

* Characteristics:

    * Can be used with numerical as well as categorical data.
    * A data set can be uni-, bi-, tri-, or multimodal, depending on how many modes there are.

### Examples with Python and Numpy

```python
import numpy as np

arr = np.random.rand(100)

mean = sum(arr)/len(arr)

f"plain python: {mean}", f"numpy: {np.mean(arr)}"
```

```
('plain python: 0.4941350366338245', 'numpy: 0.4941350366338244')
```

```python
def median(arr):
    arr_asc = sorted(arr)
    pos = (len(arr_asc)+1)/2
    if pos % 1 == 0:
        idx = int(pos-1)
    else:
        idx = [int(pos // 1 - 1), int(pos // 1)]

    if isinstance(idx, int):
        return arr_asc[idx]
    return (arr_asc[idx[0]] + arr_asc[idx[1]]) / 2

f"plain python: {median(arr)}", f"numpy {np.median(arr)}"
```

```
('plain python: 0.4968189154566815', 'numpy 0.4968189154566815')
```

### Mode with Pandas

```python
import pandas as pd

arr = pd.Series([1,2,2,3,3,3,4,4,5])

mode = [k for k, v in dict(arr.value_counts()).items() if v == max(arr.value_counts())]

f"pandas value_counts: {mode}", f"pandas mode method: {arr.mode().values}"
```

```
('pandas value_counts: [3]', 'pandas mode method: [3]')
```

