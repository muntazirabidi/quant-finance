# Guide to SIG Trading Problem-Solving Assessment

This guide focuses on efficient problem-solving strategies for the SIG Trading Assessment, with emphasis on speed and accuracy under time pressure.

## 1. Probability & Bayes' Theorem

### Key Formulas and Theorems
- **Basic probability**: $P(A) = \frac{\text{favorable outcomes}}{\text{total outcomes}}$
- **Conditional probability**: $P(A|B) = \frac{P(A \cap B)}{P(B)}$
- **Bayes' Theorem**: $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$
- **Law of Total Probability**: $P(A) = \sum_{i} P(A|B_i)P(B_i)$
- **Independence**: $P(A \cap B) = P(A)P(B)$
- **Expected Value**: $E[X] = \sum_{i} x_i P(X=x_i)$
- **Variance**: $\text{Var}(X) = E[X^2] - (E[X])^2$
- **Linearity of Expectation**: $E[X + Y] = E[X] + E[Y]$ (works even when $X$ and $Y$ are dependent)

### Fast Problem-Solving Strategies
- Use **tree diagrams** for conditional sequences
- When faced with complex conditional probabilities, try writing out **explicit sample spaces**
- For expected value, break problems into **simpler components** and apply linearity
- Use **symmetry** to simplify calculations
- Apply the **complement rule** when "at least one" is involved: $P(\text{at least one}) = 1 - P(\text{none})$
- For repeated trials, identify if it's a **binomial scenario** to use: $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$

### Common Pitfalls
- **Confusing $P(A|B)$ with $P(B|A)$** - always verify which event is conditional
- **Failing to account for dependence** between events
- **Miscounting the sample space** - verify denominators carefully
- **Normalizing incorrectly** in Bayesian updates
- **Overlooking the difference** between "and" (intersection) and "or" (union)

### Example Problem
> A trader makes profitable trades with 60% probability. If they make 5 trades, what is the probability of making exactly 3 profitable trades?

**Solution**:
1. Identify as binomial: $n=5$ trials, probability of success $p=0.6$
2. Apply formula: $P(X=3) = \binom{5}{3}(0.6)^3(0.4)^2$
3. Calculate: $\binom{5}{3} = \frac{5!}{3!(5-3)!} = \frac{5 \cdot 4 \cdot 3!}{3! \cdot 2 \cdot 1} = 10$
4. $P(X=3) = 10 \cdot (0.6)^3 \cdot (0.4)^2 = 10 \cdot 0.216 \cdot 0.16 = 10 \cdot 0.03456 = 0.3456$
5. Therefore, probability $\approx 0.346$ or $34.6\%$

### Mental Math Tricks
- For probabilities close to 0.5, use the **approximation** that $\binom{n}{k}0.5^n \approx \sqrt{\frac{2}{\pi n}}$
- For binomial problems, **recognize special patterns**: 
  * With $p=0.5$, most likely outcome is $\frac{n}{2}$ (or both $\frac{n-1}{2}$ and $\frac{n+1}{2}$ if $n$ is odd)
  * With $p=\frac{1}{3}$, $E[X]=\frac{n}{3}$
- When working with conditional probability, sometimes it's easier to use the **definition directly**: $P(A|B) = \frac{P(A \cap B)}{P(B)}$

## 2. Combinatorics & Counting

### Key Formulas and Theorems
- **Permutations**: $P(n,r) = \frac{n!}{(n-r)!} = n \times (n-1) \times ... \times (n-r+1)$
- **Combinations**: $\binom{n}{r} = \frac{n!}{r!(n-r)!}$
- **Permutations with repetition**: $n^r$
- **Combinations with repetition**: $\binom{n+r-1}{r}$
- **Stars and bars**: Ways to distribute $n$ items into $k$ groups = $\binom{n+k-1}{k-1}$
- **Principle of Inclusion-Exclusion**: $|A \cup B \cup C| = |A|+|B|+|C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$
- **Derangements** (no fixed points): $D(n) = n! \times (1-\frac{1}{1!}+\frac{1}{2!}-\frac{1}{3!}+...+\frac{(-1)^n}{n!}) \approx \frac{n!}{e}$ (rounded to nearest integer)

### Fast Problem-Solving Strategies
- Always clarify: **Does order matter?** (permutation vs. combination)
- For complex problems, break into **cases** based on constraints
- Use **complementary counting** for "at least one" or "no" scenarios
- For recursive patterns, try to find a **recurrence relation**
- When faced with constraints, sometimes it's easier to **count the complement** (invalid arrangements) and subtract from total
- Look for **symmetry** to reduce calculation burden

