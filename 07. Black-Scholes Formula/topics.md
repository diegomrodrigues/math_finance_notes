   **7.1 The Black-Scholes Model**
* **Goal of the Chapter:** The final goal is to combine ideas from the discrete time framework with the continuous time tools developed in the previous chapters, to construct the Black-Scholes formula.

* **Emphasis on Methodology:** That the goal of this chapter is to show the steps to construct the formula, and not the formula itself.

* **Black-Scholes Model:** That this model is the continuous-time analog of the Cox-Ross-Rubinstein binomial model, and how to see its relation with the binomial model.

* **Limitations of the Model:**  That the model is too simple to be realistic, but it provides a starting point and allows for explicit calculations.

* **Financial Market Model:** That the model starts with a fixed time horizon T, a sample space, and a Brownian motion.

* **Filtration for the Black-Scholes Model:** That the model uses the filtration generated by the Brownian motion, with nullsets to satisfy the usual conditions.

* **Bank Account:** The definition of a risk-free asset, that has a continuous interest rate r and the price at time t is given by exp(rt)

* **Risky Asset:** The definition of the risky asset or stock whose price is determined by two parameters: drift μ and volatility σ, where the price change has a geometric form.

* **Undiscounted Prices:** How to define the risky asset price in its original form, where its volatility is driven by a BM.

* **Application of Itô's Formula:**  That Itô's formula is directly used to show how the SDE of the price processes are obtained.

* **Differential notation:** How to write the dynamics of the prices with differential notations, for both the riskless asset and the risky one.

* **Interpretation of parameters**: How to see that the parameter r represents the growth rate of the bank account, while the other parameters influence the behavior of the stock.

* **Drift and Volatility:** The definition of the drift and volatility as a result of the SDE of the risky asset, which models its instantaneous mean and variance.

* **Continuous-Time Analogue of the CRR model:** How to relate the model as the continuous analogue of the CRR model, where the prices have random fluctuations in the continuous time model.

* **Discounted Prices:** The concept of moving from the original prices to the prices discounted with the riskless asset, to get a zero interest market.

* **Representation of the Discounted Price:** The formula to write the discounted stock price in terms of a stochastic exponential of the Brownian Motion.

* **SDE for the Discounted Price:** The SDE for the discounted stock price, which does not have the interest rate term.

* **Quadratic Variation of Discounted Stock Price:** The expression for the quadratic variation of the stock price which is used later.

*   **Filtration Generated by the Assets:**  That under this simple model the filtration generated by the Brownian motion is equivalent to the filtration generated by the price processes.

   **7.2 Equivalent Martingale Measure**
   
* **Need for an Equivalent Martingale Measure:** That it is important to find the Equivalent Martingale Measure for the discounted stock price process, as it was for the discrete case.

* **Rewriting the SDE of the Discounted Price:** That the SDE of the discounted price can be rewritten in terms of a drift-less stochastic integral of a Brownian motion, by a specific transformation.

* **The Transformed Brownian Motion W*:** The definition of the transformed Brownian motion, that includes a specific parameter related to the Sharpe ratio or Market price of risk.

* **Instantaneous Market Price of Risk (λ):** The definition of the term that multiplies the transformed Brownian motion, which represents the market price of risk.

* **Girsanov's Theorem and the Transformed Brownian Motion:**  How to use Girsanov's theorem to change the probability measure and to show that the transformed Brownian motion is indeed a BM with respect to the new measure.

* **Equivalent Martingale Measure (Q*) for Black-Scholes Model:** How to define a new measure Q*, such that the transformed Brownian motion is a Brownian motion under this new measure.

* **Density Process for Black-Scholes Model:** How the density process of the new probability measure Q* with respect to P is related with the instantaneous market price of risk.

* **Relationship between the martingales under different measures:** That the density process has also the stochastic exponential form with respect to the market price of risk.

* **Discounted Stock Price as a Q* Martingale:**  That the discounted price is a martingale with respect to the new measure and the transformation of the Brownian Motion.

* **Unique ELMM for Black Scholes**: That the constructed martingale measure for the discounted stock price is the unique EMM.

* **Pricing with Equivalent Martingale Measures:** The definition of an arbitrage-free market and its connection with the existence of an EMM.

* **Self financing strategies with stochastic integrals:** How self financing strategies can be described in this continuous time setting.

* **Risk Neutral Valuation:** How to use the equivalent martingale measure to price the option based on the expectation of the payoff under Q*.

* **Characterization of ELMMs:**  That every Equivalent Martingale Measure can be described by a particular transformation of the Brownian Motion.

* **Itô's Representation Theorem and Unique ELMM:** That the uniqueness of the ELMM is given by Itô's representation Theorem which allows us to rewrite the density in terms of an integral of the Brownian motion.

* **Representation of a local P-martingale**: That every P-martingale can be described by an Ito Integral, which is needed for the construction of an equivalent measure.

* **Replication Strategies with Brownian Motion:** That every option has a replicating strategy that can be expressed as the integral with respect to a Brownian Motion, even with an equivalent probability measure.

* **Constraints on Integrability:**  That the integrability of the process must be assumed to show the existence of a unique EMM.

* **Necessity of the Filtration:** The fact that to show the unique ELMM we need that the filtration is generated by the Brownian Motion, and not by the asset prices.

* **Restrictions in General Models:** That if we add extra randomness on top of the Brownian motion the Ito representation theorem will be limited, and will have some extra difficulties.

* **Financial Relevance of Itô's Representation Theorem:** That in financial models, the natural filtration would be the one generated by prices, but that this filtration is difficult to describe.

* **Limitations in Arbitrage-Free Arguments:**  That the no arbitrage condition only gives a unique price process and a self-financing strategy if the value of the option is bounded.

