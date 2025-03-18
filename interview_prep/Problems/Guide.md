# Quantitative Trading Techinical Test Preparation Guide

## Combinatorics

### Key Formulas and Theorems

- **Permutations** (ordered arrangements): $P(n,k) = \frac{n!}{(n-k)!}$
- **Combinations** (unordered selections): $C(n,k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$
- **Binomial Theorem**: $(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$
- **Stars and Bars**: Number of ways to put $n$ indistinguishable objects into $k$ distinguishable groups: $\binom{n+k-1}{k-1}$
- **Multinomial Coefficient**: Number of ways to arrange $n$ objects where there are $n_1$ objects of type 1, $n_2$ objects of type 2, etc.: $\binom{n}{n_1, n_2, \ldots, n_k} = \frac{n!}{n_1! \cdot n_2! \cdot \ldots \cdot n_k!}$
- **Pigeonhole Principle**: If $n$ items are placed into $m$ containers and $n > m$, then at least one container has more than one item

### Problem-Solving Strategies

- **Break down complex arrangements** into simpler cases
- Use **complementary counting** when it's easier to count what's not in a set
- For complex problems, try **recurrence relations** to connect to simpler subproblems
- In trading contexts, think about **combinations of assets** or **permutations of trades**
- **Symmetry arguments** can simplify many problems where outcomes are equivalent

### Common Pitfalls

- Confusing permutations (order matters) with combinations (order doesn't matter)
- Forgetting to account for overcounting when objects are indistinguishable
- Neglecting edge cases (empty set, single-element set)
- Not recognizing when the problem needs the inclusion-exclusion principle

### Example Problems

**Problem 1: Trading Desk Assignment**
*You need to assign 7 traders to 3 different trading desks: equities, fixed income, and derivatives. How many different ways can you make this assignment if each desk must have at least one trader?*

Solution:
1. This is a problem of distributing 7 distinguishable objects (traders) into 3 distinguishable groups (desks) with no empty groups
2. Use inclusion-exclusion principle:
   - Total number of ways without restrictions: $3^7$ (each trader can go to any of 3 desks)
   - Subtract cases where at least one desk is empty:
   - Ways with exactly 1 empty desk: $\binom{3}{1} \cdot 2^7$
   - Ways with exactly 2 empty desks: $\binom{3}{2} \cdot 1^7$
3. Final answer: $3^7 - \binom{3}{1} \cdot 2^7 + \binom{3}{2} \cdot 1^7 = 2187 - 3 \cdot 128 + 3 \cdot 1 = 2187 - 384 + 3 = 1806$

**Problem 2: Portfolio Construction**
*From a universe of 20 stocks, how many different portfolios can be constructed that contain exactly 5 stocks?*

Solution:
1. This is a straightforward combination problem since order doesn't matter
2. $C(20,5) = \binom{20}{5} = \frac{20!}{5!(20-5)!} = \frac{20!}{5!15!}$
3. Calculate: $\frac{20 \cdot 19 \cdot 18 \cdot 17 \cdot 16}{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = \frac{1,860,480}{120} = 15,504$

### Mental Math Techniques

- Memorize common values: $\binom{n}{0}=\binom{n}{n}=1$ and $\binom{n}{1}=\binom{n}{n-1}=n$
- Use symmetry: $\binom{n}{k}=\binom{n}{n-k}$
- Pascal's triangle for quick calculations of binomial coefficients
- Quick factorial approximations using Stirling's formula: $n! \approx \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$
- For large $n$ and small $k$: $\binom{n}{k} \approx \frac{n^k}{k!}$

## Probability

### Key Formulas and Theorems

- **Basic Probability**: $P(A) = \frac{\text{favorable outcomes}}{\text{total outcomes}}$
- **Addition Rule**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Multiplication Rule**: $P(A \cap B) = P(A) \cdot P(B|A)$
- **Conditional Probability**: $P(A|B) = \frac{P(A \cap B)}{P(B)}$
- **Independence**: $A$ and $B$ are independent if $P(A \cap B) = P(A) \cdot P(B)$
- **Law of Total Probability**: $P(A) = \sum_{i} P(A|B_i) \cdot P(B_i)$ where $B_i$ form a partition
- **Expected Value**: $E[X] = \sum_{i} x_i \cdot P(X = x_i)$ or $\int x \cdot f(x) \, dx$ for continuous variables
- **Variance**: $Var(X) = E[(X-E[X])^2] = E[X^2] - (E[X])^2$
- **Linearity of Expectation**: $E[aX + bY] = aE[X] + bE[Y]$ (regardless of independence)
- **Common Distributions**:
  - Binomial: $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$, $E[X] = np$, $Var(X) = np(1-p)$
  - Poisson: $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$, $E[X] = Var(X) = \lambda$
  - Normal: $f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$, $E[X] = \mu$, $Var(X) = \sigma^2$

### Problem-Solving Strategies

- **Decompose complex events** into simpler ones using the law of total probability
- Use **symmetry and invariance** to simplify calculations
- For sequential events, use **tree diagrams** to organize possibilities
- In trading, think about **expected value of strategies** and **risk-reward tradeoffs**
- For continuous variables, use **discretization** to approximate when formulas are complex

### Common Pitfalls

- Neglecting dependencies between events
- Confusing conditional probabilities: $P(A|B) \neq P(B|A)$
- Misinterpreting independent events as mutually exclusive (they're usually not)
- Forgetting that correlations don't imply causation
- In trading: ignoring survivorship bias in historical data analysis

### Example Problems

**Problem 1: Trading Strategy Evaluation**
*A trading strategy has a 55% chance of making a winning trade. If you make 100 independent trades, what is the probability of having at least 60 winning trades?*

Solution:
1. This follows a binomial distribution: $X \sim B(100, 0.55)$
2. We need $P(X \geq 60) = 1 - P(X \leq 59)$
3. Using the normal approximation since $n$ is large:
   - $\mu = np = 100 \cdot 0.55 = 55$
   - $\sigma = \sqrt{np(1-p)} = \sqrt{100 \cdot 0.55 \cdot 0.45} \approx 4.97$
   - $P(X \geq 60) = P(Z \geq \frac{59.5-55}{4.97}) = P(Z \geq 0.91) \approx 0.1814$
4. Using continuity correction, we get $P(X \geq 60) \approx 0.1814$ or about 18.14%

**Problem 2: Market Movement Probability**
*The daily returns of a stock follow a normal distribution with mean 0.05% and standard deviation 1.2%. What is the probability that the stock will go up by more than 2% in a single day?*

Solution:
1. We need to find $P(X > 2\%)$ where $X \sim N(0.05\%, 1.2\%)$
2. Standardizing: $P(X > 2\%) = P\left(Z > \frac{2 - 0.05}{1.2}\right) = P(Z > 1.625)$
3. Using the standard normal table or function: $P(Z > 1.625) \approx 0.0521$
4. Therefore, there's approximately a 5.21% chance of the stock going up by more than 2% in a single day

### Mental Math Techniques

- For binomial problems with $n \geq 30$, use normal approximation: $B(n,p) \approx N(np, np(1-p))$
- For small probabilities, use Poisson approximation to binomial: $B(n,p) \approx Poisson(np)$ when $n$ is large and $p$ is small
- Rule of 72: Time to double money at interest rate $r\%$ is approximately $\frac{72}{r}$
- Quick standard deviation estimate: For a normal distribution, about 68% of values lie within 1 standard deviation, 95% within 2, and 99.7% within 3

## Bayes' Theorem

### Key Formulas and Theorems

- **Bayes' Theorem**: $P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$
- Expanded form: $P(A|B) = \frac{P(B|A) \cdot P(A)}{\sum_i P(B|A_i) \cdot P(A_i)}$
- **Prior probability**: $P(A)$ - Initial belief before evidence
- **Posterior probability**: $P(A|B)$ - Updated belief after evidence
- **Likelihood**: $P(B|A)$ - Probability of evidence given hypothesis

### Problem-Solving Strategies

- Always identify clearly: prior probabilities, likelihoods, and what the posterior should be
- Use **tree diagrams** for complex Bayesian problems
- For multiple updates, use the posterior from one step as the prior for the next
- In trading contexts, think of Bayes' theorem as **updating market beliefs** with new information
- When working with multiple hypotheses, organize information in a table

### Common Pitfalls

- Confusing $P(A|B)$ with $P(B|A)$ (the "prosecutor's fallacy")
- Neglecting to normalize probabilities (ensure they sum to 1)
- Using incorrect prior probabilities that don't reflect base rates
- In trading: overreacting to new information or underreacting (not updating enough)

### Example Problems

**Problem 1: Trading Signal Reliability**
*A trading signal correctly predicts market rises 80% of the time and market falls 70% of the time. Historically, the market rises 55% of days. If the signal predicts a market rise tomorrow, what is the probability that the market will actually rise?*

Solution:
1. Define events:
   - $R$ = Market rises
   - $S$ = Signal predicts rise
2. Given information:
   - $P(S|R) = 0.8$ (Signal accuracy when market rises)
   - $P(S|R^c) = 0.3$ (Signal false positive when market falls)
   - $P(R) = 0.55$ (Prior probability of market rise)
3. Using Bayes' theorem to find $P(R|S)$:
   $P(R|S) = \frac{P(S|R) \cdot P(R)}{P(S|R) \cdot P(R) + P(S|R^c) \cdot P(R^c)}$
4. Substituting values:
   $P(R|S) = \frac{0.8 \cdot 0.55}{0.8 \cdot 0.55 + 0.3 \cdot 0.45} = \frac{0.44}{0.44 + 0.135} = \frac{0.44}{0.575} \approx 0.7652$
5. Therefore, if the signal predicts a rise, there's approximately a 76.52% probability that the market will actually rise

**Problem 2: Data Quality Assessment**
*You're evaluating a dataset for algorithmic trading. You know that 5% of datasets have data quality issues. Your validation test has a 98% chance of detecting issues when they exist and a 3% false positive rate. If your test flags a dataset, what is the probability it actually has issues?*

Solution:
1. Define events:
   - $I$ = Dataset has issues
   - $F$ = Test flags the dataset
2. Given information:
   - $P(I) = 0.05$ (Prior probability of issues)
   - $P(F|I) = 0.98$ (Test sensitivity)
   - $P(F|I^c) = 0.03$ (Test false positive rate)
3. Using Bayes' theorem to find $P(I|F)$:
   $P(I|F) = \frac{P(F|I) \cdot P(I)}{P(F|I) \cdot P(I) + P(F|I^c) \cdot P(I^c)}$
4. Substituting values:
   $P(I|F) = \frac{0.98 \cdot 0.05}{0.98 \cdot 0.05 + 0.03 \cdot 0.95} = \frac{0.049}{0.049 + 0.0285} = \frac{0.049}{0.0775} \approx 0.6323$
5. Therefore, if the test flags a dataset, there's approximately a 63.23% probability it actually has issues, despite the high test accuracy

### Mental Math Techniques

- For simple Bayesian updates, remember that the posterior odds equal the prior odds multiplied by the likelihood ratio: $\frac{P(A|B)}{P(A^c|B)} = \frac{P(A)}{P(A^c)} \cdot \frac{P(B|A)}{P(B|A^c)}$
- When the prior probability is small, even a test with high sensitivity and specificity can give a posterior probability that's still relatively small
- In trading contexts, a rule of thumb: If your confidence in a trade is $p$, and new information is $n$ times more likely under your hypothesis than the alternative, your new confidence should be about $\frac{p \cdot n}{p \cdot n + (1-p)}$

## Logic

### Key Formulas and Theorems

- **Basic Operators**:
  - Negation: $\neg p$ (not p)
  - Conjunction: $p \wedge q$ (p and q)
  - Disjunction: $p \vee q$ (p or q)
  - Implication: $p \rightarrow q$ (if p then q)
  - Biconditional: $p \leftrightarrow q$ (p if and only if q)
- **De Morgan's Laws**:
  - $\neg(p \wedge q) = \neg p \vee \neg q$
  - $\neg(p \vee q) = \neg p \wedge \neg q$
- **Implication Rules**:
  - $p \rightarrow q \equiv \neg p \vee q$
  - Contrapositive: $p \rightarrow q \equiv \neg q \rightarrow \neg p$
- **Logical Equivalence**: $p \leftrightarrow q \equiv (p \rightarrow q) \wedge (q \rightarrow p)$
- **Quantifiers**:
  - Universal: $\forall x, P(x)$ (for all x, P(x) is true)
  - Existential: $\exists x, P(x)$ (there exists an x such that P(x) is true)

### Problem-Solving Strategies

- **Truth tables** for analyzing complex logical expressions
- Use **indirect proofs** (contradiction or contrapositive) when direct proofs are difficult
- For complex implications, break them down into component logical steps
- In trading contexts, use logic to analyze **decision trees** and **conditional strategies**
- For sequences of logical deductions, use organized chains of implications

### Common Pitfalls

- Confusing implication ($p \rightarrow q$) with biconditional ($p \leftrightarrow q$)
- Incorrectly negating complex statements (use De Morgan's laws carefully)
- Assuming that $p \rightarrow q$ means $q \rightarrow p$ (the converse is not logically equivalent)
- In trading: creating overly complex logical conditions that are hard to evaluate quickly

### Example Problems

**Problem 1: Trading Strategy Logic**
*You're considering a strategy that buys a stock when either (1) both the 50-day moving average is above the 200-day moving average AND the RSI is below 30, or (2) the stock has fallen more than 10% in a week. Express this as a logical formula and simplify it.*

Solution:
1. Define propositions:
   - $p$: 50-day MA > 200-day MA
   - $q$: RSI < 30
   - $r$: Stock has fallen > 10% in a week
2. Express the strategy: $(p \wedge q) \vee r$
3. This is already in simplified form (disjunctive normal form)
4. The formula means: Buy when either condition (1) OR condition (2) is satisfied

**Problem 2: Market Scenario Analysis**
*Given: "If inflation rises, then either the Fed raises rates or the bond market sells off." You observe that the bond market didn't sell off. What can you logically conclude?*

Solution:
1. Define propositions:
   - $p$: Inflation rises
   - $q$: Fed raises rates
   - $r$: Bond market sells off
2. Given statement: $p \rightarrow (q \vee r)$
3. Observed: $\neg r$ (bond market didn't sell off)
4. From the implication and $\neg r$, we know that if $p$ is true, then $q$ must be true (since one part of the disjunction must be true)
5. This gives us: $p \rightarrow q$ (If inflation rises, then the Fed raises rates)
6. We cannot determine whether inflation actually rose or whether the Fed actually raised rates, only the implication between them

### Mental Math Techniques

- Use truth tables to quickly check logical equivalences
- For implications, remember: "$p \rightarrow q$" is only false when $p$ is true and $q$ is false
- When negating statements with quantifiers: $\neg(\forall x, P(x)) \equiv \exists x, \neg P(x)$ and $\neg(\exists x, P(x)) \equiv \forall x, \neg P(x)$
- In trading contexts, quickly analyze complex conditions by breaking them into simpler components and evaluating each separately

## Mathematical Problem-Solving (General)

### Key Approaches and Techniques

- **First principles thinking**: Break down complex problems into fundamental truths
- **Pattern recognition**: Identify structures and sequences that follow known patterns
- **Invariant analysis**: Look for quantities that remain unchanged through transformations
- **Extreme cases**: Test solutions against boundary conditions
- **Dimensional analysis**: Use units to check formula consistency
- **Symmetry exploitation**: Use symmetrical properties to simplify calculations
- **Recurrence relations**: Express complex problems in terms of simpler versions of themselves

### Problem-Solving Strategies

- **Start with simple cases** to build intuition before tackling the general problem
- Use **multiple methods** to verify your solution
- **Draw diagrams** to visualize abstract problems
- **Estimate the answer** before calculating precisely to catch gross errors
- In trading contexts, develop **heuristics** for quick approximations based on known benchmarks

### Common Pitfalls

- Overcomplicating problems that have elegant, simple solutions
- Not verifying solutions with test cases
- Overlooking implicit assumptions in problem statements
- In trading: applying sophisticated mathematics without understanding the underlying assumptions
- Confirmation bias: looking only for evidence that supports your initial approach

### Example Problems

**Problem 1: Expected Trade Value**
*You have a trading opportunity with a 60% chance of making $5,000 and a 40% chance of losing $6,000. What is the expected value of this trade, and should you take it if you need a positive expected value?*

Solution:
1. Calculate the expected value: 
   $E[X] = 0.6 \times \$5,000 + 0.4 \times (-\$6,000) = \$3,000 - \$2,400 = \$600$
2. Since the expected value is positive ($\$600$), this trade has a positive expectation
3. However, consider other factors like risk tolerance and the variance before deciding

**Problem 2: Trading System Performance**
*A trading system makes 100 trades per year with a win rate of 55%. Winning trades make an average of 2 units, while losing trades lose an average of 1 unit. What is the expected annual return in units, and what is the standard deviation of the annual return?*

Solution:
1. Expected return per trade: 
   $E[X] = 0.55 \times 2 + 0.45 \times (-1) = 1.1 - 0.45 = 0.65$ units
2. Expected annual return:
   $E[Y] = 100 \times 0.65 = 65$ units
3. Variance per trade:
   $Var(X) = E[X^2] - (E[X])^2$
   $E[X^2] = 0.55 \times 2^2 + 0.45 \times (-1)^2 = 0.55 \times 4 + 0.45 = 2.2 + 0.45 = 2.65$
   $Var(X) = 2.65 - 0.65^2 = 2.65 - 0.4225 = 2.2275$
4. Standard deviation per trade:
   $\sigma_X = \sqrt{2.2275} \approx 1.4925$ units
5. Standard deviation of annual return (assuming independent trades):
   $\sigma_Y = \sqrt{100} \times 1.4925 = 10 \times 1.4925 \approx 14.925$ units

### Mental Math Techniques

- **Fermi estimation**: Break down complex problems into simpler parts with rough estimates
- **Quick powers**: Remember that $2^{10} \approx 10^3$ for quick approximations
- **Compounding approximation**: For small returns $r$ over $n$ periods, $n \times r$ gives a rough estimate
- **Rule of 70/72**: Time to double at growth rate $r\%$ is approximately $\frac{70}{r}$ or $\frac{72}{r}$
- **Mental exponentiation**: Use the fact that $(a+b)^2 = a^2 + 2ab + b^2$ to mentally square numbers close to round numbers

## Quick Reference for Mental Math in Trading

### Approximations and Shortcuts

- **Percentages**: 
  - $x\%$ of $y = y\%$ of $x$ (e.g., $8\%$ of $25 = 25\%$ of $8 = 2$)
  - To find $1\%$, divide by 100. For other percentages, scale accordingly
  
- **Compound Growth**:
  - Rule of 72: Money doubles in approximately $\frac{72}{r}$ years at interest rate $r\%$
  - Quick compounding: 10% growth for 7 years ≈ doubling
  
- **Statistical Approximations**:
  - For normal distributions: 68% within 1σ, 95% within 2σ, 99.7% within 3σ
  - For large samples: $\sigma_{\bar{x}} \approx \frac{\sigma}{\sqrt{n}}$
  
- **Risk Calculations**:
  - Sharpe ratio = $\frac{\text{excess return}}{\text{volatility}}$
  - Quick volatility scaling: Daily vol × $\sqrt{252} \approx$ Annual vol
  
- **Option Approximations**:
  - ATM option delta ≈ 0.5
  - Option gamma is highest ATM and drops off on both sides
  - Quick vega estimate: 1% vol change affects 1-month ATM option by about 0.4%

### Trading-Specific Heuristics

- **Kelly Criterion** simplified: Optimal bet size ≈ $\frac{\text{edge}}{\text{odds}}$
- **Position Sizing**: Position risk ($\%$ of portfolio) ≈ $\frac{\text{target risk}}{\text{position volatility}}$
- **Correlation Effects**: Two uncorrelated assets with equal volatility combined reduce portfolio volatility by $\approx \frac{1}{\sqrt{2}}$
- **Breakeven Calculation**: After losing $x\%$, you need a return of $\frac{x}{100-x} \times 100\%$ to break even
- **Win/Loss Ratio**: To break even with win probability $p$, you need a win/loss ratio of at least $\frac{1-p}{p}$

## Final Tips for Quant Interviews

1. **Practice explaining your thought process** out loud as you solve problems
2. **Verify solutions** by plugging back into the original problem
3. **Consider edge cases** to test the robustness of your solution
4. **Look for patterns** in historical SIG interview questions
5. **Balance intuition and rigor**: Show both quick estimation skills and careful mathematical precision
6. **Connect to financial applications** whenever possible
7. **Be honest about uncertainties** rather than making unfounded assertions
8. **Demonstrate speed and accuracy** in your calculations but prioritize correctness

Remember that quantitative trading interviews often evaluate not just your answers but your approach to solving problems under pressure. Good luck with your preparation!