### Common Pitfalls
- **Overcounting** by not accounting for identical items
- **Undercounting** by missing valid arrangements
- **Confusing when to add vs. multiply** counts
- **Forgetting to account for "zero" cases** (especially in "at least" scenarios)
- **Misapplying formulas** for arrangements with/without repetition

### Example Problem
> A trading algorithm needs to select 3 stocks from a pool of 8 tech stocks and 7 financial stocks. How many ways can it select exactly 2 tech stocks and 1 financial stock?

**Solution**:
1. Break into separate selections: need to choose 2 tech stocks and 1 financial stock
2. Tech stock selection: $\binom{8}{2} = \frac{8 \cdot 7}{2 \cdot 1} = 28$ ways
3. Financial stock selection: $\binom{7}{1} = 7$ ways
4. Apply multiplication principle: $28 \times 7 = 196$ ways

### Mental Math Tricks
- **Symmetry in combinations**: $\binom{n}{r} = \binom{n}{n-r}$
- For combinations, **factorize before multiplying**: 
  $\binom{10}{3} = \frac{10 \cdot 9 \cdot 8}{3 \cdot 2 \cdot 1} = \frac{10 \cdot 3}{3} \cdot \frac{9}{3} \cdot \frac{8}{2} = 30 \cdot 3 \cdot 4 = 360$
- When computing $\binom{n}{r}$, try to **cancel terms** early: $\binom{20}{18} = \binom{20}{2} = \frac{20 \cdot 19}{2 \cdot 1} = 190$
- For sequential combinations, **use the previous result**: if you know $\binom{n}{r}$, then $\binom{n}{r+1} = \binom{n}{r} \cdot \frac{n-r}{r+1}$

## 3. Quantitative & Logical Reasoning

### Key Formulas and Theorems
- **Algebraic identities**: 
  * $(a+b)^2 = a^2+2ab+b^2$
  * $(a-b)^2 = a^2-2ab+b^2$
  * $(a+b)(a-b) = a^2-b^2$
- **Quadratic formula**: $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$
- **Arithmetic sequence**: 
  * $a_n = a_1 + (n-1)d$
  * Sum = $\frac{n(a_1+a_n)}{2} = \frac{n(2a_1+(n-1)d)}{2}$
- **Geometric sequence**: 
  * $a_n = a_1r^{n-1}$
  * Sum = $\frac{a_1(1-r^n)}{1-r}$ (for $|r|<1$)
- **Logarithm properties**: 
  * $\log(ab) = \log(a)+\log(b)$
  * $\log(\frac{a}{b}) = \log(a)-\log(b)$
  * $\log(a^n) = n \log(a)$

### Fast Problem-Solving Strategies
- **Estimate and eliminate** clearly wrong answers first
- **Work backwards** from answer choices when direct calculation is difficult
- **Substitute simple values** to test relationships
- **Look for hidden patterns** in data or sequences
- For inequalities, **test boundary cases** and check direction of inequality
- **Dimensional analysis**: ensure units match on both sides of an equation

### Common Pitfalls
- **Sign errors** in algebraic manipulations
- **Off-by-one errors** in counting or sequences
- **Overlooking constraints** in the problem statement
- **Failing to check** if a solution satisfies all conditions
- **Misinterpreting "if and only if"** conditions

### Example Problem
> A trader notices that the price of a stock follows the pattern: 100, 90, 81, 72.9, ... 
> What will be the price after 10 days if this pattern continues?

**Solution**:
1. Identify the pattern: Each term is 0.9 times the previous term (a geometric sequence)
2. First term $a_1 = 100$, common ratio $r = 0.9$
3. To find the 10th term: $a_{10} = a_1r^{10-1} = 100(0.9)^9$
4. Calculate step by step: 
   - $(0.9)^9 = (0.9)^{8+1} = (0.9)^8 \times 0.9$
   - $(0.9)^2 = 0.81$, $(0.9)^4 = (0.81)^2 = 0.6561$, $(0.9)^8 = (0.6561)^2 = 0.43046721$
   - $(0.9)^9 = 0.43046721 \times 0.9 = 0.387420489$
5. $a_{10} = 100 \times 0.387420489 = 38.74$ (rounded to 2 decimal places)

### Mental Math Tricks
- **Power of 2 approximations**: $2^{10} \approx 10^3$, $2^{20} \approx 10^6$
- **Percentage shortcuts**: 
  * 10% is dividing by 10
  * 5% is half of 10%
  * To find x% of y, find y% of x (commutative)
- **Quick squaring**:
  * For numbers near 100: $(100+n)^2 = 10000 + 200n + n^2$
  * For numbers near 50: $(50+n)^2 = 2500 + 100n + n^2$
