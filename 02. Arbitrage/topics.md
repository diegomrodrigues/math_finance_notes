**2. Arbitrage and Martingale Measures**

   **2.1 Arbitrage Concepts**
*   **Arbitrage Opportunity:** The ability to create a risk-free profit with zero initial investment through a specific trading strategy, and the several forms of arbitrage.
*   **Arbitrage Opportunity (First Kind):**  A strategy that has a nonnegative final value, and has a positive probability of being strictly positive, this is the most common notion of arbitrage.
*   **Arbitrage Opportunity (Second Kind):** A strategy that has a nonpositive initial investment and a positive probability of having a negative final investment.
*  **(NA+) Condition:** The statement that it is impossible to produce something out of nothing using 0-admissible strategies.
*  **(NA') Condition:** The statement that it is impossible to produce something out of nothing using any self-financing strategy.
*   **Equivalence of Arbitrage Concepts (in finite discrete time):** That the different concepts of arbitrage and their limitations are equivalent in discrete time models, but may differ in continuous or infinite-horizon setups.
*   **Example of Arbitrage:** A concrete example where an arbitrage opportunity arises when an asset has a positive probability of decreasing, and the consequences in terms of an explicit strategy.
*   **Space of Nonnegative Variables (L+(G)):** The definition of a space of nonnegative random variables which are measurable with respect to a certain σ-algebra, a core tool for analyzing the arbitrage conditions.
* **Equivalence relation of the space of measurable variables**: How to see that two random variables are the same if they are equal P-a.s. in the definition of L+.
*   **Arbitrage-free condition:** The state of the model where there are no available strategies that can generate profits from nothing.
* **Parametrization of self-financing strategies:** The reference to proposition 1.2.3 regarding the relationship between an initial investment, a risky asset strategy and the self financing strategy, and its consequences in defining no-arbitrage.
*   **Geometric Interpretation of No-Arbitrage:** The interpretation of the no-arbitrage conditions by observing the intersection between the set of nonnegative final wealths and the set of the gains of the strategies.
*   **Equivalent Probability Measures (Q ≈ P):** The concept that two measures may differ in the assignment of probabilities, but agree on what are the impossible events.
*   **Nullsets:** The concept of sets with a probability of 0 which defines when two measures are equivalent.
*   **Equivalence in the Multinomial Model:** The characterization of equivalent measures in the multinomial model by relating the positivity of their transition probabilities.
*   **Lemma 1.2 (Martingale Measure Implies No Arbitrage):** The theorem that establishes that if an equivalent martingale measure exists then no arbitrage is possible.
*   **Relationship between Martingales and Arbitrage-Free Markets:**  How the existence of a martingale under an equivalent probability measure implies the absense of arbitrage.

   **2.2 Remarks on the Martingale Implies No Arbitrage Lemma**
*   **Local Martingale in Lemma 1.2:** The notion that a local martingale is enough to guarantee the no-arbitrage condition.
*   **Alternative Proof:** How to achieve an alternative proof of the lemma based on Fatou's lemma.
*  **Supermartingales and the Proof of the Lemma:** How to use a supermartingale and localization arguments to prove the result.
*   **Complete Proof:** How to give a proof of the lemma based only on the already proven results of the previous chapter.
*  **Boundedness of the predictable part and the Martingale Property:** How the predictable process must be bounded for the integral to be a Martingale and how it is used in the proof.
*   **Fatou's Lemma and the Proof:** The use of Fatou's Lemma as a way to go from bounded processes to the limit process and how this is required to prove the result.
*   **Continuous Time Complications:** How the usage of local martingales requires specific arguments in continuous time.
*   **Example:** How to calculate the conditions for the existence of a martingale in the multinomial model.
*   **One-step transition probabilities**: The application of the general theory to the case of the multinomial model.
*   **I.I.D. returns and the Martingale Measure:** The remark that the martingale measure may change the i.i.d. condition of the model.
*   **Corollaries 1.4 and 1.5:** That the lemma is a step towards proving the existence of an arbitrage, but it has an associated condition as demonstrated in the previous Corollaries.

   **2.3 The Fundamental Theorem of Asset Pricing**
*   **Equivalent Martingale Measure (EMM):** The probability measure equivalent to P under which S is a martingale, and how this is related to arbitrage and the FTAP.
*   **Equivalent Local Martingale Measure (ELMM):** The generalization of EMM to the case of local martingales.
*   **Set of EMMs (IPe(S)):**  The set of all possible EMMs and their properties.
*  **The fundamental Theorem of Asset Pricing:** The central result of this chapter stating that if and only if there is no arbitrage in a model, then an Equivalent Martingale Measure exists.
*   **Significance of the Theorem:**  That the FTAP translates an economic condition into a mathematical and probabilistic property, and how it opens the door to martingale theory.
*  **Gambling Theory and Martingales:** The relation between martingale theory and the FTAP, specifically regarding the impossibility of winning from betting on a martingale.
*   **Integrability:**  That the price process must be integrable for the measure Q in the FTAP, and that such integrability can be found with an equivalent probability measure.
*   **Proof Difficulty for Infinite Spaces:** The remark that proving the FTAP for general (infinite) sample spaces is more complex.
*   **Geometric Idea of the Proof:** That the no arbitrage condition translates to a separation between two sets, and how the normal vector of this separation gives the density of the martingale measure.
*   **Proof in Finite Sample Spaces:** The specific case where the sample space is finite, which allows to obtain an explicit argument using the separation of convex sets.
*   **Separation Theorem for convex sets in IR^n**: That when two convex sets do not intersect, we can find an hyperplane that separates the two sets.
*   **Convexity of EMMs:** That the set of EMMs for a given model is a convex set.
*   **Uniqueness of EMMs:** That the set of EMMs is either empty, or contains one element, or contains uncountably many elements.
*  **Random Variables and Atoms:** The use of Atoms of a Sigma algebra to define the linear and finite structure of the space of variables in finite sample spaces.
*   **Normal vector to the hyperplane:** How to see that the normal vector of the hyperplane that separates the gains and nonnegative variables can be used to find the EMM.
*   **Specific formula of the process Z:** How the coefficients of the normal vector can be used to construct a density that guarantees the martingale property of a given process.
*   **Generalization to Infinite Dimensions:** That the result can be generalized to infinite dimensional spaces but it requires more advanced arguments.
*   **NFLVR (no free lunch with vanishing risk):** The more general version of the no arbitrage property that is required in continuous time.
*   **Limitations of the FTAP:** The dependence of the FTAP on the basic assumptions such as the existence of frictionless markets and small investors.
*   **Corollaries 2.2 and 2.3:** The application of the FTAP to the multinomial and binomial models.

  **2.4 Equivalent (Martingale) Measures**
*   **Role of EMMs:** The general importance of EMMs in mathematical finance.
*   **Option Pricing and Hedging:** The importance of EMMs in the areas of option pricing and hedging, which will be explored in later chapters.
*   **Relationship between P and Q:** How to relate computations and probabilistic properties under P and under Q in the case of equivalent measures.
*   **Radon-Nikodým Theorem:** The main result that guarantees the existence of a density between two equivalent measures, and how to compute the equivalent probabilities using this density.
*  **Radon-Nikodym Derivative:** The random variable that is the density between two equivalent probability measures.
*   **Relationship between P and Q expectations**: That the Radon-Nikodym derivative can be used to compute expectations from one measure to another one.
*   **Density Process (Z):** The definition of a martingale that helps to switch from expectations under measure P to measure Q.
*   **Strict Positivity of Density Process:** How to prove the strictly positivity of the density process using the equivalence of measures.
*   **Bayes Formula for Conditional Expectations:** The transformation rule for conditional expectations that relates the different expectations under P and Q.
*  **Link between Q-Martingales and P-Martingales**: How to use the process Z to switch from martingales in Q to martingales in P and vice-versa.
*  **Process D:** The definition of the process D that allows to recover the density process Z given that we have an initial value and that D has the martingale property.
* **One-step conditional densities**: How to see that the process D plays the role of the one step conditional densities of the measure Q given the measure P.
* **Parametrization of EMMs:** How to parametrize an EMM based on the processes Z and D.
*   **Integrability Condition**: How the EMM choice must also guarantee the integrability of the price process.
*   **Choice for Zo:** The simplest case where the measure Q coincides with P at the initial time.
*   **EMM for models with i.i.d. returns:** The definition of the EMM for the specific case of i.i.d. returns, and how the process D depends on the random returns Y.
*  **Specific formula for the Dk process:** How to find the process Dk given that we have i.i.d. returns and a predictable structure for Dk.
* **Simplifications for the function gk**: How we can simplify the function gk from the fact that the returns are i.i.d..
*   **EMMs for Discrete Random Variables:** The discussion on how to find the EMMs for the case of discrete random returns, and the implication in the set of possible probabilities.
*  **EMMs for continuous random variables:** The specific example of how to find a EMM for a process with normal returns.
