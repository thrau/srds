Simple Random Distribution Sampling
===================================

SRDS is mainly a wrapper around scipy's statistical functions
([scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html)).
It makes it easier to sample from parameterized distributions and provides tools that accelerate random sampling.

## Examples

### Truncation or rejection sampling

srds adds several classes that make it easier to utilize scipy statistical distributions.
To sample from a log-normal distribution with `σ = 0.25`, but truncate at `0.5` and `2`, the `BoundRejectionSampler`
helps:

```python
from srds import ParameterizedDistribution as PDist, BoundRejectionSampler

dist = PDist.lognorm(0.25)
sampler = BoundRejectionSampler(dist, 0.5, 2)

x = sampler.sample(10)
```

### Fast sampling of single values

calling `dist.rvs` on a scipy statistical distribution is computationally expensive. This is problematic for code that
does something like:

```python
# will be slow (calls dist.rvs 10000 times)
for i in range(10000):
    x = dist.sample()
    # ...
``` 

srds provides a `BufferedSampler` that draws a larger sample from a distribution, and subsequently returns from that
sample.

```python
from srds import BufferedSampler

dist = BufferedSampler(dist)

# will be much faster! (calls dist.rvs only 10 times with a sample size of 1k)
for i in range(10000):
    x = dist.sample()
    # ...
``` 

### Sampling from populations

You can use the `PopulationSampler` to draw from a discrete set, and also bias the sampling with weights.
```python
from srds import PopulationSampler

sampler = PopulationSampler(['a', 'b', 'c'], [8, 1, 1])
sampler.sample() # will return 'a' 8 out of 10 times on average
sampler.sample(10) # returns a list containing items from ['a', 'b', 'c'] in random order
```