* **Importance of self-financing for the price**: That the price should come from the unique self-financing strategy to avoid arbitrage.

   **7.3 Markovian Payoffs and PDEs**
   
* **PDE Approach to Option Pricing:** The goal of describing an alternative way of pricing the options, using the properties of the related Partial Differential Equations.

* **Markovian Setting for Option Pricing:** That this PDE approach is valid for situations where the prices are markovian.

* **Payoff as a Function of Terminal Asset Price:**  That for the PDE approach, we must be able to write the payoff as a function of the price at maturity.

* **European Call Option**: That this approach can be applied to the specific case of a european call option on the asset with a discounted strike K.

* **Value Process as a Function of Time and Asset Price:**  That the option price process can be seen as a function of time and asset price by the use of conditional expectations.

* **Formula for the value of the option** The explicit formula of the conditional expectation, using the fact that W*t-W*s is independent of F_t.

* **Structure of the Value Process:** That the value of the option has a very specific structure given by a function that depends on the current price of the underlying.

* **Computation with Normal Distributions:** How to explicitly compute the formula using standard properties of normal random variables.

* **The Black-Scholes Formula:** The explicit formula of the Black Scholes price of the call option, which only depends on the price of the underlying, time, interest rate, volatility and strike.

* **Absence of the Drift term in the formula:** That in the expression of the price formula, the drift term is missing as in the CRR model.

* **Replicating Strategy:** The definition of the replicating strategy with the derivative of the value function with respect to the price of the asset.

* **Relation between replicating strategy and the derivative of the price**: The relationship between the replicating strategy and the first order derivative, and its interpretation as the hedge ratio.

* **Smoothness Conditions:**  That it is essential that the function v is smooth in order to apply the Ito's Formula and obtain a Partial Differential Equation.

* **Partial Derivatives of the Value Function:** That the function v, and therefore the price of the option, has partial derivatives with respect to time and price.

* **Application of Ito's Formula to the Option Value:** That to show the specific form of the partial differential equation it is important to use the Ito's Formula with the function v and the stochastic price process S.

* **Vanishing drift term in the Itô Formula**: That the drift term of the resulting process is equal to 0 and that this condition gives the form of the Partial Differential equation.

* **Black-Scholes Partial Differential Equation:** That the price of the option must satisfy a second order partial differential equation.

* **Black-Scholes Boundary Condition:** That this PDE has a specific boundary condition at the time of maturity.

* **The PDE Approach to Option Pricing:** That the option price can be numerically computed by solving the related PDE.

* **Solution of the PDE by Convolutions:**  That the PDE is solved by a convolution which implies that the solution has to be smooth.

* **Solution of the PDE:** How to obtain the solution of the PDE by a convolution of a function with a normal distribution.

* **Verification of the Solution:** That to prove that the solution is correct the analytical properties of the solution must be calculated.

* **Generality of the Approach:** The PDE approach is not specific to the Black-Scholes model, but rather to all the models with a Markov property, where the condition expectation depends on the current state of the model.

* **Martingale Property and the Generator:**  That the Martingale Property is translated into the generator of the underlying process must vanish.

* **Diffusion Processes and PDEs:** That for diffusion processes the generator is a second-order partial differential operator.

* **Lévy Processes and PIDEs:** That for Lévy processes the generator has integral terms, hence we obtain PIDEs

* **Technicalities of PDE Approaches:** That many technical conditions need to be checked to guarantee the properties of the solutions, such as regularity, existence and uniqueness.

* **The Undiscounted Payoff:** The formulation of the call option in terms of undiscounted prices.

* **The relationship between undiscounted and discounted prices**: That this is given by a simple formula and that it affects the boundary conditions of the PDE.

* **Relationship with Undiscounted Quantities:** How to relate all the calculations of the prices with their undiscounted version.

* **PDE for Undiscounted Quantities:** The PDE for the undiscounted option price, where the interest rate term appears directly.

* **Greek Letters:**  The definition of different sensitivities of the option price, which include Delta, Gamma, Rho, Vega, Charm and Volga.

*  **Greek letters interpretation:** How to see that each Greek letter is defined as a different partial derivative of the option price, that captures different properties about its behavior.

  **7.4 Analysis and Limitations**

* **Limit derivation of the Black-Scholes formula:** How the Black-Scholes formula can be obtained as a limiting case of a binomial model and the use of Donsker's theorem or the Central Limit Theorem.

* **Critique of the Limiting Derivation:**  That while this limit-type proof is simple, it is not completely satisfactory.

* **Absence of Structural Properties:**  That the direct use of Ito’s representation theorem to find the Black-Scholes formula is superior because the methodology of the formula is more important than the formula itself.

* **Limitations of the Black-Scholes Model:** That the Black-Scholes model is oversimplified by assuming parameters as constant and that the use of stochastic or price-dependent processes may lead to more complex models.

* **Existence of Solutions for Stochastic Models:** That if the coefficients are dependent on prices then the existence of solutions is not always clear.

* **Filtration and extra randomness:** That if the volatility depends on another process, we may have to use a larger filtration for the model.

* **Itô Representation Theorem Limitations in Stochastic Volatility Models:** That the Itô’s representation theorem may not always be available for models that depend on extra random noise.

* **Practical Difficulties with Price Filtrations:** That the most natural filtration is the one generated by prices, but that it is difficult to work with.

* **Arbitrage-Free Valuation in Continuous Time:** That in continuous time, we do not have an arbitrage in the traditional sense but instead in a slightly more complex and subtle way.

* **Importance of admissibility** That, if the options are not bounded from above then the replicating strategy is also not admissible.

*   **Self-Financing and Admissibility:** That in continuous time, the concept of self financing and admissibility are not exactly the same, while in discrete time they are.
