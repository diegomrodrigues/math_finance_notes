   **6.1 Itô's Formula**
*   **Goal of Stochastic Calculus:**  To develop tools for working with stochastic processes and stochastic integrals in continuous time, using results that will be fundamental for the development of continuous time option pricing.
*   **Filtration for Stochastic Calculus:** The same definitions of right-continuity and P-completeness for the filtration.
*  **Time Parameter for Stochastic Calculus:** That time can be either bounded or not bounded.
*  **Basic Question in Stochastic Calculus:** The main question of this chapter: how to describe the process f(X) if X is a semimartingale and f is some suitable function.
*   **Chain Rule for Classical Calculus:** The classical chain rule for composing two differentiable functions, which is a source of intuition for the Itô formula.
*   **Limitation of Chain Rule for Stochastic Processes:** That the classical chain rule fails for processes that are not of finite variation and that the trajectories may not be differentiable, as in the case of Brownian Motion.
*   **Need for Itô's Formula:** That a new version of the chain rule must be formulated that includes a quadratic variation term.
*   **Connection with Semimartingales:** That the goal is to develop the Itô's formula for a semimartingale, using properties about its martingale and finite variation parts.
*   **Quadratic Variation of Finite Variation Processes:**  That finite variation processes have a quadratic variation equal to the sum of their jumps.
*   **Polarization of the Quadratic Variation:** That the covariation can be obtained by polarization of the quadratic variation.
*   **Quadratic Variation of a Semimartingale:** The quadratic variation of a general semimartingale as a function of the quadratic variation and jumps of the components.
* **Quadratic Variation of Continuous processes**: That the quadratic variation of continuous processes only depends on the local martingale part.
*   **Itô's Formula I (Continuous Case):** That for a continuous semimartingale X and a twice differentiable function f, the composition f(X) is again a semimartingale, and it also includes a term related to the quadratic variation.
*   **Itô's Formula II (General Case):**  The version of the formula for a general d dimensional process and with a sum for the jumps if X is not continuous.
*   **Interpretation of Itô's Formula:** That the main result adds a second order term from the quadratic variation of the stochastic process.
*   **Itô's Formula as an Extension of the Chain Rule:** That Itô's formula can be seen as an analytical result that extends the classical chain rule.
*  **Relaxation on Differentiability Conditions:** That relaxing the continuity conditions in x requires more assumptions on the differentiability on f, where the function f must be twice differentiable.
*   **Financial Relevance of Itô's Formula:**  How Itô's formula can be used to understand how derivatives react to changes of the underlying.
*  **Non-linearity of Itô's Formula:** That the Ito's formula shows that a simple linear approximation is not enough to describe the process.
*   **Taylor Expansion for Itô's Formula Proof:** That a Taylor expansion shows how the second order terms must be present in the formula.
*   **Formal Reasoning for Itô's Formula:**  The use of infinitesimal increments to obtain an intuition of the terms in the formula.
* **Formal and Informal proofs:** That the reasoning is not a formal proof but it gives intuition about the result, while the detailed proof requires extra mathematical arguments.
*  **Convergence of the quadratic variation for semimartingales:** That the quadratic variation of a semimartingale converges to the sum of squared jumps.
*   **Use of Weak Convergence:**  That this convergence implies the convergence of integrals, and that it also implies the dominated convergence theorem to achieve a rigorous proof.
*   **Example of Applying Itô's formula:** An example to verify Itô’s formula where a function f(x) = x² is applied to a Brownian motion.
*   **Relationship with previous chapters:** How this example relates to a result from a previous chapter on stochastic integrals.
*   **Itô's Formula and Stochastic Differential Equations (SDEs):**  That SDEs can be solved by applying Itô’s formula.
*   **Geometric Brownian Motion as an SDE:** How the GBM, which was given explicitly before, can be seen as the solution of an SDE, and Itô's formula is used to check the solution.
*   **Generalization of Itô’s Formula:** The generalization of the formula to a general real valued semimartingale with an exponential form.
*   **Stochastic Exponential:** The introduction of the stochastic exponential operator, and how the Itô formula is used to solve the related SDE.
*   **Itô's formula and the stochastic exponential:** How to use Ito's formula to show that the stochastic exponential solves a specific SDE.
*   **Stochastic Exponential and Jump Discontinuities:** That the stochastic exponential may become 0 or negative if the process has jumps and the properties of the jump are known.
* **Stochastic Integral in Terms of Itô's formula:** That stochastic integrals are a special case of semimartingales and that their process is described by Itô's formula.
*   **Linearity of Stochastic Integrals with Itô's Formula:** How to calculate and verify linearity of the stochastic integral using Itô's formula.
* **The Product Rule of Stochastic Calculus:** The importance of obtaining the product rule for stochastic integrals, which is directly implied by the Ito's formula.
*  **Example of a Product rule for stochastic calculus**: That the product rule for stochastic integrals is essential to study the Ito's Formula.
*   **Itô Process:** The definition of an Itô process as a solution of a stochastic differential equation, and that Itô's formula also applies to Itô processes.
*  **Multidimensional Itô Formula:** That Ito’s formula applies to both multidimensional semimartingales, vectors and matrix valued functions, and that they can be generalized with the appropriate dimensions.
*  **Example of a Ruin Problem:**  The application of Itô's formula to understand a ruin problem with a Brownian motion.
*   **Expectation of the Hitting Time and Process at Hitting Time:** How to use Ito's formula to obtain the expected value of the hitting time and of the BM at the hitting time.

   **6.2 Girsanov's Theorem**

