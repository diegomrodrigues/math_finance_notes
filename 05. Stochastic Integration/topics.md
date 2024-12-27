   **5.1 Introduction to Stochastic Integration**
*   **Trading Gains in Discrete Time:** That the gains of a self-financing strategy in a discrete time model can be described by a stochastic integral.
*   **Stochastic Integral in Continuous Time:** That for an analogous theory in continuous time, it is essential to understand how to define a stochastic integral process in continuous time.
*   **Riemann Sums as an Approximation for Stochastic Integrals:** How to construct an integral via Riemann sums, and how to pass to the limit for a generic function.
*   **Path-Wise Integration of Stochastic Processes:** That the direct computation of the integral with a pathwise approach is insufficient and fails for some fundamental processes.
*   **Integrator with Finite Variation:** That the pathwise approach is valid only for functions with finite variation, and that it would exclude processes like Brownian motion.
*   **Different Approaches to Stochastic Integration:**  That depending on where the integrand is calculated in the interval, different integrals will be obtained: Itô, Forward and Stratonovich.
*   **Itô Integral for Finance:** That in financial applications, the Itô integral is the correct choice because the trading decisions must be taken before the price move.
*   **Stochastic Integrals with Pathwise definition**: That if the integrator and integrand match up well enough it may be possible to find an integral in the pathwise sense.
*   **Itô's Formula and w-wise definition**: That a w-wise approach may be useful in Itô's formula when the integrand is equal to a derivative, but fails when we try to fix an integrator.
*  **Difficulties in w-wise Stochastic Integrals:** That fixing an integrator and allowing many integrands, leads to problems.
*   **Stochastic Integral with respect to Local Martingale:** That the key idea is to construct the integral using a (real-valued) local martingale null at 0 and a predictable process with a suitable integrability property.
*   **Extension to Semimartingales:** How to extend this idea to the case of semimartingales in later sections.
*   **Real-valued Processes:** That for simplicity we are considering real-valued processes, but that it is also possible to generalize to higher dimensions.
*   **Necessary Changes in Higher Dimensions:** That we will comment on the necessary changes in higher dimensions later.
*   **Usual conditions for the filtration:** The usual assumption for the filtration of being right continuous and P-complete, which allows the use of the RCLL property for martingales.
* **Irrelevance of M at 0:** That as we will focus on integrals with the format of (a,b] we can ignore the values of the martingale at 0.
* **RCLL definition of jumps:** That the jump of a process is the difference between the value at that time and its left limit.

  **5.2 Construction of the Quadratic Variation**
