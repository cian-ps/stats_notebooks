## Margin of Error

The *Margin of Error* (MOE) is a statistic that expresses the amount of random sampling error. More precisely, the margin of error is the maximum expected difference between a point estimate and the actual population parameter. The higher the MOE the more you expect a statistic to differ from the true parameter.

**Formula**: $\large MOE=Z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}$

Where:
* $Z_{1-\alpha/2}$ (the critical value) is the standard score $Z$ where the cumulative distribution function of that standard score $F(Z) = 1-\alpha/2$.

    Or: $Z=F^{-1}(1-\alpha/2)$

* $\alpha$ is the significance level, representing the fraction of the times, when the difference between the point estimate and the population parameter is greater than the margin of error.

* ${\frac{\sigma}{\sqrt{n}}}$ is  the standard deviation of a sampling distribution of the mean; the standard error.

#### Common critical Z-values:

```python
import pandas as pd
from scipy.stats import norm

conf = [90, 95, 99]
alphas = [1 - i / 100 for i in conf]
z = [norm.ppf(1-a/2) for a in alphas]
pd.DataFrame(data={"confidence level": conf, "critical value": z})
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>confidence level</th>
      <th>critical value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>90</td>
      <td>1.644854</td>
    </tr>
    <tr>
      <th>1</th>
      <td>95</td>
      <td>1.959964</td>
    </tr>
    <tr>
      <th>2</th>
      <td>99</td>
      <td>2.575829</td>
    </tr>
  </tbody>
</table>
</div>

Going by the Central Limit Theorem, sample means are normally distributed around the population mean. According to the empirical rule (68-95-99.7 rule), 95% of sample means are within approx. 2 standard errors from the population mean. In other words, one can say, with 95% confidence, that the population mean lies within approx. 2 standard errors from a sample mean. Such an interval is called a confidence interval and the MOE is the radius of that interval.

### Critical T-value

**Assumptions**:
1. The sample size is small (<30) or the population variance is unknown.
2. The sample is drawn from a normally distributed population.

**Formula**: $MOE=t_{1-\alpha/2,n-1}\frac{s}{\sqrt{n}}$

The critical T-value comes from a Student's T-distribution with $n-1$ degrees of freedom.

#### Critical T-values:

Sample size $n = 10$

```python
from scipy.stats import t

n = 10
conf = [90, 95, 99]
alphas = [1 - i / 100 for i in conf]
t_ = [t.ppf(1-a/2, n-1) for a in alphas]
pd.DataFrame(data={"confidence level": conf, "critical value": t_})
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>confidence level</th>
      <th>critical value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>90</td>
      <td>1.833113</td>
    </tr>
    <tr>
      <th>1</th>
      <td>95</td>
      <td>2.262157</td>
    </tr>
    <tr>
      <th>2</th>
      <td>99</td>
      <td>3.249836</td>
    </tr>
  </tbody>
</table>
</div>

A T-distribution takes sample size and the uncertainty regarding the population variance into account.