*   **Invariance of Semimartingales Under Change of Measure:**  That the class of semimartingales is invariant under a C2 transformation or under a change of measure.
*   **Change of Measure in Continuous Time:** That the class of semimartingales is also invariant under equivalent change of probability measure.
*   **Local Equivalence:** The definition of two measures being locally equivalent which is a weaker condition than the global equivalence in finite horizon settings.
*  **Density Process Definition:** The definition of the density process as an RCLL version of a martingale, and the assumption that Z is positive almost surely.
*   **Density Process as a Supermartingale:** That the density process is always a supermartingale and that its infimum is also greater than 0.
*  **Predictability of 1/Z:** That if Z is a P-supermartingale, then 1/Z is predictable and locally bounded.
*   **Bayes' Formula for Continuous Time:** The transformation rule for conditional expectations that relates P and Q probabilities.
*   **Relationship Between Q and P Martingales:** That a process is a local Q-martingale if and only if its product with the density is a local P-martingale.
*   **Properties of Density Process:** That the density process can be used to switch from expectations under measure P to measure Q.
*   **Girsanov Theorem:** That if M is a local P-martingale, then there exist a process M that is a Q-martingale, where this process is obtained using the density process.
*  **Semimartingale invariance:** That if a process is a semimartingale under P, then it is a semimartingale under any equivalent probability measure Q.
*   **Key Idea for Girsanov Proof:** How the construction of the Q martingale M is done by adding the quadratic covariation term.
*   **Connection with the Stochastic Logarithm:**  That the density process can be seen as the stochastic exponential of a semimartingale.
*   **Girsanov with the stochastic exponential** That the stochastic logarithm can be used to write the density process as a local P-martingale, to show that a similar transformation results in a local Q martingale.
*   **Girsanov and Stochastic Logarithms:** That the new martingale in Girsanov's theorem is related with the change of the stochastic logarithm L.
* **Girsanov and Equivalent Martingale Measures:** That if we change the measure, we change the martingale property.
*  **Transforming P Brownian Motion to Q Brownian Motion**: That with the right density the P Brownian motion can be transformed to a Brownian motion under the equivalent probability measure Q with a drift term.
*   **Proof of Girsanov:** That the key is to write the martingale as a sum of a stochastic integral and finite variation parts and to use the Ito's formula to transform this to a Q martingale.

   **6.3 Itô's Representation Theorem**
*   **Goal of the Itô Representation Theorem:**  To provide a description of all possible martingales that can be constructed in a model generated by a Brownian motion.
*   **Itô Representation Theorem in Black-Scholes:** That this theorem is the mathematical explanation behind the completeness of the Black Scholes Model.
*   **Filtration Generated by Brownian Motion:**  The definition of the filtration generated by a Brownian motion and the augmentation with nullsets to get a complete filtration.
*   **Augmented Filtration:** That we add the class N of the null sets in order to have a P-complete filtration.
*  **Right Continuity of the filtration generated by Brownian Motion:** That the filtration generated by Brownian motion is right continuous as a consequence of the Strong Markov property.
*   **Itô's Representation Theorem:** That, under the generated filtration, every random variable that is integrable can be described using a constant term plus a stochastic integral of the Brownian motion.
* **Integrability Condition**: The integrability condition that is also necessary for the integrand in the stochastic integral.
*  **Martingale Property of the integral**: The need for the integrand to ensure that the stochastic integral is a martingale in the interval [0, ∞].
*   **Representation of Measurable Functions:**  That under the filtration generated by the Brownian motion, every measurable function can be seen as being described by a constant and a stochastic integral.
*   **Corollary 3.2:**  That every local martingale is described by the local martingale part of the integral with respect to the Brownian Motion.
* **Every Local Martingale in F^W is continuous:** A crucial result to characterize the martingales of Brownian motion.
* **Proof of Corollary 3.2:** That we prove that the localized version of a local martingale is also of the form of the Ito Representation Theorem.
*   **Dudley's Theorem:** A general result that describes all functions that are measurable with respect to an infinite time horizon filtration.
*   **Description of measurable random variables:** The statement that all random variables are given by a stochastic integral with respect to the Brownian motion, even if the information comes from an external filtration.
*   **Limitations of the Results:** That although the theorem is powerful, the integral has some limitations and caveats.
*   **Impossibility of Bounded Integrands:** That the integral from Dudley's Theorem can not be bounded from below and is typically not a true martingale.
*   **Non-Uniqueness of the Integrand:** That the integrand of the stochastic integral may not be unique in this case.
*  **Integrands and Finance:** That the integrands of this type of representation may be problematic for financial applications, as they are not well behaved.
* **Arbitrage Implication:** That having such a type of integrand would imply that it is possible to have an arbitrage with the same initial capital.