- **Difference of squares** for multiplication: $a \times b = \left(\frac{a+b}{2}\right)^2 - \left(\frac{a-b}{2}\right)^2$

## 4. Mathematical Concepts

### Key Formulas and Theorems
- **Derivatives**: 
  * $\frac{d}{dx}(x^n) = nx^{n-1}$
  * $\frac{d}{dx}(e^x) = e^x$
  * $\frac{d}{dx}(\ln(x)) = \frac{1}{x}$
- **Integration**: 
  * $\int x^n dx = \frac{x^{n+1}}{n+1} + C$ (for $n \neq -1$)
  * $\int \frac{1}{x} dx = \ln|x| + C$
- **Matrix determinant** (2×2): $|A| = ad-bc$ where $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$
- **Matrix inverse** (2×2): If $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, then $A^{-1} = \frac{1}{ad-bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$
- **Taylor series**: 
  * $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + ...$
  * $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - ...$ (for $|x|<1$)

### Fast Problem-Solving Strategies
- For optimization, **set derivative to zero** and check endpoints
- Use **linear approximation** for functions near known values: $f(x) \approx f(a) + f'(a)(x-a)$
- **Exploit symmetry** and invariance when possible
- For calculus problems, **sketch the function** to understand behavior
- For matrix problems, check for **special properties** (symmetric, diagonal, etc.)

### Common Pitfalls
- **Forgetting to check critical points** for max/min
- **Sign errors** in derivatives and integrals
- **Overlooking domain restrictions**
- **Confusing necessary vs. sufficient conditions**
- **Matrix multiplication order** errors (not commutative)

### Example Problem
> A trader models the profit function for a trading strategy as $P(x) = 10x - x^2$, where $x$ is the position size in thousands. What is the optimal position size to maximize profit?

**Solution**:
1. To maximize profit, find where derivative equals zero: $P'(x) = 10 - 2x$
2. Set $P'(x) = 0$: $10 - 2x = 0$
3. Solve for $x$: $2x = 10$, therefore $x = 5$
4. Check second derivative: $P''(x) = -2 < 0$, confirming this is a maximum
5. Therefore, optimal position size is 5,000 units ($x = 5$ thousand)
6. Maximum profit is $P(5) = 10(5) - 5^2 = 50 - 25 = 25$ thousand dollars

### Mental Math Tricks
- **First-order approximations**: $e^{0.1} \approx 1.1$, $\ln(1.1) \approx 0.1$
- **Quick determinant calculation** for 2×2 matrices: multiply diagonals and subtract
- **Quadratics with integer roots**: if $x^2 + bx + c = 0$ has integer roots $p$ and $q$, then $b = -(p+q)$ and $c = pq$
- **Function approximations** near zero:
  * $\sin(x) \approx x$ for small $x$ (in radians)
  * $\cos(x) \approx 1 - \frac{x^2}{2}$ for small $x$ (in radians)

## 5. Finance & Trading Concepts

### Key Formulas and Theorems
- **Expected return**: $E[R] = \sum_{i} R_i \times P(R_i)$
- **Sharpe ratio**: $\frac{E[R] - R_f}{\sigma}$ where $R_f$ is risk-free rate and $\sigma$ is standard deviation
- **Kelly criterion**: optimal bet size = $\frac{\text{edge}}{\text{odds}} = \frac{bp-q}{b}$ where $p$=win probability, $q$=loss probability, $b$=net odds received
- **Put-call parity**: $C - P = S - K \cdot e^{-rt}$ (C=call price, P=put price, S=stock price, K=strike price)
- **CAPM**: $E[R] = R_f + \beta(E[R_m] - R_f)$

### Fast Problem-Solving Strategies
- Use **expected value** to evaluate trading decisions
- Apply **risk-neutral pricing** for option-like payoffs
- For arbitrage questions, look for **inconsistent pricing** across related securities
- In market scenarios, identify **zero-sum constraints** where applicable
- For portfolio problems, use **weighted averages** of individual securities

### Common Pitfalls
- **Ignoring transaction costs** in trading problems
- **Overlooking the time value of money**
- **Misunderstanding risk vs. return** relationships
- **Confusing causation and correlation** in market relationships
- **Failing to account for constraints** like position limits or margin requirements

### Example Problem
> A trader is considering two trading strategies. Strategy A has a 60% chance of making $5,000 and a 40% chance of losing $4,000. Strategy B has a 75% chance of making $3,000 and a 25% chance of losing $5,000. Which strategy has the higher expected value?

**Solution**:
1. Calculate expected value for Strategy A:
   $E[A] = 0.6 \times \$5,000 + 0.4 \times (-\$4,000) = \$3,000 - \$1,600 = \$1,400$

2. Calculate expected value for Strategy B:
   $E[B] = 0.75 \times \$3,000 + 0.25 \times (-\$5,000) = \$2,250 - \$1,250 = \$1,000$

3. Compare: $E[A] = \$1,400 > E[B] = \$1,000$
   Therefore, Strategy A has the higher expected value.

### Mental Math Tricks
- **Rule of 72**: Time to double money = $\frac{72}{r}$ (where $r$ is percentage return)
- **Quick EV calculations**: For binary outcomes, EV = $p(\text{win amount}) - (1-p)(\text{loss amount})$
- For risk/reward ratios, if win:loss = a:b and win probability is p, then **break-even probability** = $\frac{b}{a+b}$
- **Weighted average shortcuts**: For two assets with weights $w$ and $(1-w)$, the combined property is: $w(\text{property}_1) + (1-w)(\text{property}_2)$

## 6. Additional Practice Problems with Solutions

### Probability Problem
> If you roll two fair six-sided dice, what is the probability that their sum will be greater than 9?

**Solution**:
1. Identify the sample space: When rolling two dice, there are $6 \times 6 = 36$ possible outcomes, all equally likely
2. List the favorable outcomes (sums > 9):
   * Sum of 10: (4,6), (5,5), (6,4) → 3 outcomes
   * Sum of 11: (5,6), (6,5) → 2 outcomes
   * Sum of 12: (6,6) → 1 outcome
3. Total favorable outcomes: $3 + 2 + 1 = 6$
4. $P(\text{sum} > 9) = \frac{6}{36} = \frac{1}{6} \approx 0.167$

### Combinatorics Problem
> In how many ways can a trader select 4 stocks from 10 different stocks for a portfolio, if the order of selection doesn't matter?

**Solution**:
1. This is a combination problem: choosing 4 items from 10 where order doesn't matter
2. Apply the combination formula: $\binom{10}{4} = \frac{10!}{4!(10-4)!} = \frac{10!}{4!6!}$
3. Calculate: $\frac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6!}{4 \cdot 3 \cdot 2 \cdot 1 \cdot 6!} = \frac{10 \cdot 9 \cdot 8 \cdot 7}{24} = \frac{5040}{24} = 210$

