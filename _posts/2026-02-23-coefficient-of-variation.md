## Coefficient of Variation (CV) - relative standard deviation

$CV=\frac{StdDev}{Mean}$

The *Coefficient of Variation* is a relative measure of variability. It is calculated by dividing the standard deviation by the mean.
Unlike standard deviation, CV is a standardized and unitless measure which makes it useful for comparison. Comparing the standard deviations across data sets is meaningless, while comparing coefficients of variation is not.

Population Formula: $C_V=\sigma/\mu$

Sample Formula: $\widehat{C_V}=s/\bar{X}$

```python
import numpy as np

x = np.linspace(1,10,10)
np.std(x, ddof=1) / np.mean(x)
```

```
np.float64(0.5504818825631803)
```

### Interpretation

Analysts often report a the coefficient of variation as a percentage. In the above example the standard deviation of x is 55% of the mean of x. A CV of 1 or 100% means that the standard deviation is exactly equal to the mean. A CV less than 1 is typical. A higher value indicates a higher relative variability.

