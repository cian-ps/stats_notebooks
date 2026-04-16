## Standard Error

The *Standard Error* of a statistic is the standard deviation of its sampling distribution.
The Standard Error of the sample mean describes how accurately a sample mean represents the entire population mean.

**Formula**: $\sigma_{\bar{x}}=\frac{\sigma}{\sqrt{n}}$

$\bar{X}\sim\mathcal{N}(\mu,\frac{\sigma^2}{n})$

$\sigma_{\bar{X}}=\sqrt{\frac{\sigma^2}{n}}=\frac{\sigma}{\sqrt{n}}$

The sample mean $\bar{X}$ is expected to be close the population mean if there are a large number of observations per sample. In other words, the standard error decreases as the sample size increases.

### Estimate

$\widehat{\sigma_{\bar{x}}}\approx\frac{s}{\sqrt{n}}$

The population standard deviation ($\sigma$) is seldom known, therefore the standard error is usually estimated by replacing $\sigma$ with the standard deviation of the sample ($s$).

---

To avoid confusion, it's important to distinguish between:

* standard deviation of the population ($\sigma$)
* standard deviation of the sample ($s$)
* standard deviation of the sample mean, which is the standard error ($\sigma_{\bar{x}}$)
* the estimate of the standard error ($\widehat{\sigma_{\bar{x}}}$)

### Example

```python
import numpy as np

def sample(data, n):
    return data[:n]

population = np.random.randint(0,1000,1000)
sigma = np.std(population)

for n in [10, 50, 100]:
    print(f"""n = {n}
population mean: {np.mean(population)}
sample mean: {np.mean(sample(population, n))}
standard error: {sigma / np.sqrt(n)}
""")
```