### Expected Value Problem
> A trader can invest in Project A which returns $\$10,000$ with probability $0.3$ and loses $\$5,000$ with probability $0.7$, or Project B which returns $\$7,000$ with probability $0.5$ and loses $\$3,000$ with probability $0.5$. Which project has the higher expected value?

**Solution**:
1. Calculate $E[\text{Project A}]$:
   $E[A] = 0.3 \times \$10,000 + 0.7 \times (-\$5,000) = \$3,000 - \$3,500 = -\$500$
   
2. Calculate $E[\text{Project B}]$:
   $E[B] = 0.5 \times \$7,000 + 0.5 \times (-\$3,000) = \$3,500 - \$1,500 = \$2,000$
   
3. Since $E[B] > E[A]$, Project B has the higher expected value.

### Optimization Problem
> A market maker's daily profit function is modeled as $P(x) = 100x - 2x^2$ where $x$ is the number of trades (in hundreds). What is the optimal number of trades to maximize profit, and what is the maximum profit?

**Solution**:
1. To find the maximum, take the derivative: $P'(x) = 100 - 4x$
2. Set equal to zero: $100 - 4x = 0$
3. Solve: $4x = 100$, so $x = 25$
4. Verify it's a maximum: $P''(x) = -4 < 0$ ✓
5. Optimal trades = $25 \times 100 = 2,500$ trades
6. Maximum profit = $P(25) = 100(25) - 2(25)^2 = 2,500 - 2(625) = 2,500 - 1,250 = \$1,250$

## 7. Speed Math Techniques for the Exam

### Fast Multiplication
- **Multiply by 5**: Multiply by 10, then divide by 2
- **Multiply by 25**: Multiply by 100, then divide by 4
- **Multiply by 9**: Multiply by 10, then subtract the original number
- **Squaring numbers ending in 5**: $(10a + 5)^2 = 100a(a+1) + 25$
  Example: $85^2 = 100 \times 8 \times 9 + 25 = 7,200 + 25 = 7,225$

### Quick Approximations
- **Powers of 2 and 10**:
  * $2^{10} = 1,024 \approx 10^3 = 1,000$
  * $2^{20} \approx 10^6 = 1,000,000$
