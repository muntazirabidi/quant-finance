# Chapter 2: Confidence Intervals - Statistical Inference

## Overview

This chapter explores the crucial concept of confidence intervals in statistical inference - a fundamental tool for quantifying uncertainty in parameter estimation. We move beyond point estimates to understand how to construct intervals that capture the true parameter value with a specified probability.

## Key Topics

### Section 2.1: Basic Concepts

- Definition and interpretation of confidence intervals
- Point estimates vs interval estimates
- Confidence level and significance level ($\alpha$)
- One-sided confidence limits
- Central and equal-tailed intervals

### Section 2.2: CLT Based Confidence Intervals

- Constructing CIs using Central Limit Theorem
- Large sample approximations
- Normal approximation method

### Section 2.3: MLEs and Asymptotic Distribution

- Using asymptotic distribution of Maximum Likelihood Estimators
- Fisher Information matrix $I(\theta)$
- Approximate confidence intervals: $(\hat{\theta} \pm z_{\alpha/2}I(\hat{\theta})^{-1/2})$
- Reparametrization techniques

### Section 2.4: Special Distributions

- Chi-square distribution: $\chi^2_r$
- Student's t-distribution: $t_r$
- Properties and relationships to Normal distribution
- Independence of $\bar{X}$ and $S^2$ in normal samples

## Key Formulas

1. Basic Normal CI:
   $(\bar{X} \pm z_{\alpha/2}\frac{\sigma_0}{\sqrt{n}})$

2. MLE-based CI:
   $(\hat{\theta} \pm z_{\alpha/2}\sqrt{I(\hat{\theta})^{-1}})$

3. Student's t CI for normal mean:
   $(\bar{X} \pm t_{n-1,\alpha/2}\frac{S}{\sqrt{n}})$

4. Chi-square CI for variance:
   $(\frac{(n-1)S^2}{\chi^2_{n-1,\alpha/2}}, \frac{(n-1)S^2}{\chi^2_{n-1,1-\alpha/2}})$

## Important Distributions

1. Chi-square: $Y = Z_1^2 + ... + Z_r^2$ where $Z_i \sim N(0,1)$

   - $Y \sim \chi^2_r$
   - $E(Y) = r$
   - $Var(Y) = 2r$

2. Student's t: $T = \frac{Z}{\sqrt{Y/r}}$ where $Z \sim N(0,1)$ and $Y \sim \chi^2_r$
   - $T \sim t_r$
   - As $r \to \infty$, $t_r \to N(0,1)$

## Critical Concepts

1. **Pivotal Quantity**: A function of both data and parameter whose distribution doesn't depend on unknown parameters.
   Example: $T = \frac{\bar{X}-\mu}{S/\sqrt{n}} \sim t_{n-1}$

2. **Independence in Normal Samples**:
   - $\bar{X}$ and $S^2$ are independent
   - $\bar{X} \sim N(\mu, \sigma^2/n)$
   - $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$

## Further Reading and Practice

Detailed notes for each section are available in separate files within this chapter's directory. These include:

- Worked examples
- Proofs of key theorems
- Practice problems
- Applications to real data

---

This chapter forms a crucial foundation for statistical inference, bridging the gap between point estimation and practical decision-making under uncertainty.

_Note: For detailed derivations, proofs, and examples, please refer to the section-specific notes in this directory._
