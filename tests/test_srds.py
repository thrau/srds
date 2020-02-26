from unittest import TestCase

from srds import ParameterizedDistribution as PDist, BoundRejectionSampler, PopulationSampler


class TestSampling(TestCase):
    def test_sampling(self):
        # FIXME: bogotest, extend tests!
        dist = PDist.lognorm(0.25)
        sampler = BoundRejectionSampler(dist, 0.5, 2)

        x = sampler.sample(10000)
        self.assertGreater(x.min(), 0.5)
        self.assertLess(x.max(), 2)

    def test_population_sampler(self):
        sampler = PopulationSampler(['a', 'b', 'c'], [10, 1, 1])

        x = sampler.sample(10)
        print(x)