- **Compound Interest**:
  * Money doubles in about 72/r years (r in percent)
  * $1.1^{10} \approx 2.59$ (compound growth of 10% for 10 periods)

### Division Shortcuts
- **Division by 5**: Multiply by 2, then divide by 10
- **Division by 25**: Multiply by 4, then divide by 100
- **Division by 0.1**: Multiply by 10
- **Division by 0.01**: Multiply by 100

### Estimation Techniques
- **Quickly approximate square roots**:
  * For number $n$ close to perfect square $a^2$: $\sqrt{n} \approx a + \frac{n-a^2}{2a}$
  * Example: $\sqrt{50} \approx 7 + \frac{50-49}{14} = 7 + \frac{1}{14} \approx 7.07$
- **Binomial approximation**: $(1+x)^n \approx 1 + nx$ for small $x$
  * Example: $(1.02)^5 \approx 1 + 5(0.02) = 1.1$

## General Test-Taking Strategies for SIG Assessment

1. **Time management**: Allocate approximately 6-7 minutes per question
2. **Skip and return**: Don't get stuck on difficult problems; mark and return later
3. **Estimation**: Use approximation when exact calculation is time-consuming
4. **Work backward**: Check if any answer choices can be eliminated quickly
5. **Draw diagrams**: Visualize probability trees, coordinate systems, or distributions
6. **Check units**: Ensure your solution has the correct units/dimensions
7. **Sanity check answers**: Ask if your answer makes logical sense in context

Remember that SIG values both correct answers and efficient problem-solving approaches. Focus on developing intuition for quick pattern recognition and leveraging symmetry or simplification whenever possible.



---
# Susquehanna Online Assessment Practice Problems

## Expected Value and Probability

1. You play a game where you roll a 6-sided die. If you roll a 1 or 2, you win $5. If you roll a 3 or 4, you win $10. If you roll a 5 or 6, you lose $15. What is your expected profit or loss from this game? Express your answer to the nearest cent.

2. A casino offers a game where you draw 2 cards from a standard 52-card deck without replacement. You win $20 if both cards are aces, $10 if both cards are the same suit, and $5 if both cards are face cards (J, Q, K). What is your expected profit if it costs $3 to play?

3. A modified roulette wheel has 38 slots numbered 0, 00, and 1 through 36. Red covers slots 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, and 36. What is the probability that the ball will land on a red number? Express your answer as a fraction.

## Combinatorics and Counting

4. In how many ways can 5 distinct books be arranged on a shelf if two particular books must always be adjacent to each other?

5. A company password must be 8 characters long and contain only uppercase letters (A-Z) and digits (0-9). Each password must contain at least one letter and at least one digit. How many different possible passwords are there?

6. Eight friends want to play doubles tennis (2 vs 2). In how many different ways can they be divided into 4 teams of 2, where the teams will play each other in a tournament?

## Logic Puzzles

7. All dolphins are mammals. Some mammals live in water. Therefore...
   - All dolphins live in water
   - Some dolphins live in water
   - No dolphins live in water
   - Cannot be determined from the given information

8. You are on an island with three types of inhabitants: knights who always tell the truth, knaves who always lie, and spies who can either tell the truth or lie. You meet three inhabitants labeled A, B, and C.
   
   A says: "I am a knight or B is a knave."
   B says: "C is not a spy."
   C says: "A is a knave."
   
   What types are A, B, and C?

## Geometric Probability

9. A square dartboard has a side length of 20 cm. A circular bullseye with a radius of 5 cm is placed in the center of the board. If you throw a dart and it lands randomly on the board, what is the probability it will hit the bullseye?

10. Two points are selected randomly on a line of length 10. What is the probability that the distance between them is less than 3?

## Advanced Probability

11. You have 3 coins with the following properties:
    - Coin A: Fair (50% heads, 50% tails)
    - Coin B: Biased (70% heads, 30% tails)
    - Coin C: Biased (20% heads, 80% tails)
    
    You select one coin at random and flip it twice. If both flips show heads, what is the probability that you selected Coin B?

12. You're playing a game where you roll a fair 6-sided die repeatedly. You win when you roll a 6, but if you roll a 1, you lose immediately. You can choose to stop at any time and collect $2 for each roll you've made so far. What's the expected value of this game if you use the optimal strategy?

## Calculus and Series

13. Find the value of the following integral:
    ∫(0 to π/2) sin(x) * cos(x) dx

14. A particle moves along a straight line with position function s(t) = 3t³ - 12t² + 9t where t ≥ 0 represents time in seconds and s is measured in meters. At what time(s) is the particle at rest?

15. Find the sum of the infinite series:
    Σ(n=1 to ∞) 3/(2^n)