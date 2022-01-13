# Contextuality violations

### Scientific background

Classically, physical systems are assumed to be in a well-defined state, i.e., a collection of `N` real attributes that are independent of measurement (e.g., mass, position, momentum, etc.). This so-called ontic state, which can be represented vectorially as an ordered array of those attributes, is drawn stochastically from an ensemble of ontic states, i.e., from the set of all possible `K` combinations of the attributes. (For example, if the system can be fully desribed by three binary attributes, then there are `K = 2^3 = 8` possible combinations.) When taking into account the epistemological ignorance of the observer, the most complete representation of a physical system is therefore a convex combination of those `K` possible ontic states.

In general, however, measurements on the system are not necessarily revealing the individual attributes, but are rather obtained from logical combinations thereof such as their products. In those cases, the measurement vector `μ` doesn't directly reflect the ontic attributes, but rather lives in a projected space of smaller dimensions than that supported by the `N×K` collection of ontic states. Classically, one should be able to reconstruct `μ` from some convex combination of the ontic states. If that isn't the case, then one says that `μ` is an unreal measurement vector. Contextuality, and concomitantly, violations of realism, arise whenever one demonstrates such a `μ` lies outside the reach of the ontic states. Algebraically, the violation of realism, is quantified as the smallest distance `D` between `μ` and the hull spanned by all possible convex combinations of the ontic states.

### Object-oriented framework

Computationally, the problem of determining whether a measurement vector is unreal (i.e., lives outside the real hull of `N` ontic states) can be broken down into the following steps:

1. Assemble the ensemble of `N` `K`-dimensional ontic states into an `N×K` matrix `A`.

### References

* Altay Dikme, Nicolas Reichel, Amine Laghaout, Gunnar Björk, Measuring the Mermin-Peres magic square using an online quantum computer, [arXiv:2009.10751 (2020)](https://arxiv.org/abs/2009.10751)