*   **Brownian Motion as a Key Example:**  That the Brownian motion is a key example for understanding stochastic integration and quadratic variation.
*   **Quadratic Variation of Brownian Motion:** That the quadratic variation of Brownian motion is the process t.
*   **Quadratic Variation as a Pathwise Limit:**  That quadratic variation can be obtained as the limit of the sum of squared increments.
* **Quadratic Variation for a Local Martingale:**  That a similar result can be generalized for a general local martingale which is the key to constructing stochastic integrals.
*   **Existence of Optional Quadratic Variation [M]:** The result that for any local martingale M, there exists a unique RCLL increasing process null at 0 such that M2-[M] is also a local martingale.
*  **Properties of Quadratic Variation process**: That this process is always adapted, increasing and right-continuous with left limits.
*   **Quadratic Variation of M:** That it can be obtained via a limit of a sum of squared increments, and a sequence of partitions of the sample space.
*   **Square Integrable Martingales:** The definition of a square integrable martingale using the supremum in L^2 norm.
*   **Integrability of Quadratic Variation:** That the quadratic variation of a square-integrable martingale is also integrable.
* **Martingale Property of M²-[M]** The key result that the process obtained by taking the square of the martingale minus its quadratic variation is also a martingale.
*   **Proof of Theorem 1.1:**  That the result can be proven by using references from specialized books.
*   **Finite Variation of Quadratic Variation Process:** The property that quadratic variation is of finite variation and its paths are increasing.
*   **Pathwise Integral for Quadratic Variation:** That because quadratic variation is of finite variation, we can define a pathwise integral with it.
*   **Dependence of Partitions on M:**  That, in general, the sequence of partitions used to compute the quadratic variation can depend on the martingale M.
*   **Covariation Process:** That for two local martingales, it is possible to define their covariation process with polarization.
*  **Bilinearity of the covariation process:** That the operation of calculating the covariation is bilinear.
*   **Relationship between Covariation and Local Martingales:** The relationship between the covariation process and the local martingale property of the difference MN-[M,N].
*   **Predictable Compensator:** That a square integrable martingale can be decomposed into a martingale with a predictable compensator.
*   **Sharp Bracket Process:** The definition of the sharp bracket and its relationship with the quadratic variation process, where the sharp bracket is the predictable part of the quadratic variation.
*   **Predictability in Continuous Time:**  That we still need to define the meaning of predictability in continuous time.
*   **Localisation to Extend Results:**  That the results for square integrable martingales can be extended to locally square integrable martingales if we can understand the meaning of localization.
*   **Automatic Local Boundedness for Continuous Processes:** That continuous processes are automatically locally bounded, and the implication in integrability.
*   **Relationship between Quadratic Variation and Jumps:**  That if M is continuous, then its quadratic variation is also continuous.
*   **Quadratic Variation of Brownian Motion:** That the quadratic variation of Brownian motion is equal to the time.
* **Multidimensional case**: That the results about quadratic variation and covariation are also valid for multidimensional martingales.
*  **Difference between [M] and <M>:** That for any local martingale the quadratic variation always exists, but that the sharp bracket only exists if the process has extra integrability.
*   **Bounded Elementary Processes (bƐ):**  The definition of a set of processes that are piecewise constant and bounded with respect to time.
*   **Stochastic Integral with Elementary Processes:**  The definition of a stochastic integral with respect to an elementary process as the sum of increments multiplied by the value of the process.
*   **RCLL of the stochastic integral:** That the stochastic integral of an elementary process also has the property of being RCLL.
*   **Scalar Product for Multivariate Integrals:** That integrals between multivariate processes can be defined by simply using scalar products.
* **Square integrable martingale of stochastic integrals:** That the stochastic integral process H.M is a square integrable martingale.
*  **Isometry property of the stochastic integral:** That the variance of the stochastic integral is equal to the expected value of the quadratic variation of the integral.
*   **Finiteness of Integrals:** That the infinite time stochastic integrals are indeed finite because the processes are locally finite.
*   **Adaptedness and Square-Integrability of Stochastic Integrals:** That stochastic integrals are adapted, square-integrable, and that their increments are a martingale.
*  **Martingale Property of Integrals of Martingales:**  That if the integrator is a square-integrable martingale and the integrand is bounded, then the stochastic integral is a martingale.
*  **Relation between the Quadratic Variation of the integral and the quadratic variation of the integrator:** That the quadratic variation of the stochastic integral is the stochastic integral of the quadratic variation of the martingale.
*   **The process that gives a Martingale:** That (H.M)² − ∫H²d[M] is a martingale, as a fundamental property.

   **5.3 Extension to L2 Integrands**
*   **Processes as Random Variables:** How stochastic processes can be seen as random variables in the product space Ωx(0, ∞)
*   **Predictable Sigma-Field:** The definition of the predictable sigma field, as the field generated by all adapted left continuous processes.
*   **Predictable Processes:**  That a process is predictable if it is measurable with respect to the predictable sigma-field.
*   **Predictability of Elementary Processes:** The property that elementary processes are predictable.
*   **Infinite Measures in the Integral:** How the quadratic variation of a general martingale may not be a finite measure, and the implications for the integral.
*  **Definition of the measure P_M**: How to define the measure P_M which takes the martingale quadratic variation as its measure.
*   **Space of Square Integrable Integrands L²(M):**  The definition of a new space of integrands for a given martingale with a well defined norm.
* **Equivalence Classes**: The importance of noting that functions are equivalent in L2(M) if they are equivalent with respect to P_M.
*  **New formulation of Lemma 1.3**: How to rephrase the result in terms of a mapping from processes into square integrable martingales with the norm of L2(M).
*  **Linearity of the mapping H -> H.M**: That the mapping from integrable processes into stochastic integrals is linear.
*   **Isometry between L2(M) and Martingales:**  That the norm of the integral is the same as the norm of the integrand in the space L2(M), and how this isometry allows for extensions of the integral.
*  **Density of bE in L2(M)**: That bE is dense in L2(M), and that any function can be approached by elementary functions, which enables us to obtain a bigger space of functions that can be integrated.
*   **Existence of the Stochastic Integral:** That the stochastic integral can be extended to the space L2(M), by considering limits of elementary processes and that the isometry property is still satisfied.
*   **Importance of the Closure:**  That the closure of bƐ is used to construct the stochastic integral with more general functions.
* **Predictable vs Local:** That we are considering only predictable processes and local martingales.
*  **Definition of Local Martingales**: How to define a local martingale with the use of a sequence of stopping times.
*   **Locally Square Integrable Martingales:** The definition of the set of locally square-integrable martingales, which are locally bounded in L^2.
*   **Localized Class of Integrands:**  That the integrands are also localized so that the integrals can be well defined, and how to define this localized class.
*  **Use of Stopping Times:** How to use stopping times and localizing sequences to define new stochastic processes and integrals.
*   **Consistency of Localization:** How to ensure that the localized stochastic integral is consistent.
*   **Continuous Local Martingales:** The class of processes for which the above results simplify considerably, because they are also automatically locally bounded.
*   **Integrands for continuous processes:** That for continuous martingales we can describe explicitly the set of functions that are integrable with respect to this martingale.
*  **Properties of the stochastic integral:** That the stochastic integral is a local martingale with quadratic variation and other properties of this type.
*   **Jumps in Stochastic Integrals:** That if both the integrand and integrator are continuous then there are no jumps, but if not they can be explicitly calculated.
*   **Example of Stochastic Integral Calculation:** A step-by-step example of how the Itô integral of W with respect to W can be explicitly calculated using limits of Riemann sums.
*   **Correction Term in the Itô Integral:** The observation that the correction term of the stochastic integral is related to the quadratic variation of Brownian motion.
*   **Exercise for Stratonovich and Backward Integrals:**  That there also exist other integrals and that it is important to analyze their properties.
* **Exercise about Integrable Martingales**: That stochastic integrals are also martingales when the integrands are bounded and predictable.
* **Exercise about Quadratic Variation with stopping times:** That the quadratic variation can be calculated by stopping at certain times.

   **5.4 Extension to Semimartingales**

