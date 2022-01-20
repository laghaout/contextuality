# Framework for simulating contextuality experiments

### Scientific background

Classically, physical systems are assumed to be in a well-defined state, i.e., a collection *__a__* of *N* real attributes *a~n~* that are independent of measurement (e.g., mass, position, momentum, etc.). This so-called *ontic* state, which can be represented as a vector of those attributes, is drawn stochastically from an ensemble, i.e., from the set of all possible *K* combinations of the attributes. (For example, if the system can be fully described by three binary attributes, then there are *K* = 2<sup>3</sup> = 8 possible combinations.) When taking into account the epistemological ignorance of the observer, the most complete representation of a physical system is therefore a convex combination of those *K* possible ontic states where each *k*<sup>th</sup> combination is associated with a probability *p*<sup>(k)</sup>. Therefore, over several measurement runs, the mean values of the attributes can be assembled into an *N*-dimensional measurement vector *__μ__* whose *n*<sup>th</sup> component is *μ<sub>n</sub>* = Σ<sub>k</sub> *p*<sup>(k)</sup> *a*<sub>n</sub><sup>(k)</sup>. In other words, if one were to concatenate all the *K* possibles ontic states *__a<sup>(k)</sup>__* into an *N×K* matrix __A__, then *__μ__* = __A__ *__p__*.

In general, however, measurements on the system are not necessarily revealing the individual attributes, but are rather obtained from logical combinations thereof. E.g., instead of measuring *a<sub>n</sub>* or *a<sub>m</sub>* directly, one could measure their product *a<sub>n</sub>×a<sub>m</sub>*. In those cases, the measurement vector *μ* doesn't directly reflect the ontic attributes *a<sub>n</sub>*, but rather lives in a projected space of reduced dimensions compared to that supported by the *N×K* collection of ontic states.[^reduced_space] Classically, one should be able to reconstruct *μ* from some convex combination of the ontic states. If that isn't the case, then one says that *μ* is an unreal measurement vector. Contextuality, and concomitantly violations of realism, arise whenever one demonstrates that such a *μ* lies outside the (convex) reach of the ontic states. Algebraically, the violation of realism is quantified as the smallest distance *D* between *μ* and the hull spanned by all possible convex combinations obtained from the ontic states.

### Object-oriented framework

Computationally, the problem of contextuality consists of defining an ontology, i.e., a realm of (stochastic yet classical) possibilities which are algebraically defined by a convex hull, the so-called *real* hull. The remaining polytope of whatever vectors cannot be supported by the real hull, is therefore supported by a complementary *unreal* hull. If one obtains a measurement on this latter hull, one is said to have violated realism. Let us represent such an ontology by a Python class `Ontology` defined in the module `ontology.py`. 

Computationally, the problem of determining whether a measurement vector is unreal (i.e., lives outside the real hull of *N* ontic states) can be broken down into the following sequence of operations:

1. In the function `self.define_ontic()`, assemble the ensemble of *K* *N*-dimensional ontic states into an *N×K* matrix `self.ontic`.
2. In the function `self.compute_derived()`, compute the logical derivation of ontic states (e.g., products thereof) and assemble them into the matrix `self.derived` which supports the real hull.
3. In the function `self.compute_hulls()`, compute the real and unreal hulls in function `self.compute_hulls()` and store them in the `SimpleNamespace`s `self.hulls.{real, unreal}.hull` along with their supports `self.hulls.{real, unreal}.support`.
4. Whenever provided with a measurement vector __μ__, invoke the function `self.violation(**mu)` to determine its violation, namely its distance *D* to the real hull, the closest point on the real hull, the probability vector __*p*__ of the closest point on the hull, as well as, optionally, the number of  standard errors of __μ__ to the real hull. (The latter is only provided if __μ__ is specified along with its standard deviation.)

For further documentiation, please refer to the comments in the code.

The [Peres-Mermin square](https://doi.org/10.1103/PhysRevLett.65.3373) is an example of the aforementioned ontology and it used to showcase it in the default executions of `main.py`. The whole framework is however customizable to any ontology which inherits from the `Ontology` parent class.

### References

* Altay Dikme, Nicolas Reichel, Amine Laghaout, Gunnar Björk, *Measuring the Mermin-Peres magic square using an online quantum computer*, [arXiv:2009.10751 (2020)](https://arxiv.org/abs/2009.10751)

[^reduced_space]: For example, although two bits live in the four-dimensional space {[0, 0], [0, 1], [1, 0], [1, 1]}, their product only lives in the two-dimensional space {0, 1}, whereby the first three "ontic" states map to 0 and the last maps to 1.