*   **Semimartingales as Integrators:**  That the goal is to extend the integral to the case of a more general class of integrators that includes local martingales and functions with finite variation.
*   **Decomposition of Semimartingales:** That a semimartingale is a process that can be decomposed into a local martingale and a finite variation process.
*   **Special Semimartingales:** That in the special case the decomposition must be a predictable variation process.
*   **Canonical Decomposition:**  The property that the special decomposition of a process is unique.
* **Continuous Semimartingales:** That a continuous semimartingale has both the martingale and finite variation parts being continuous and predictable.
*  **Optional quadratic variation for semimartingales:** The definition of the quadratic variation of a semimartingale.
*   **Quadratic Variation and Jumps:** That the quadratic variation of a semimartingale takes jumps into account.
*   **Stochastic Integral for Semimartingales:** The definition of the stochastic integral for semimartingales by adding the stochastic integral of the martingale and the pathwise integral of the finite variation part.
*   **Well-Definedness of the Integral:** That the stochastic integral for a semimartingale must be well defined.
*   **Properties of Stochastic Integrals with respect to Semimartingales:** That many of the previous properties of the stochastic integrals remain true in this more general context.
*   **Loss of Isometry Property:**  That when integrating with respect to a semimartingale we lose the isometry property.
*  **Other properties**: That the linearity, associativity and stopping property still remain true in this context.
*   **Jumps in Semimartingale Integrals:**  That the jumps of a stochastic integral of a semimartingale is given by the jump of the integrator multiplied by the integrand.
*   **Dominated Convergence Theorem for Stochastic Integrals:**  The property that allows for a controlled passage to the limit in stochastic integrals.
* **UCP property:** The type of convergence in probability used in this section.
*   **Continuity of Stochastic Integrals with Respect to Semimartingales:**  That stochastic integration has a continuity property with respect to semimartingales.
*   **Semimartingale as Natural Integrators:** That semimartingales are a very natural class of integrators, given that many properties and formulas can be extended to them.
*   **Itô's Formula for Semimartingales:**  That if a function is twice differentiable, its composition with a semimartingale is also a semimartingale, which is a result that will be seen later.
*   **Semimartingales under Equivalent Measures:**  That a semimartingale will remain a semimartingale under equivalent measures, which will be related with Girsanov's theorem.
*   **Semimartingales as Natural Integrators:** That if a mapping on elementary functions has a continuity property, then the integrator must be a semimartingale, meaning that they are a very natural class.
*   **Semimartingales for Discounted Asset Prices:**  That discounted asset prices are a good candidate to be represented as semimartingales in financial markets, a key for using the models of this chapter.
*   **Semimartingales and Transaction Costs:** That in models where semimartingales are not valid there will be arbitrage, which is avoided in frictionless markets.
* **Limitations of the Theory**: That this approach only applies for locally bounded integrands and that further studies are necessary for more general functions.
* **More possible integrands**: How to introduce a class L(X) for which the stochastic integral of the semimartingale X is well defined even for more general integrands.
* **Advanced techniques**: That constructing a class of larger integrands involves complex techniques of stochastic calculus.
